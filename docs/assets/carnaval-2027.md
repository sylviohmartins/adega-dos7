# Logo Carnaval 2027 — Design Packet e provenance

## Identificação

```text
arquivo: assets/logos/carnaval-2027.png
tema: Carnaval 2027
origem estrutural: assets/logos/original.png
referência de tratamento: assets/logos/natal-2026.png
referência de contraste: assets/logos/ano-novo-2027.png
formato: PNG
modo: 8-bit sRGB Palette, 256 cores
canvas: 1254 × 1254 px
tamanho: 516.185 bytes
SHA-256: 7807e9f8a153c69f130c7eba005ae185ba74d50ec6f983fac0e8034db36b5698
git blob SHA-1: feb3b02d76b26cf04985f99e5acb715cb2a257b7
última validação local: 2026-09-08
```

## Objetivo

Criar uma edição de Carnaval do emblema da **ADEGA DOS 7** que pareça uma reformulação temática interna autêntica, mantendo a marca reconhecível e sem ornamentação fora do contorno.

## Percepção desejada

> “É a **ADEGA DOS 7** em uma edição especial de Carnaval brasileiro: vibrante, exuberante, premium e imediatamente festiva.”

## Referências

- matriz canônica de identidade: `assets/logos/original.png`;
- referência de tratamento: `assets/logos/natal-2026.png`, usada somente para o grau de reconstrução do miolo e para a contenção do tema dentro do emblema;
- referência de contraste: `assets/logos/ano-novo-2027.png`, usada para evitar a repetição de fogos, preto/dourado, azul frio e linguagem de Réveillon;
- referências externas e decisões: [`docs/references.md`](../references.md).

## Theme Research Pack e advogado do diabo

Pesquisa realizada em **2026-09-08**:

- [Confea — Quando a fantasia entra na avenida](https://www.confea.org.br/quando-fantasia-entra-na-avenida-engenharia-sustenta-o-espetaculo) descreve plumas, paetês, pedrarias, tecidos e cores vibrantes como parte do impacto visual e material das fantasias;
- [Riotur — Com que roupa?](https://riotur.rio/editorial/com-que-roupa/) destaca glitter, pedra, cor, volume, brilho, paetês e acessórios multicoloridos em blocos, bailes e coleções;
- [Gshow — Baile da Vogue 2026](https://gshow.globo.com/carnaval/2026/noticia/baile-da-vogue-veja-os-looks-dos-famosos-para-o-evento.ghtml) registra fantasias elaboradas, referências à cultura brasileira, personagens e muito brilho;
- [Prefeitura do Rio — Carnaval 2026](https://prefeitura.rio/riotur/carnaval-2026-prefeitura-divulga-o-balanco-do-primeiro-dia-de-desfiles-do-grupo-especial/) mostra a associação entre fantasias/adereços detalhados, cores vibrantes, luz e pluralidade.

Conclusão: Carnaval não é comunicado apenas por “colocar confete”. O conjunto de materiais — plumas, paetês, pedrarias, brilho, volume, máscara e fitas — é mais autêntico do que uma paleta isolada. Ao mesmo tempo, usar todos os códigos com a mesma intensidade gera ruído e pode sugerir um bloco ou uma escola específica. A direção escolhida concentra esses materiais em uma fan interna atrás dos objetos, usa carvão para organizar o contraste e mantém as áreas de leitura mais limpas. Não usa bandeiras, brasões, cores de escola, futebol ou associação institucional específica.

## Contrato de transformação interna

### PRESERVAR

- contorno circular externo e campo externo preto;
- texto exato `ADEGA DOS` no arco superior e número `7` no rótulo;
- silhueta, escala relativa e posição geral da garrafa central;
- narguilé/rosh à esquerda;
- fumaça característica do rosh: wisp compacto, translúcido, em curva suave, com a mesma origem e peso visual do master;
- topologia: exatamente uma saída visível, uma mangueira contínua e uma única piteira final;
- arcos estruturais existentes, com a mesma contagem, raios e posições relativas do master; nenhum arco novo foi usado como ornamento.

### LIMPAR

- tracinhos laterais do master;
- raios radiais e barras paralelas genéricas;
- preenchimento ornamental legado do rótulo que não define o `7`;
- qualquer decoração natalina ou de Ano Novo herdada por proximidade visual.

### RECONSTRUIR

- todo o campo interno com fan de plumas, paetês, pedrarias, máscara, serpentinas e confetes;
- rótulo da garrafa como medalhão carnavalesco em torno do `7`, sem texto adicional;
- materiais e cor do interior em carvão, magenta/fúcsia, coral/vermelho, laranja, turquesa e violeta;
- brilho e textura de tecido, lantejoula e metal para dar sensação de fantasia real, não de overlay digital;
- reflexos do vidro e do líquido da garrafa, preservando a função e a leitura do objeto;
- fumaça do rosh somente como correção conservadora para manter a assinatura original, sem convertê-la em serpentina.

### LIMITE

- tudo que for temático permanece estritamente dentro do anel externo;
- o canvas ao redor fica preto, limpo e sem confetes, penas, serpentinas, halos ou texto;
- nenhum slogan, ano, faixa, placa ou palavra nova;
- nenhum arco, anel, rosh, mangueira ou piteira adicionais;
- não copiar a paleta, fogos, fumaça ou composição de `ano-novo-2027.png`.

## Invariantes, hierarquia e topologia

- P1: garrafa central e `7`; P2: assinatura `ADEGA DOS`; P3: narguilé, mangueira, rosh, fumaça e piteira; P4: plumas, máscara, paetês, serpentinas e confetes;
- emblema circular 1:1 e arcabouço sem arco decorativo novo;
- o centro óptico permanece na garrafa/`7`, e os elementos carnavalescos são uma camada interna atrás dos objetos;
- `NARGUILÉ → 1 saída → 1 mangueira contínua → 1 piteira final`;
- `GARRAFA → rótulo carnavalesco → número 7`.

## Blueprint e safe areas

```text
┌────────────────────────────────┐
│      canvas externo preto       │
│       ADEGA DOS [P2]           │
│  plumas/paetês dentro do anel  │
│                                │
│  narguilé [P3]  garrafa/7 [P1] │
│       fumaça      máscara      │
│        ╲                       │
│         ╰─ 1 mangueira ──►    │
│ confetes/serpentinas [P4]      │
└────────────────────────────────┘
```

Preservar respiro no lettering, no `7`, no vidro frontal, na saída do rosh, na fumaça, no trajeto da mangueira e na piteira. A margem externa fica livre para recorte circular e avatar.

## Estudo de valores, paleta e materiais

- canvas externo: preto sólido; base interna: carvão quase preto;
- identidade: ivory/creme e metal claro para lettering, contorno e highlights;
- foco: vidro e líquido âmbar/laranja com reflexos claros;
- tema: plumas e paetês saturados, com brilhos pequenos e controlados.

| Função | Cor/material | Uso |
| --- | --- | --- |
| Base | preto externo + carvão interno | contraste e distinção do Ano Novo |
| Identidade | ivory/creme | lettering, contorno e leitura |
| Carnaval 1 | magenta/fúcsia | plumas, máscara, paetês e fitas |
| Carnaval 2 | coral/vermelho e tangerina | plumas, reflexos e calor |
| Carnaval 3 | turquesa/teal e violeta | contraste e iridescência |
| Material | paetê, pedraria, cetim/lamê, pena e contas | códigos físicos de fantasia |
| Acento restrito | ouro/champagne | poucos brilhos, contas e reflexos; nunca dominante |

## Tipografia e regras negativas

- texto incorporado: somente `ADEGA DOS` e o número `7`; não gerar `Carnaval 2027`, slogan, nome de bloco, escola ou texto secundário;
- não usar azul dominante, branco/azul futurista, neon ou preto/dourado como sistema principal;
- não usar árvore, neve, azevinho, laços natalinos, fogos, relógio, champanhe de Ano Novo ou contagem regressiva;
- não colocar elementos fora do emblema;
- não adicionar arcos, anéis, raios, barras, side dashes ou ornamentos lineares genéricos;
- não duplicar mangueira, piteira, rosh ou fumaça;
- não transformar a fumaça em serpentina;
- não usar bandeiras, brasões, cores de escola de samba, clubes, futebol ou mascotes;
- não deixar a imagem parecer apenas o master com adesivos decorativos.

## Prompt de produção usado

```text
Create a production-quality 1:1 seasonal brand emblem: an authentic Brazilian Carnival edition of the ADEGA DOS 7 logo.

Use original.png as the only canonical identity source. Preserve its outer circular emblem, exact “ADEGA DOS” lettering and “7”, central bottle, hookah/narguile, rosh, original characteristic rosh smoke plume, one outlet → one continuous hose → one mouthpiece, and the structural circular arcs. Keep the same count, radii, relative positions and visual weight of the original structural arcs. Do not delete an existing structural arc and do not add a new circular arc.

Use natal-2026.png only to understand the degree of internal thematic reconstruction and containment. Do not copy Christmas objects, ribbons, holly, palette or ornament placement. Use ano-novo-2027.png only as contrast. Do not copy its fireworks, smoke, confetti layout, black-and-gold palette, blue/white mood or futuristic feeling.

Rebuild the entire non-essential interior so the first impression is unmistakably Brazilian Carnival, not a generic holiday logo and not stickers over the master. Remove generic orange filler, side dashes, radial spokes, parallel bars and legacy label ornament that are not part of the identity skeleton. Inside the emblem, create a premium samba/carnival atmosphere with a controlled fan of iridescent feathers behind the bottle and rosh, tactile sequins and jewel-like highlights, satin streamers, metallic confetti, beads and a restrained masquerade-mask/feather motif integrated into the bottle medallion around the existing 7. Make the bottle glass, liquid and reflections believable.

Use a dark charcoal/near-black interior with saturated magenta/fuchsia, coral-red, tangerine/orange, turquoise/teal and royal violet/indigo accents. Use ivory and small silver/iridescent highlights. Gold/champagne is only a trace accent in a few reflections and beads, never the dominant color. Avoid a blue-dominant, white-firework, metallic-futurist or gold-dominant look. Avoid flags, school crests, sports/team colors, football or any specific samba-school identity.

Preserve the original compact, pale translucent gray-white S-shaped rosh smoke wisp: same origin, scale, direction and visual weight. It must read as smoke, never as a colored ribbon or feather. Keep the exact “ADEGA DOS” wording and the number “7”; no dates, slogans or extra text. Keep every new theme element strictly inside the outermost emblem contour and keep the surrounding canvas solid black and clean. No extra rings, arcs, hoses, mouthpieces, rosh bowls, smoke plumes, external decorations or pseudo-text. The final logo must be crisp, premium, balanced and readable at 64–128 px.
```

## Iterações e decisões

### Iteração 1 — reconstrução carnavalesca

- fan de plumas, paetês, máscara, pedrarias, serpentinas e confetes criou uma leitura temática imediata;
- a paleta magenta/coral/turquesa/violeta com carvão diferenciou a peça das campanhas anteriores;
- a fumaça do rosh apareceu como uma fita colorida e precisava recuperar a assinatura do master.

### Iteração 2 — correção dirigida do rosh

- restaurado o wisp compacto, claro e translúcido do master;
- preservados a composição carnavalesca, o lettering, o `7`, a garrafa, o narguilé, a mangueira e a fronteira externa;
- saída selecionada para validação técnica e revisão humana.

## Critérios de aprovação e testes de contexto

- leitura imediata como **ADEGA DOS 7**;
- Carnaval perceptível no primeiro olhar por plumas, paetês, máscara, brilho, volume, serpentinas e confetes;
- miolo reconstruído, não apenas coberto por adesivos;
- identidade, fumaça do rosh, topologia da mangueira e arcos estruturais preservados;
- nenhuma decoração fora do emblema e nenhuma associação específica de escola/equipe;
- comparação lado a lado com `original.png`, `natal-2026.png` e `ano-novo-2027.png` realizada;
- thumbnail em 128 px e 64 px e versão em tons de cinza inspecionadas;
- avatar/canvas externo conferido: contorno preservado e área externa sem decoração.

## Validação técnica

Executados/registrados: `file`, `identify`, `sha256sum`, `git hash-object`, `python scripts/validate_assets.py`, `python scripts/validate_repository.py` e `git diff --check`.

Resultado local: PNG decodificável, 1254 × 1254 px, 8-bit sRGB Palette com 256 cores, SHA-256 e hash Git local registrados acima. Blob remoto e CI serão preenchidos após o commit/PR; o gate humano continua pendente.

## Reprodutibilidade e limitações

- ferramenta: built-in `image_gen`;
- referências: `original.png` como identidade, `natal-2026.png` como tratamento, `ano-novo-2027.png` como contraste;
- primeira saída: `generated_images/exec-20669fe5-efe7-4a00-aeea-26d48c15c304.png`;
- edição final: `generated_images/exec-66b756d3-0f1a-49a0-ba9d-31d1a944e431.png`;
- seed e parâmetros internos: NOT_RECORDED;
- a primeira geração estabeleceu a reconstrução interna; a segunda foi uma edição dirigida para corrigir exclusivamente a fumaça do rosh;
- geração raster pode alterar pixels estruturais de forma não determinística; revisão adversarial, testes de contexto e aprovação humana continuam obrigatórios;
- não há vetor mestre derivado nesta rodada.
