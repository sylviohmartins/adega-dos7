# Referências de mercado e decisões de arquitetura

Este repositório usa uma arquitetura de instruções em camadas para reduzir repetição, melhorar portabilidade entre agentes e manter critérios de design verificáveis.

## Agentes, instruções, skills e prompts

### OpenAI / Codex

- Codex e `AGENTS.md`: https://openai.com/index/introducing-codex/
- Loop/instruções do agente Codex: https://openai.com/index/unrolling-the-codex-agent-loop/

Aplicação no repositório:

- `AGENTS.md` contém somente regras persistentes, mapa do repositório e checks obrigatórios;
- detalhes extensos ficam em `docs/` para evitar inflar contexto sempre-on;
- verificações programáticas são tratadas como parte do critério de conclusão.

### GitHub Copilot

- Custom instructions: https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions
- Customization cheat sheet: https://docs.github.com/en/copilot/reference/customization-cheat-sheet
- Prompt files: https://docs.github.com/en/copilot/tutorials/customization-library/prompt-files/your-first-prompt-file
- Custom agents: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-custom-agents
- Agent Skills: https://docs.github.com/en/copilot/concepts/agents/about-agent-skills

Aplicação no repositório:

```text
.github/copilot-instructions.md        contexto persistente do repositório
.github/instructions/*.instructions.md regras por caminho
.github/prompts/*.prompt.md             tarefas reutilizáveis acionadas sob demanda
.github/agents/*.agent.md               especialistas com processo próprio
.github/skills/*/SKILL.md               conhecimento procedural carregado quando relevante
```

### Agent Skills / progressive disclosure

- Anthropic — Agent Skills: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills

Princípio adotado:

- `name` e `description` ajudam o agente a decidir quando a skill é relevante;
- `SKILL.md` contém o procedimento principal;
- documentação complementar fica fora da skill e é carregada somente quando necessária.

Isso reduz contexto duplicado e permite que o mesmo conhecimento procedural seja reutilizado por diferentes tarefas/agentes.

### Claude Code

- Project memory / `CLAUDE.md`: https://docs.anthropic.com/en/docs/claude-code/memory

Aplicação no repositório:

- `CLAUDE.md` é um adaptador curto;
- ele encaminha para `AGENTS.md` e para a documentação canônica;
- regras extensas não são duplicadas no arquivo de memória.

### Gemini CLI

- Context files / `GEMINI.md`: https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/gemini-md.md
- Configuration/context filename support: https://github.com/google-gemini/gemini-cli/blob/main/docs/reference/configuration.md

Aplicação no repositório:

- `GEMINI.md` é um adaptador curto para o mesmo contexto canônico;
- a arquitetura continua utilizável sem obrigar todos os agentes a interpretar uma configuração proprietária específica.

A estratégia completa de portabilidade está em `docs/agent-compatibility.md`.

## Design, UX, UI e acessibilidade

### Hierarquia visual

- Nielsen Norman Group — Visual Hierarchy: https://www.nngroup.com/videos/visual-hierarchy/

Princípio adotado:

- prioridade visual deve ser explícita por tamanho, contraste, posição, proximidade e agrupamento;
- o Design Packet registra P1/P2/P3/P4 antes da geração.

### Cor e tipografia

- Apple Human Interface Guidelines — Color: https://developer.apple.com/design/human-interface-guidelines/color
- Apple Human Interface Guidelines — Typography: https://developer.apple.com/design/human-interface-guidelines/typography

Princípios adotados:

- usar cor com função definida;
- evitar depender somente de cor para comunicar informação;
- preservar contraste e legibilidade;
- minimizar variedade tipográfica;
- usar peso, tamanho e cor para sustentar hierarquia.

### Acessibilidade

- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- Understanding Contrast Minimum: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum

Princípios adotados:

- avaliar contraste em conteúdo funcional;
- não depender exclusivamente de cor;
- evitar imagem de texto quando texto real puder cumprir a função;
- reconhecer que logotipos são um caso especial, mas ainda devem funcionar nos contextos reais de uso.

## Engenharia do processo visual

O fluxo do repositório combina princípios tradicionais de design com controles específicos para geração por IA:

1. briefing;
2. invariantes/variáveis;
3. topologia dos objetos;
4. blueprint/wireframe;
5. hierarquia e valores;
6. cor/material/tipografia;
7. prompt de produção;
8. primeira saída tratada como rascunho;
9. auditoria adversarial de anomalias;
10. edição conservadora;
11. testes de contexto;
12. validação técnica do arquivo;
13. versionamento e validação remota.

A intenção é aproximar o fluxo de IA de um processo profissional de direção de arte: **planejar antes de renderizar, revisar antes de aprovar e validar antes de versionar**.

## Observação sobre fontes externas da marca

Perfis de redes sociais podem exigir autenticação ou bloquear leitura automatizada. Quando uma informação de bio, endereço, catálogo, contato ou posicionamento não puder ser verificada diretamente, ela não deve ser promovida a fato no README. O repositório deve registrar apenas informações confirmadas ou explicitamente fornecidas pelo responsável da marca.
