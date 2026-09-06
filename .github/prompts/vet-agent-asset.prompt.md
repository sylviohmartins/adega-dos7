---
description: Avalia uma skill, plugin, MCP, hook, prompt, extensão ou agente externo antes de incorporá-lo ao ecossistema da ADEGA DOS 7.
---

Avalie o candidato `${input:source}` para uso no repositório da **ADEGA DOS 7**.

Siga `.agents/skills/agent-asset-vetting/SKILL.md` e `.agents/rules/agent-asset-supply-chain.md`.

Investigue:

- origem/mantenedor;
- licença;
- maturidade/manutenção;
- permissões e superfície de ataque;
- scripts de instalação/downloads;
- prompt injection/exfiltração;
- dependências;
- overlap com capacidades locais;
- valor incremental para design, branding, pesquisa visual, QA ou gestão de assets;
- possibilidade de `ADAPT` em vez de copiar/instalar.

Entregue uma avaliação compatível com `.agents/schemas/agent-asset-assessment.schema.json` e decisão `ADOPT`, `ADAPT`, `TRIAL`, `REJECT` ou `SUPERSEDED`.

Não instale nem vendorize o candidato sem aprovação humana explícita.
