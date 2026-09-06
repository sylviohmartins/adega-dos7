# Copilot instructions — ADEGA DOS 7

Este repositório gerencia identidade visual, prompts, agentes, skills, provenance e arquivos gráficos da **ADEGA DOS 7**.

## Fonte de verdade

- `AGENTS.md`: instruções gerais compartilháveis entre agentes.
- `.agents/config.json`: política declarativa de execução, contexto e promoção.
- `.agents/rules/`: regras por categoria de risco.
- `.agents/skills/`: workflows especializados carregados sob demanda.
- `docs/`: design system, construção visual, provenance e referências.

## Comportamento esperado

- Use progressive disclosure; não carregue todas as skills por padrão.
- Para criação/adaptação visual, use `.agents/skills/image-production/SKILL.md`.
- Antes de produzir arte final, construa Design Packet/blueprint e, quando o tema exigir pesquisa, Theme Research Pack.
- Preserve invariantes da marca e escreva **ADEGA DOS 7** sempre em maiúsculas em texto humano.
- Faça auditoria explícita de branding, hierarquia, composição, topologia, tipografia, cor, acessibilidade, anomalias de IA, contexto de uso e produção.
- Para revisão final, use `.agents/skills/design-review/SKILL.md`.
- Imagens raster são binárias; use `.agents/skills/asset-management/SKILL.md` e nunca grave PNG/JPG por APIs de conteúdo UTF-8.
- Para assets externos de agente, use `.agents/skills/agent-asset-vetting/SKILL.md`; não instale por popularidade.
- Trabalhe em branch + PR por padrão e trate CI como feedback de execução.
- Execute `python scripts/validate_repository.py` antes de concluir mudanças de configuração/documentação e `python scripts/validate_assets.py` quando `assets/` mudar.
- Mantenha adaptadores finos; não replique documentação extensa aqui.
