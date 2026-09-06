#!/usr/bin/env python3
"""Valida assets de imagem sem reescrevê-los.

Verifica convenção de nomes, assinatura/formato, dimensões básicas, sinais de truncamento
e imprime SHA-256. Usa apenas a biblioteca padrão do Python.
"""
from __future__ import annotations

import hashlib
import re
import struct
import sys
import zlib
from pathlib import Path

SUPPORTED = {".png", ".jpg", ".jpeg", ".gif", ".webp"}
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*\.(?:png|jpg|jpeg|gif|webp)$")
BANNED_PARTS = {"final", "definitivo", "corrigido"}
VERSION_RE = re.compile(r"(?:^|-)v\d+(?:-|\.)")


class ValidationError(Exception):
    pass


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def validate_png(data: bytes) -> tuple[int, int]:
    sig = b"\x89PNG\r\n\x1a\n"
    if not data.startswith(sig):
        raise ValidationError("assinatura PNG inválida")
    pos = len(sig)
    width = height = None
    saw_ihdr = saw_iend = False
    while pos < len(data):
        if pos + 12 > len(data):
            raise ValidationError("chunk PNG truncado")
        length = struct.unpack(">I", data[pos:pos + 4])[0]
        ctype = data[pos + 4:pos + 8]
        end = pos + 12 + length
        if end > len(data):
            raise ValidationError("dados de chunk PNG truncados")
        payload = data[pos + 8:pos + 8 + length]
        expected_crc = struct.unpack(">I", data[pos + 8 + length:end])[0]
        actual_crc = zlib.crc32(ctype + payload) & 0xFFFFFFFF
        if actual_crc != expected_crc:
            raise ValidationError(f"CRC inválido no chunk {ctype.decode('ascii', 'replace')}")
        if ctype == b"IHDR":
            if saw_ihdr or length != 13:
                raise ValidationError("IHDR PNG inválido")
            width, height = struct.unpack(">II", payload[:8])
            saw_ihdr = True
        elif ctype == b"IEND":
            if length != 0:
                raise ValidationError("IEND PNG inválido")
            saw_iend = True
            if end != len(data):
                raise ValidationError("bytes extras após IEND")
            break
        pos = end
    if not saw_ihdr or not saw_iend or not width or not height:
        raise ValidationError("estrutura PNG incompleta")
    return width, height


def validate_gif(data: bytes) -> tuple[int, int]:
    if len(data) < 13 or data[:6] not in (b"GIF87a", b"GIF89a"):
        raise ValidationError("assinatura GIF inválida")
    if data[-1:] != b";":
        raise ValidationError("GIF sem trailer; possível truncamento")
    width, height = struct.unpack("<HH", data[6:10])
    if not width or not height:
        raise ValidationError("dimensões GIF inválidas")
    return width, height


def validate_jpeg(data: bytes) -> tuple[int, int]:
    if len(data) < 4 or not data.startswith(b"\xff\xd8") or not data.endswith(b"\xff\xd9"):
        raise ValidationError("JPEG inválido ou truncado")
    pos = 2
    sof_markers = {0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF}
    while pos < len(data) - 2:
        while pos < len(data) and data[pos] != 0xFF:
            pos += 1
        while pos < len(data) and data[pos] == 0xFF:
            pos += 1
        if pos >= len(data):
            break
        marker = data[pos]
        pos += 1
        if marker in (0xD8, 0xD9) or 0xD0 <= marker <= 0xD7 or marker == 0x01:
            continue
        if pos + 2 > len(data):
            raise ValidationError("segmento JPEG truncado")
        seglen = struct.unpack(">H", data[pos:pos + 2])[0]
        if seglen < 2 or pos + seglen > len(data):
            raise ValidationError("segmento JPEG inválido")
        if marker in sof_markers:
            if seglen < 7:
                raise ValidationError("SOF JPEG inválido")
            height, width = struct.unpack(">HH", data[pos + 3:pos + 7])
            if not width or not height:
                raise ValidationError("dimensões JPEG inválidas")
            return width, height
        pos += seglen
    raise ValidationError("dimensões JPEG não encontradas")


def _u24le(b: bytes) -> int:
    return b[0] | (b[1] << 8) | (b[2] << 16)


def validate_webp(data: bytes) -> tuple[int, int]:
    if len(data) < 20 or data[:4] != b"RIFF" or data[8:12] != b"WEBP":
        raise ValidationError("assinatura WEBP inválida")
    declared = struct.unpack("<I", data[4:8])[0] + 8
    if declared > len(data):
        raise ValidationError("WEBP truncado")
    ctype = data[12:16]
    size = struct.unpack("<I", data[16:20])[0]
    payload = data[20:20 + size]
    if len(payload) < size:
        raise ValidationError("chunk WEBP truncado")
    if ctype == b"VP8X":
        if len(payload) < 10:
            raise ValidationError("VP8X inválido")
        return 1 + _u24le(payload[4:7]), 1 + _u24le(payload[7:10])
    if ctype == b"VP8 ":
        if len(payload) < 10 or payload[3:6] != b"\x9d\x01\x2a":
            raise ValidationError("VP8 inválido")
        width = struct.unpack("<H", payload[6:8])[0] & 0x3FFF
        height = struct.unpack("<H", payload[8:10])[0] & 0x3FFF
        return width, height
    if ctype == b"VP8L":
        if len(payload) < 5 or payload[0] != 0x2F:
            raise ValidationError("VP8L inválido")
        bits = int.from_bytes(payload[1:5], "little")
        width = (bits & 0x3FFF) + 1
        height = ((bits >> 14) & 0x3FFF) + 1
        return width, height
    raise ValidationError(f"chunk WEBP não suportado: {ctype!r}")


def validate_file(path: Path) -> tuple[int, int]:
    data = path.read_bytes()
    if not data:
        raise ValidationError("arquivo vazio")
    ext = path.suffix.lower()
    if ext == ".png":
        return validate_png(data)
    if ext in {".jpg", ".jpeg"}:
        return validate_jpeg(data)
    if ext == ".gif":
        return validate_gif(data)
    if ext == ".webp":
        return validate_webp(data)
    raise ValidationError(f"formato não suportado: {ext}")


def validate_name(path: Path) -> None:
    name = path.name
    if not NAME_RE.match(name):
        raise ValidationError("nome deve usar minúsculas, números e hífens")
    stem_parts = set(path.stem.split("-"))
    if stem_parts & BANNED_PARTS or VERSION_RE.search(name):
        raise ValidationError("não use final/definitivo/corrigido/vN no nome; use o histórico do Git")


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("assets")
    if not root.exists():
        print(f"ERRO: diretório não encontrado: {root}", file=sys.stderr)
        return 2
    files = sorted(p for p in root.rglob("*") if p.is_file() and p.suffix.lower() in SUPPORTED)
    if not files:
        print(f"ERRO: nenhum asset suportado encontrado em {root}", file=sys.stderr)
        return 2
    failures = 0
    for path in files:
        try:
            validate_name(path)
            width, height = validate_file(path)
            digest = sha256(path)
            print(f"OK  {path}  {width}x{height}  {path.stat().st_size} bytes  sha256={digest}")
        except ValidationError as exc:
            failures += 1
            print(f"FAIL {path}: {exc}", file=sys.stderr)
    if failures:
        print(f"\n{failures} asset(s) inválido(s).", file=sys.stderr)
        return 1
    print(f"\n{len(files)} asset(s) validado(s) com sucesso.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
