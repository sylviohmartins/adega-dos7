---
name: planning
description: Converte pedidos ambíguos ou multi-requisito da ADEGA DOS 7 em plano verificável, com critérios de sucesso, invariantes, riscos, evidências e gates. Use antes de mudanças complexas, visuais ou de arquitetura de agentes.
---

# Planning

## Objetivo

Definir sucesso antes de produzir ou editar.

## Plano mínimo

Registre:

1. objetivo observável;
2. contexto e uso final;
3. requisitos obrigatórios;
4. invariantes da marca;
5. variáveis autorizadas;
6. fora de escopo;
7. riscos e associações indesejadas;
8. arquivos/áreas afetados;
9. validações determinísticas;
10. validações humanas/visuais;
11. rollback;
12. gate de promoção.

## Para imagens

Inclua obrigatoriamente um Design Packet antes do prompt de produção, conforme `docs/image-construction-workflow.md`.

## Para tarefas longas

Crie um run em `.agents/runs/<task-id>.json` conforme `.agents/specs/completion-contract.md`.

## Regra

Critérios materiais devem virar verificações concretas. Não considere um requisito atendido apenas porque ele apareceu no planejamento.
