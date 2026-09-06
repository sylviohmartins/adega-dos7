# Contrato de conclusão

Use este contrato em tarefas longas, multi-requisito, multiagente ou sujeitas a perda de contexto.

## Estado por requisito

Cada requisito deve ter um dos estados:

- `PENDING` — ainda não iniciado;
- `IN_PROGRESS` — há trabalho em curso;
- `BLOCKED` — existe impedimento concreto registrado;
- `DONE` — há evidência verificável de atendimento;
- `NOT_APPLICABLE` — requisito explicitamente fora do escopo com justificativa.

## Evidência de `DONE`

Um requisito só pode ser `DONE` quando houver evidência concreta, por exemplo:

- arquivo/path criado ou alterado;
- resultado de check;
- comparação visual documentada;
- hash/dimensões de asset;
- link para fonte ou decisão de design;
- PR/review concluído;
- validação remota do arquivo.

## Checkpoint de tarefa

Para trabalhos prolongados, registre em `.agents/runs/<task-id>.json`:

- objetivo;
- requisitos;
- estado de cada requisito;
- decisões e suposições;
- arquivos afetados;
- evidências;
- último checkpoint;
- próximos passos;
- riscos/bloqueios.

## Gate final

Antes de declarar conclusão:

1. nenhum requisito material pode permanecer `PENDING` ou `IN_PROGRESS`;
2. `BLOCKED` deve conter motivo e impacto claros;
3. todos os checks obrigatórios devem ter evidência ou limitação explícita;
4. impactos de marca/design e integridade de assets devem estar registrados;
5. a decisão de promoção deve respeitar `.agents/rules/change-promotion.md`.

Uma síntese de conversa não substitui o estado estruturado da tarefa.
