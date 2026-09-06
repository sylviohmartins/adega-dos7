---
name: asset-management
description: Gerencia com segurança arquivos visuais binários da ADEGA DOS 7, incluindo nomenclatura, validação, hash, upload, substituição, integridade remota e rollback. Use sempre que PNG, JPG, WEBP, GIF, PDF visual ou outro asset binário for criado, movido ou substituído.
---

# Asset Management

## Fonte principal

Leia `../../../docs/asset-management.md`.

## Regras obrigatórias

1. Confirme o arquivo fonte real antes de qualquer upload.
2. PNG/JPG/WEBP/GIF são binários; não use ações documentadas como UTF-8/texto para gravá-los.
3. Preserve bytes do master quando a tarefa for apenas versionamento/upload.
4. Valide formato real, dimensões, tamanho, decodificação completa e SHA-256.
5. Use convenção de nome definida no repositório; revisões pertencem ao Git, não ao filename.
6. Depois do push, valide path, tamanho, blob remoto e preview/download quando possível.
7. Compare hash fonte/destino quando o objetivo for cópia byte a byte.
8. Se a ferramenta não suporta upload binário real, não improvise conversão textual; use um fluxo suportado ou documente a limitação.

## Antes do commit

```bash
python scripts/validate_assets.py
```

## Depois do push

Confirme que o arquivo remoto existe, possui tamanho plausível e não está truncado. Um commit criado não é evidência suficiente de integridade.

## Rollback

Para substituições, identifique o commit/blob anterior antes da promoção para permitir restauração rápida.
