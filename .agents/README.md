# Ecossistema de agentes — ADEGA DOS 7

Este diretório concentra a arquitetura canônica de operação de agentes de IA do repositório.

## Princípio

A identidade visual da **ADEGA DOS 7** é um ativo de marca. Agentes devem trabalhar com o mesmo rigor de um fluxo profissional de design: descobrir contexto, planejar, produzir, revisar, validar, registrar evidências e somente então promover a mudança.

## Estrutura

```text
.agents/
├── config.json
├── rules/
├── specs/
├── skills/
├── memory/
├── runs/
└── schemas/
```

- `config.json`: política declarativa de execução, contexto, promoção e segurança.
- `rules/`: regras persistentes que se aplicam por categoria de risco.
- `specs/`: contratos de processo e conclusão.
- `skills/`: procedimentos especializados carregados sob demanda.
- `memory/`: conhecimento durável, verificado e com provenance; nunca transcrições de conversa.
- `runs/`: estado transitório de tarefas longas ou multi-etapas.
- `schemas/`: formatos estruturados para configuração, avaliações e evidências.

## Fonte canônica

`AGENTS.md` continua sendo a entrada principal e compartilhável entre ferramentas. Este diretório detalha o processo sem inflar o contexto always-on.

Adaptadores como `CLAUDE.md`, `GEMINI.md` e `.github/copilot-instructions.md` devem apontar para a fonte canônica e não competir com ela.

## Progressive disclosure

Carregue apenas o necessário para a tarefa. Regras simples e universais ficam em `AGENTS.md`; procedimentos especializados ficam em `skills/`; referências extensas ficam em `docs/`.

## Terceiros

Skills, MCPs, plugins, hooks, agentes e prompts externos devem passar pelo fluxo de avaliação em `.agents/rules/agent-asset-supply-chain.md` antes de serem incorporados. Popularidade não é autorização.
