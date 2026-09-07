---
description: Constrói o Design Packet/blueprint da ADEGA DOS 7 antes da produção de uma nova arte ou adaptação temática.
---

# Design Blueprint — criar a planta visual antes da arte

Use este prompt para transformar qualquer briefing visual em um **Design Packet** antes da geração final.

## Entrada

- Tema: `${input:theme}`
- Tipo de peça: `${input:pieceType}`
- Objetivo: `${input:objective}`
- Canal/uso: `${input:channel}`
- Referência principal: `${input:reference}`
- Texto exato: `${input:exactText}`
- Restrições adicionais: `${input:constraints}`

## Tarefa

Leia `AGENTS.md`, `.agents/rules/brand-integrity.md`, `.agents/skills/image-production/SKILL.md`, `docs/design-system.md` e `docs/image-construction-workflow.md`.

Não gere ainda a arte final.

Construa um **Design Packet** que permita a outro designer/agente entender exatamente como a imagem deve ser montada.

Entregue:

1. objetivo em uma frase;
2. percepção desejada;
3. invariantes da identidade;
4. variáveis controladas pelo tema;
5. hierarquia visual P1/P2/P3/P4;
6. mapa de objetos e conexões funcionais;
7. blueprint ASCII do canvas com zonas, safe areas, centro óptico e fluxo de leitura;
8. proporções relativas aproximadas;
9. estudo de valores claro/escuro;
10. paleta com função de cada cor;
11. materiais e acabamentos;
12. tipografia/texto exato;
13. negative space e áreas onde não inserir ornamentos;
14. associações visuais indesejadas;
15. elementos proibidos;
16. bloqueadores de aprovação;
17. testes de thumbnail, avatar/feed/story e impressão quando aplicável;
18. mapa de transformação interna `PRESERVAR / LIMPAR / RECONSTRUIR / LIMITE`;
19. quantidade, raio e posição relativa dos arcos estruturais a preservar;
20. recomendação de estratégia: geração do zero ou edição conservadora.

## Regras

- Não invente elementos de marca ausentes das referências.
- Para a **ADEGA DOS 7**, trate `assets/logos/original.png` como o master canônico. Descreva `assets/logos/natal-2026.png` e outras peças sazonais como derivados temáticos, nunca como origem da identidade.
- Para uma peça de marca, escreva **ADEGA DOS 7** sempre em maiúsculas quando o nome completo aparecer em texto humano.
- Não trate tema como mera coleção de enfeites; traduza-o por cor, luz, material, textura, atmosfera e ornamentos controlados.
- Não trate cada detalhe interno do master como imutável. Separe o arcabouço estrutural do resíduo decorativo que deve ser limpo/reconstruído.
- Em logos sazonais, preserve somente o contorno, lettering, garrafa/7, narguilé/rosh, fumaça característica, topologia funcional e os arcos estruturais existentes; não adicione arcos novos.
- Faça a direção de cor e materialidade nascer da pesquisa do tema atual, sem herdar automaticamente a paleta ou os objetos de outra variação.
- Mantenha a transformação temática dentro do emblema e declare qualquer exceção.
- Modele explicitamente quantidades e conexões de objetos funcionais.
- Identifique riscos de anomalias de IA antes da produção.
- Para variações da marca: **RECOGNITION FIRST. THEME SECOND.**

Ao final, forneça uma seção **READY FOR PRODUCTION** resumindo tudo que o prompt final precisará conter.
