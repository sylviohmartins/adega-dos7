# Copilot instructions — Adega dos 7

Este repositório gerencia identidade visual, prompts, agentes, skills e arquivos gráficos da **Adega dos 7**.

## Fonte de verdade

- Regras gerais para agentes: `AGENTS.md`.
- Sistema e disciplinas de design: `docs/design-system.md`.
- Processo de construção/blueprint: `docs/image-construction-workflow.md`.
- Manipulação segura de binários: `docs/asset-management.md`.
- Prompt universal: `docs/image-generation-prompt.md`.

## Comportamento esperado

- Para criação ou adaptação visual, não gere a solução final de imediato: construa primeiro o Design Packet/blueprint definido no processo.
- Preserve invariantes da marca e altere apenas variáveis autorizadas pelo briefing.
- Faça auditoria explícita de hierarquia, composição, tipografia, cor, acessibilidade, coerência física, anomalias de IA, small-size legibility e contexto de uso.
- Não aceite texto incorreto, objetos funcionais duplicados, conexões sem origem/destino ou elementos decorativos sem função.
- Imagens raster são binárias; não use APIs ou ações UTF-8 para gravá-las.
- Quando `assets/` mudar, execute `python scripts/validate_assets.py` e valide também o arquivo remoto após o push.
- Mantenha documentação enxuta e sem duplicação; quando uma regra já existir em `docs/`, faça referência a ela.
- Use commits objetivos e sem sufixos de versão nos nomes dos assets.
