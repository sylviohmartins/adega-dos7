# Compatibilidade entre agentes

O repositório da **ADEGA DOS 7** usa **uma fonte canônica + adaptadores finos + skills portáveis**, evitando duplicar regras para cada fornecedor.

## Camadas

```text
AGENTS.md                         instruções compartilháveis e always-on
└── .agents/
    ├── config.json               política declarativa
    ├── rules/                    regras por risco
    ├── specs/                    execução e conclusão
    ├── skills/                   procedimentos sob demanda
    ├── memory/                   conhecimento durável
    ├── runs/                     estado transitório
    └── schemas/                  contratos estruturados

.github/                          integrações específicas do GitHub/Copilot
CLAUDE.md                         adaptador Claude Code
GEMINI.md                         adaptador Gemini CLI
docs/                             conhecimento detalhado e provenance
```

## OpenAI / Codex

Entrada principal:

```text
AGENTS.md
```

`AGENTS.md` é hierárquico: instruções mais próximas do arquivo têm precedência dentro do escopo. Checks programáticos descritos nas instruções devem ser executados quando aplicáveis.

O modelo de execução local está em `.agents/specs/execution-model.md` e foi inspirado no fluxo GitHub-mediated do `nexo-financeiro-api`, adaptado para governança de marca e produção visual.

## GitHub Copilot

Configurações usadas:

```text
.github/copilot-instructions.md
.github/instructions/*.instructions.md
.github/prompts/*.prompt.md
.github/agents/*.agent.md
.agents/skills/*/SKILL.md
```

Separação:

- `copilot-instructions.md`: contexto curto e always-on específico do Copilot;
- path instructions: regras automáticas para arquivos/paths específicos;
- prompt files: tarefas reutilizáveis acionadas pelo usuário;
- custom agents: especialistas com função e processo próprios;
- Agent Skills: workflows procedurais carregados quando relevantes.

O GitHub documenta `.agents/skills` como localização válida para skills de projeto; por isso ela é a raiz canônica usada aqui, reduzindo acoplamento a uma única ferramenta.

## Claude Code

Adaptador:

```text
CLAUDE.md
```

Ele importa/aponta para `AGENTS.md` e mantém o contexto permanente curto. As skills locais continuam em `.agents/skills`; quando a ferramenta não fizer descoberta automática desse path, `AGENTS.md` roteia explicitamente para a skill adequada.

A orientação do projeto favorece instruções claras, critérios de sucesso, investigação antes de afirmar fatos e self-correction `draft -> review -> refine`.

## Gemini CLI

Adaptador:

```text
GEMINI.md
```

Gemini CLI suporta contexto hierárquico em `GEMINI.md` e imports `@arquivo`. O arquivo raiz importa `AGENTS.md`, evitando duplicação. Extensões Gemini podem empacotar prompts, MCPs e comandos, mas não são adicionadas enquanto capacidades locais forem suficientes.

## Agent Skills

Raiz canônica:

```text
.agents/skills/<skill-name>/SKILL.md
```

Cada skill usa frontmatter mínimo `name` + `description` e corpo procedural. Esse desenho segue progressive disclosure: o agente decide relevância pela metadata e só carrega as instruções completas quando necessário.

Skills atuais:

- `repository-discovery`;
- `planning`;
- `task-completion`;
- `image-production`;
- `design-review`;
- `asset-management`;
- `agent-asset-vetting`;
- `documentation`.

## Custom agents da ADEGA DOS 7

```text
.github/agents/art-director.agent.md
.github/agents/brand-guardian.agent.md
.github/agents/design-qa.agent.md
.github/agents/visual-researcher.agent.md
```

- **Art Director**: orquestra briefing, blueprint, produção e refinamento.
- **Brand Guardian**: protege invariantes, nomenclatura e factualidade.
- **Design QA**: revisão visual/técnica adversarial.
- **Visual Researcher**: pesquisa temática, códigos visuais e riscos de associação.

## MCPs, hooks, plugins e extensões

Não são adicionados por padrão. Use `.agents/skills/agent-asset-vetting/SKILL.md` antes de incorporar qualquer capacidade externa. A regra é necessidade comprovada + menor privilégio + licença + revisão estática + benchmark.

## Regra contra drift

Quando uma regra evoluir:

1. atualize `AGENTS.md`, `.agents/` ou `docs/` conforme a natureza da regra;
2. altere adaptadores apenas quando a ponte precisar mudar;
3. não copie blocos extensos para vários fornecedores;
4. execute `python scripts/validate_repository.py`;
5. valide os links e paths no PR.
