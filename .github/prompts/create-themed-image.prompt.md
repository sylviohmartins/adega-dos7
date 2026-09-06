---
description: Converte um Design Packet aprovado em prompt de produção e processo de criação/edição temática da ADEGA DOS 7.
---

# Produção de imagem temática — do blueprint à arte final

Use este prompt depois de existir um Design Packet aprovado ou suficientemente claro.

## Entrada

- Tema: `${input:theme}`
- Design Packet: `${input:designPacket}`
- Referência principal: `${input:reference}`
- Modo: `${input:mode}`
- Formato final: `${input:format}`
- Texto exato: `${input:exactText}`
- Entregável: `${input:deliverable}`

## Tarefa

Leia `AGENTS.md`, `.agents/skills/image-production/SKILL.md`, `.agents/rules/brand-integrity.md`, `docs/design-system.md`, `docs/image-construction-workflow.md` e `docs/image-generation-prompt.md`.

Converta o Design Packet em um prompt de produção completo e execute a criação/edição quando o ambiente possuir ferramenta de geração de imagem.

## Regras de produção

1. Preserve os invariantes definidos no Design Packet.
2. Respeite a hierarquia visual e o blueprint do canvas.
3. Reproduza exatamente o texto solicitado.
4. Quando o nome completo aparecer em texto humano, use **ADEGA DOS 7**.
5. Respeite quantidades e conexões funcionais dos objetos.
6. Use o tema como camada de direção de arte, não como colagem de enfeites.
7. Não invente símbolos, palavras ou acessórios não solicitados.
8. Evite associações cromáticas/culturais proibidas no briefing.
9. Preserve negative space e safe areas.
10. Para variações de marca: **RECOGNITION FIRST. THEME SECOND.**

## QA obrigatório após a primeira saída

Trate a primeira renderização como rascunho. Antes de considerar a imagem concluída, audite:

- reconhecimento da marca;
- texto e números;
- quantidade de objetos;
- cabos/mangueiras/conexões;
- geometria, perspectiva, reflexos e sombras;
- hierarquia e composição;
- cor e contraste;
- tipografia;
- excesso decorativo;
- legibilidade em thumbnail;
- safe area;
- adequação ao canal;
- anomalias típicas de IA.

Classifique os achados em `BLOCKER`, `MAJOR`, `MINOR` ou `POLISH`.

Se houver blocker, corrija e reavalie. Quando a maior parte estiver correta, prefira edição localizada e conservadora a regenerar toda a composição.

Faça uma segunda passagem deliberada para refinamento de alinhamento, proporção, ruído, contraste e materialidade antes de adicionar novos elementos.

## Saída

Entregue/produza a imagem somente quando os blockers estiverem resolvidos e os critérios do Design Packet estiverem atendidos.
