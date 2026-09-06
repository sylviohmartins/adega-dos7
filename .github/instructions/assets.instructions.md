---
applyTo: "assets/**/*"
---

# Instruções para assets visuais

- Trate PNG, JPG, JPEG, WEBP e GIF como arquivos binários reais.
- Nunca grave imagens por uma operação descrita como criação/edição de conteúdo UTF-8.
- Preserve o arquivo fonte sem redimensionar, recomprimir ou alterar perfil de cor, salvo requisito explícito.
- Antes do commit, valide formato, dimensões, tamanho, decodificação e SHA-256 quando possível.
- Depois do push, confirme caminho remoto, tamanho coerente e preview/download completo.
- Execute `python scripts/validate_assets.py` após qualquer alteração em `assets/`.
- Para logos sazonais, use `<tema>-<ano>.<extensão>` em minúsculas e sem sufixos como `final`, `v2` ou `definitivo`.
- Não substitua o master por uma versão otimizada para redes sociais; derivados devem ser separados quando necessários.
