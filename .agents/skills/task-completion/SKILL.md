---
name: task-completion
description: Mantém requisitos, evidências, checkpoints e critérios de conclusão de tarefas longas ou multi-etapas da ADEGA DOS 7. Use quando a tarefa pode atravessar várias sessões, agentes, branches ou ciclos de correção.
---

# Task Completion

## Fonte

Siga `../../specs/completion-contract.md`.

## Quando usar

- múltiplos requisitos independentes;
- geração visual com várias rodadas;
- migração de arquitetura de agentes;
- tarefa que pode sofrer compactação/perda de contexto;
- trabalho dividido entre agentes/subagentes.

## Procedimento

1. crie `.agents/runs/<task-id>.json` conforme o schema;
2. registre todos os requisitos antes de marcar progresso;
3. associe evidência concreta a cada requisito `DONE`;
4. atualize checkpoint após mudanças materiais;
5. não use a conversa como estado autoritativo;
6. antes da conclusão, aplique o gate final do completion contract;
7. arquive ou remova estado transitório conforme a política do projeto quando a tarefa terminar.

Use `READY_FOR_HUMAN_REVIEW` quando a execução automatizada e os checks estiverem concluídos, mas uma aprovação humana exigida ainda não tiver sido registrada. Depois de uma decisão humana verificável, promova o estado para `DONE`.

## Regra

`DONE` sem evidência verificável é `IN_PROGRESS`.
