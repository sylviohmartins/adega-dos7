# Execuções ativas

Use este diretório para estado transitório de tarefas longas ou multi-etapas da **ADEGA DOS 7**.

Arquivos devem seguir `.agents/schemas/completion-run.schema.json` e `.agents/specs/completion-contract.md`.

Não use este diretório como histórico permanente de conversas. Ao concluir uma tarefa, preserve apenas decisões duráveis nas fontes adequadas (`docs/`, provenance do asset ou `.agents/memory/`) e trate o run conforme a necessidade de auditoria do projeto.
