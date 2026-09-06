# Pesquisa e avaliação de assets para agentes

Este documento registra referências externas avaliadas para o ecossistema de IA da **ADEGA DOS 7**. Descoberta não implica instalação.

## Critério

A avaliação segue `.agents/rules/agent-asset-supply-chain.md` e `.agents/skills/agent-asset-vetting/SKILL.md`.

## Referências avaliadas

### Anthropic `brand-guidelines`

- Fonte: `anthropics/skills`, `skills/brand-guidelines/SKILL.md`.
- Licença verificada: Apache-2.0.
- Decisão: `ADAPT`.
- Valor: demonstra uma skill pequena e específica para identidade visual, com metadata curta e regras de cor/tipografia.
- Não adotar diretamente: o conteúdo descreve a marca Anthropic e não deve contaminar a identidade da **ADEGA DOS 7**.
- Adaptação local: regras de marca ficam em `.agents/rules/brand-integrity.md`, `docs/design-system.md` e skills locais.

### Anthropic `canvas-design`

- Fonte: `anthropics/skills`, `skills/canvas-design/SKILL.md`.
- Licença verificada no repositório: Apache-2.0.
- Decisão: `ADAPT`.
- Valor: separa intenção estética da execução visual e exige segunda passagem de refinamento.
- Risco/overlap: o fluxo é genérico e privilegia liberdade artística; uma marca existente exige invariantes mais rígidos.
- Adaptação local: `Design Packet -> produção -> primeira saída como rascunho -> revisão adversarial -> edição conservadora -> segunda passagem`.
- Não vendorizar fonts/assets externos sem necessidade e revisão separada.

### GitHub `awesome-copilot`

- Fonte: `github/awesome-copilot`.
- Licença verificada: MIT.
- Decisão: `ADAPT`.
- Valor: catálogo de Agent Skills e exemplos de workflows/agentes, além de padrões de quality playbooks e progressive disclosure.
- Adaptação local: skills pequenas por responsabilidade, estado/evidência para tarefas longas e validações determinísticas.
- Não instalar skills em massa; avaliar individualmente.

### GitHub `create-agentsmd`

- Fonte: catálogo `github/awesome-copilot`.
- Decisão: `SUPERSEDED`.
- Motivo: o repositório já possui `AGENTS.md` específico para **ADEGA DOS 7** e arquitetura de instruções mais completa.

## Configurações oficiais consideradas

### OpenAI / Codex

- `AGENTS.md` hierárquico como instrução compartilhável;
- checks programáticos definidos no repositório devem ser executados quando aplicáveis;
- instruções mais próximas do arquivo têm precedência dentro do escopo.

### GitHub Copilot

- `.github/copilot-instructions.md`: regras always-on específicas do Copilot;
- `.github/instructions/*.instructions.md`: regras por path;
- `.github/prompts/*.prompt.md`: tarefas reutilizáveis;
- `.github/agents/*.agent.md`: especialistas;
- `.agents/skills/*/SKILL.md`: skills de projeto carregadas sob demanda;
- hooks e MCPs só devem ser adicionados quando houver necessidade concreta e após vetting.

### Claude / Agent Skills

- instruções claras, critérios de sucesso e self-correction são preferíveis a prompts vagos;
- subagentes ajudam quando os workstreams são independentes, mas não devem ser usados por padrão;
- skills devem encapsular procedimentos especializados e serem carregadas apenas quando relevantes.

### Gemini CLI

- `GEMINI.md` fornece contexto hierárquico;
- imports `@arquivo` permitem modularização e evitam duplicação;
- extensions podem empacotar prompts/MCPs/comandos, mas não são necessárias enquanto as capacidades locais atenderem o projeto.

## Política de adoção

O padrão para este repositório é **ADAPT antes de ADOPT**. Princípios úteis são reimplementados de forma mínima, auditável e específica para **ADEGA DOS 7**. Assets executáveis ou com acesso a rede/contas externas exigem avaliação de segurança e aprovação humana antes de incorporação.
