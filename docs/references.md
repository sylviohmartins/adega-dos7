# Referências de mercado e decisões de arquitetura

Última revisão: **2026-09-08**.

Este repositório usa arquitetura de instruções em camadas, progressive disclosure e validações determinísticas para que diferentes agentes trabalhem na **ADEGA DOS 7** com o mesmo contrato operacional.

## Referência interna: NEXO FINANCEIRO API

Repositório: `sylviohmartins/nexo-financeiro-api`.

Práticas arquiteturais adaptadas:

- `AGENTS.md` como fonte canônica;
- configuração declarativa em `.agents/config.json`;
- separação entre `rules`, `specs`, `skills`, `memory`, `runs` e `schemas`;
- execução GitHub-mediated com branch/PR/CI;
- progressive context loading;
- completion contract e evidência por requisito;
- vetting de assets externos de agentes;
- distinção entre memória durável e estado transitório.

Não foram copiadas regras do domínio financeiro, Cloudflare, D1, API ou segurança específica do NEXO FINANCEIRO API. O modelo foi traduzido para branding, direção de arte, QA visual, provenance e integridade de assets.

## OpenAI / Codex

- Codex e `AGENTS.md`: https://openai.com/index/introducing-codex/

Princípios aplicados:

- `AGENTS.md` pode existir hierarquicamente e orientar o escopo de arquivos;
- instruções mais próximas têm precedência dentro do escopo;
- checks programáticos definidos nas instruções devem ser executados quando aplicáveis;
- `AGENTS.md` deve manter instruções persistentes e o restante do conhecimento pode ser carregado progressivamente.

## GitHub Copilot

- Repository custom instructions: https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions
- Customization cheat sheet: https://docs.github.com/en/copilot/reference/customization-cheat-sheet
- Agent Skills: https://docs.github.com/en/copilot/concepts/agents/about-agent-skills
- Adding Agent Skills: https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills
- Custom agents: https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-custom-agents
- Awesome Copilot: https://github.com/github/awesome-copilot

Princípios aplicados:

```text
.github/copilot-instructions.md       contexto Copilot always-on
.github/instructions/*.instructions.md regras por path
.github/prompts/*.prompt.md            tarefas reutilizáveis
.github/agents/*.agent.md              especialistas
.agents/skills/*/SKILL.md              workflows portáveis sob demanda
```

O GitHub documenta `.agents/skills`, `.github/skills` e `.claude/skills` como localizações válidas para skills de projeto. A **ADEGA DOS 7** usa `.agents/skills` como raiz canônica para reduzir acoplamento a fornecedor.

## Anthropic / Claude / Agent Skills

- Prompting best practices: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-templates-and-variables
- Anthropic Skills: https://github.com/anthropics/skills
- `brand-guidelines`: https://github.com/anthropics/skills/tree/main/skills/brand-guidelines
- `canvas-design`: https://github.com/anthropics/skills/tree/main/skills/canvas-design

Princípios aplicados:

- instruções claras e critérios de sucesso explícitos;
- investigação antes de afirmações sobre conteúdo não lido;
- self-correction `draft -> review -> refine`;
- subagentes apenas quando o trabalho for independente/isolável;
- skills pequenas, específicas e carregadas quando relevantes;
- separação entre filosofia/direção visual e execução final;
- segunda passagem de refinamento antes de acumular elementos.

Os skills `brand-guidelines` e `canvas-design` foram avaliados como referência arquitetural `ADAPT`, não incorporados diretamente. A licença upstream verificada é Apache-2.0. Veja `docs/agent-assets.md`.

## Gemini CLI

- Context com `GEMINI.md`: https://google-gemini.github.io/gemini-cli/docs/cli/gemini-md.html
- Configuração: https://google-gemini.github.io/gemini-cli/docs/get-started/configuration.html
- Extensions: https://google-gemini.github.io/gemini-cli/docs/extensions/

Princípios aplicados:

- contexto hierárquico;
- imports `@arquivo` para modularizar e evitar drift;
- extensions/MCPs somente quando uma necessidade real justificar a superfície adicional.

## Design, UX, UI e acessibilidade

### Hierarquia visual

- Nielsen Norman Group — Visual Hierarchy: https://www.nngroup.com/videos/visual-hierarchy/

Aplicação: prioridade visual explícita por tamanho, contraste, posição, proximidade e agrupamento; Design Packet registra P1/P2/P3/P4 antes da produção.

### Cor e tipografia

- Apple Human Interface Guidelines — Color: https://developer.apple.com/design/human-interface-guidelines/color
- Apple Human Interface Guidelines — Typography: https://developer.apple.com/design/human-interface-guidelines/typography

Aplicação: cor com função definida, contraste e legibilidade; tipografia sustentando hierarquia com variedade controlada.

### Acessibilidade

- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- Contrast Minimum: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum

Aplicação: avaliar contraste de conteúdo funcional, não depender exclusivamente de cor e testar leitura em contexto real/tamanho reduzido.

## Engenharia do processo visual

Fluxo adotado:

1. descoberta;
2. planejamento;
3. pesquisa temática quando necessária;
4. invariantes/variáveis;
5. topologia dos objetos;
6. Design Packet/blueprint;
7. hierarquia e estudo de valores;
8. cor/material/tipografia;
9. prompt de produção;
10. primeira saída tratada como rascunho;
11. auditoria adversarial;
12. edição conservadora;
13. segunda passagem de refinamento;
14. testes de contexto;
15. validação técnica;
16. provenance;
17. branch/PR/CI;
18. decisão de promoção.

A intenção é aproximar agentes de IA de um processo profissional de design: **planejar antes de renderizar, revisar antes de aprovar, registrar antes de esquecer e validar antes de promover**.

## Fontes externas da marca

Redes sociais podem exigir autenticação ou bloquear leitura automatizada. Informação de bio, endereço, catálogo, contato, política comercial ou posicionamento só deve entrar no repositório como fato quando puder ser verificada ou quando for explicitamente fornecida/aprovada pelo responsável da **ADEGA DOS 7**.

## Pesquisa temática — Carnaval 2027

Consultas realizadas em **2026-09-08** para orientar a variação temática, sem transformar uma referência de mercado em regra de identidade:

- [Confea — Quando a fantasia entra na avenida](https://www.confea.org.br/quando-fantasia-entra-na-avenida-engenharia-sustenta-o-espetaculo): plumas, paetês, pedrarias, tecidos e cores vibrantes como códigos materiais do desfile;
- [Riotur — Com que roupa?](https://riotur.rio/editorial/com-que-roupa/): glitter, pedra, cor, volume, brilho, paetê e acessórios multicoloridos em blocos, bailes e coleções de Carnaval;
- [Gshow — Baile da Vogue 2026](https://gshow.globo.com/carnaval/2026/noticia/baile-da-vogue-veja-os-looks-dos-famosos-para-o-evento.ghtml): fantasias elaboradas, referências à cultura brasileira, personagens e muito brilho;
- [Prefeitura do Rio — Carnaval 2026](https://prefeitura.rio/riotur/carnaval-2026-prefeitura-divulga-o-balanco-do-primeiro-dia-de-desfiles-do-grupo-especial/): fantasias e adereços detalhados, cores vibrantes, luz e caráter plural do Carnaval de rua e dos desfiles.

Decisão aplicada: reconstruir o miolo com plumas, paetês, máscara, serpentinas e confetes em magenta, coral, turquesa, violeta e laranja, usando carvão como contraste. Dourado ficou apenas como reflexo/acento; não foi herdada a paleta dominante do Natal ou do Ano Novo. A pesquisa informa códigos visuais e riscos de associação, mas o master `assets/logos/original.png` continua sendo a única fonte de identidade estrutural.
