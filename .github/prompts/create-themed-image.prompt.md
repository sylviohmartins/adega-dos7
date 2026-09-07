---
description: Converte um Design Packet aprovado em prompt de produção e processo de criação/edição temática da ADEGA DOS 7.
---

# Produção de imagem temática — do blueprint à arte final

Use este prompt depois de existir um Design Packet aprovado ou suficientemente claro.

## Entrada

- Tema: `${input:theme}`
- Design Packet: `${input:designPacket}`
- Referência principal: `${input:reference}`
- Theme Research Pack: `${input:themeResearch}`
- Contrato `PRESERVAR / LIMPAR / RECONSTRUIR / LIMITE`: `${input:transformationContract}`
- Variações existentes que não devem ser copiadas: `${input:existingVariants}`
- Modo: `${input:mode}`
- Formato final: `${input:format}`
- Texto exato: `${input:exactText}`
- Entregável: `${input:deliverable}`

## Tarefa

Leia `AGENTS.md`, `.agents/skills/image-production/SKILL.md`, `.agents/rules/brand-integrity.md`, `docs/design-system.md`, `docs/image-construction-workflow.md` e `docs/image-generation-prompt.md`.

Converta o Design Packet em um prompt de produção completo e execute a criação/edição quando o ambiente possuir ferramenta de geração de imagem.

## Regras de produção

1. Preserve os invariantes definidos no Design Packet.
2. Para a **ADEGA DOS 7**, use `assets/logos/original.png` como matriz canônica; a arte temática é uma derivação, não uma nova origem de identidade.
3. Respeite a hierarquia visual e o blueprint do canvas.
4. Reproduza exatamente o texto solicitado.
5. Quando o nome completo aparecer em texto humano, use **ADEGA DOS 7**.
6. Respeite quantidades e conexões funcionais dos objetos.
7. Use o tema como camada de direção de arte, não como colagem de enfeites.
8. Não invente símbolos, palavras ou acessórios não solicitados.
9. Evite associações cromáticas/culturais proibidas no briefing.
10. Preserve negative space e safe areas.
11. Para um logo sazonal da **ADEGA DOS 7**, use `assets/logos/original.png` como referência estrutural e preserve apenas o contrato explícito: contorno, lettering, garrafa/7, narguilé/rosh, fumaça característica, topologia funcional e os arcos existentes na mesma quantidade, raio e posição relativa.
12. Limpe tracinhos laterais, raios, barras, ornamentos de rótulo e preenchimentos internos herdados quando não forem parte do arcabouço; reconstrua o miolo com elementos próprios do tema.
13. Mantenha a transformação dentro do emblema. Não adicione decoração no canvas externo, nem crie arcos novos, salvo autorização explícita.
14. Baseie cores, materiais e símbolos do tema atual em pesquisa própria; não copie automaticamente Natal, Ano Novo ou outra variação.
15. Para variações de marca: **RECOGNITION FIRST. THEME SECOND.**

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
- contagem, raio e posição dos arcos estruturais;
- resíduos internos antigos que deveriam ter sido limpos/reconstruídos;
- leitura imediata do tema sem depender de texto explicativo;
- diferenciação em relação às outras variações sazonais;
- ausência de decoração fora do emblema;
- legibilidade em thumbnail;
- safe area;
- adequação ao canal;
- anomalias típicas de IA.

Classifique os achados em `BLOCKER`, `MAJOR`, `MINOR` ou `POLISH`.

Se houver blocker, corrija e reavalie. Quando a maior parte estiver correta, prefira edição localizada e conservadora a regenerar toda a composição.

Faça uma segunda passagem deliberada para refinamento de alinhamento, proporção, ruído, contraste e materialidade antes de adicionar novos elementos.

## Saída

Entregue/produza a imagem somente quando os blockers estiverem resolvidos e os critérios do Design Packet estiverem atendidos.
