---
applyTo: "**/*.md"
---

# Instruções para documentação

- Em texto humano, escreva sempre **ADEGA DOS 7** em maiúsculas.
- `AGENTS.md` é a entrada canônica de instruções; não crie fontes concorrentes.
- Prefira links para `.agents/` e `docs/` a duplicar blocos extensos de regras.
- Diferencie fato verificado, decisão de design, inferência e informação desconhecida.
- Não invente claims de marca, endereço, catálogo, contato ou política comercial.
- Ao alterar comportamento de agentes, mantenha `.agents/config.json`, regras, skills, adaptadores e README coerentes.
- Ao alterar uma decisão visual material, atualize o provenance relevante em `docs/assets/`.
- Antes de concluir mudanças documentais, execute `python scripts/validate_repository.py`.
