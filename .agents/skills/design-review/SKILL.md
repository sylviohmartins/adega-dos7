---
name: design-review
description: Faz revisão adversarial de imagens, logos e peças da ADEGA DOS 7 por branding, composição, UX visual, tipografia, cor, acessibilidade, coerência física e anomalias de IA. Use antes de aprovar uma arte ou ao investigar algo visualmente estranho.
---

# Design Review

## Objetivo

Encontrar falhas concretas antes que uma arte seja promovida como oficial.

## Lentes de revisão

1. **Brand integrity** — reconhecimento, invariantes, consistência com referências aprovadas.
2. **Visual hierarchy** — foco P1/P2/P3/P4, leitura, contraste e competição entre elementos.
3. **Composition** — equilíbrio, alinhamento, ritmo, proporção, negative space, bordas e safe areas.
4. **Object topology** — origem/destino de conexões, contagem de objetos funcionais, perspectiva e continuidade.
5. **Typography** — texto exato, legibilidade, espaçamento, arco, kerning aparente e alinhamento.
6. **Color/material** — função da paleta, contraste, associação temática, consistência de luz/reflexos e materialidade.
7. **Accessibility** — legibilidade em tamanho reduzido, contraste funcional e não dependência exclusiva de cor.
8. **AI anomalies** — duplicações, fusões, peças soltas, pseudo-texto, geometria impossível, padrões repetidos sem intenção.
9. **Context of use** — avatar, feed, impressão, fundo, recorte, merchandising.
10. **Production quality** — nitidez, bordas, artefatos, resolução, compressão e exportação.

## Método

- Compare com a referência aprovada lado a lado quando possível.
- Revise primeiro em escala normal, depois em thumbnail.
- Faça uma passada em tons de cinza mental/real para validar hierarquia de valores.
- Faça uma contagem explícita de objetos funcionais quando houver topologia relevante.
- Diferencie `BLOCKER`, `MAJOR`, `MINOR` e `POLISH`.
- Para cada finding, registre evidência, impacto e correção mínima recomendada.

## Saída

A revisão deve terminar com uma decisão:

- `APPROVE`;
- `APPROVE_WITH_MINOR_POLISH`;
- `REVISE`;
- `REJECT_AND_REPLAN`.

Nunca use apenas "ficou estranho" como finding. Descreva exatamente o que está errado e por quê.
