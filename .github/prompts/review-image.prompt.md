---
description: Executa revisão adversarial de uma imagem da ADEGA DOS 7 antes da aprovação, priorizando identidade, coerência estrutural, legibilidade e produção.
---

# Revisão crítica de imagem

Use este prompt para revisar qualquer imagem criada para a **ADEGA DOS 7** antes de aprová-la.

## Entrada

- Imagem: `${input:image}`
- Briefing/Design Packet: `${input:designPacket}`
- Uso principal: `${input:usage}`

## Tarefa

Leia `AGENTS.md`, `.agents/skills/design-review/SKILL.md`, `.agents/rules/brand-integrity.md`, `docs/design-system.md` e `docs/image-construction-workflow.md`.

Compare a imagem com o briefing e faça auditoria adversarial: procure ativamente erros, não apenas qualidades.

Avalie:

1. reconhecimento da marca;
2. hierarquia visual;
3. composição e equilíbrio;
4. texto e tipografia;
5. cor, contraste e associações indesejadas;
6. coerência física/semântica dos objetos;
7. quantidade e continuidade de cabos/mangueiras/conexões;
8. perspectiva, sombras, reflexos e materiais;
9. excesso de ornamentos/ruído;
10. anomalias típicas de geração por IA;
11. legibilidade em thumbnail;
12. safe area para o canal;
13. acessibilidade aplicável;
14. produção/exportação.

Classifique cada achado como `BLOCKER`, `MAJOR`, `MINOR` ou `POLISH`.

Para cada problema, indique:

- onde está;
- por que é um problema;
- qual é a correção mínima recomendada;
- o que deve ser preservado ao corrigir.

Ao final, dê um veredito: `APPROVE`, `APPROVE_WITH_MINOR_POLISH`, `REVISE` ou `REJECT_AND_REPLAN`, com justificativa objetiva.
