# Compatibilidade entre agentes

O repositório usa **uma fonte canônica + adaptadores finos**, em vez de duplicar o mesmo conjunto de regras para cada fornecedor.

## Fonte canônica

```text
AGENTS.md
  └── docs/
      ├── design-system.md
      ├── image-construction-workflow.md
      ├── image-generation-prompt.md
      ├── asset-management.md
      └── references.md
```

`AGENTS.md` contém regras persistentes e links. A documentação detalhada é carregada conforme a tarefa.

## OpenAI / Codex

Arquivo principal:

```text
AGENTS.md
```

Codex reconhece instruções `AGENTS.md` hierarquicamente e deve executar checks programáticos definidos nelas quando aplicáveis.

## GitHub Copilot

Adaptadores:

```text
.github/copilot-instructions.md
.github/instructions/*.instructions.md
.github/prompts/*.prompt.md
.github/agents/*.agent.md
.github/skills/*/SKILL.md
```

Separação usada:

- **custom instructions**: contexto always-on;
- **path instructions**: regras por escopo;
- **prompt files**: tarefas reutilizáveis;
- **custom agents**: especialistas;
- **skills**: workflows procedurais carregados sob demanda.

## Claude Code

Adaptador:

```text
CLAUDE.md
```

Ele é propositalmente curto e encaminha para `AGENTS.md`/`docs/`, reduzindo divergência entre instruções.

## Gemini CLI

Adaptador:

```text
GEMINI.md
```

Também funciona como shim para o contexto canônico. Gemini CLI permite configurar nomes alternativos de arquivos de contexto, mas manter `GEMINI.md` facilita uso sem configuração adicional.

## Agent Skills

A skill principal está em:

```text
.github/skills/image-production/SKILL.md
```

O formato `SKILL.md` usa metadata curta (`name` e `description`) e conteúdo procedural mais detalhado, seguindo a ideia de progressive disclosure: o agente identifica a skill com pouco contexto e só carrega o procedimento completo quando necessário.

## Regra contra duplicação

Quando uma regra evoluir:

1. atualize primeiro a fonte canônica (`AGENTS.md` ou `docs/`);
2. altere os adaptadores apenas se o caminho/ponte precisar mudar;
3. não copie blocos extensos para `CLAUDE.md`, `GEMINI.md` e `copilot-instructions.md`;
4. valide se todos os links continuam corretos.

Essa arquitetura reduz drift entre ferramentas e mantém o conhecimento do projeto utilizável mesmo quando o agente/modelo muda.
