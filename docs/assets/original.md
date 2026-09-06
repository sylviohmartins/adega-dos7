# Logo original — Design Packet e provenance

Este registro documenta o master canônico da identidade visual da **ADEGA DOS 7**. A imagem legada fornecida pelo responsável da marca é a referência de identidade; a versão final consolida essa linguagem com acabamento visual refinado e estabelece a base permanente para futuras adaptações.

A linhagem oficial é sempre **original → variação temática**. A versão Natal 2026 é uma aplicação sazonal derivada dessa matriz; ela não redefine nem substitui a logo original.

## Identificação do asset

```text
arquivo: assets/logos/original.png
formato: PNG
canvas: 1254 × 1254 px
perfil: sRGB
tamanho: 1.565.513 bytes
git blob SHA-1: ce614497ec742619aa28518ebdf2084471a3a7c1
SHA-256: f2fd213e95022e63829c47afc673fe8989d373b63cba0a742bfa888a77f17703
última validação local: 2026-09-06
```

O arquivo é o master da identidade-base. A logo natalina existente continua preservada como uma variação independente em `assets/logos/natal-2026.png`.

## Linhagem da marca

```text
assets/logos/original.png
        │
        ├── preserva composição, objetos, lettering e materiais
        │
        └── adiciona uma camada temática controlada
                │
                └── assets/logos/natal-2026.png
```

Regra operacional: novas campanhas devem começar pelo master original. O tema pode alterar paleta secundária, iluminação e ornamentação, mas não deve reescrever os invariantes da marca.

## Objetivo

Consolidar uma logo original permanente, refinada e tecnicamente pronta para uso, mantendo os elementos que tornam a **ADEGA DOS 7** reconhecível:

- emblema circular e enquadramento 1:1;
- lettering arqueado `ADEGA DOS`;
- garrafa central como elemento dominante;
- número `7` grande e legível;
- narguilé à esquerda;
- mangueira contínua e uma única piteira;
- acabamento vintage-premium com materiais metálicos e vidro;
- fundo externo preto, sem halo colorido;
- ornamentação pontual, fina e subordinada à marca.

Percepção desejada:

> “Esta é a identidade permanente da ADEGA DOS 7: premium, detalhada, reconhecível e sem uma temática sazonal aplicada.”

## Referências e decisões de direção

### Referência canônica de identidade

```text
origem: referência original legada fornecida pelo responsável da marca
formato: JPEG
canvas: 1024 × 1024 px
SHA-256: a2aa0febfd5bbead683f3100cc50f04cf643576f5a676528bf3d83a71e35e057
```

Essa referência orientou identidade, cores, fundo, proporções percebidas, presença dos objetos e ritmo visual não sazonal. Ela permanece registrada por hash, mas não foi adicionada ao repositório como asset oficial.

### Padrão de acabamento da família

O refinamento segue o padrão de qualidade esperado para as variações da marca: volumes legíveis, conexões físicas coerentes, anéis bem definidos, metais em cobre/bronze, sombras azul-petróleo controladas e leitura estável em escala reduzida. Esse padrão é compartilhado com a edição de Natal, sem inverter a relação de origem entre os arquivos.

## Design Packet

### Hierarquia

1. garrafa central e número `7`;
2. lettering `ADEGA DOS`;
3. narguilé, mangueira e piteira;
4. anéis, linhas e pequenos acentos ornamentais.

### Composição

- emblema circular centralizado, ocupando a maior parte do canvas;
- lettering acompanhando o arco superior;
- garrafa em eixo vertical no centro;
- narguilé à esquerda, com a mangueira atravessando a base sem cortar a marca;
- piteira única em primeiro plano;
- margem externa suficiente para leitura em avatar e thumbnail;
- respiro preservado entre texto, garrafa e molduras.

### Topologia funcional

```text
NARGUILÉ
└── 1 saída visível
    └── 1 mangueira contínua
        └── 1 piteira final
```

Duplicações, conexões impossíveis, bocais flutuantes ou peças metálicas sem função são bloqueadores de aprovação.

## Direção cromática final

| Função | Direção |
| --- | --- |
| fundo externo | preto sólido |
| interior do emblema | preto profundo com sombra azul-petróleo discreta |
| lettering e contorno principal | creme/marfim |
| anéis e acentos | cobre, bronze e laranja queimado |
| garrafa | vidro âmbar/cobre com sombras escuras |
| mangueira | carvão/azul-petróleo com detalhes metálicos controlados |
| dourado | apenas highlight metálico, sem dominar |

## Ornamentação e fumaça

A ornamentação foi mantida deliberadamente fina e pontual, seguindo o caráter da referência legada:

- uma linha interna cobre acompanhando o arco;
- três linhas horizontais finas em cada lateral;
- poucos traços radiais delicados próximos à garrafa;
- nenhum campo pontilhado ou conjunto de bolinhas;
- duas linhas de fumaça curtas e sutis acima do bowl do narguilé;
- nenhuma névoa colorida, aura ou fumaça ambiental ao redor do emblema.

## Camada temática removida

Foram excluídos pinheiros, azevinho, frutos, pinhas, bolas, fitas, luzes, neve, vermelho/bordô temático e demais ornamentos festivos. O master original não contém elementos de Natal, datas, slogans ou texto secundário.

## Critérios de aprovação visual

- `ADEGA DOS` permanece legível em tamanho normal e thumbnail;
- o `7` continua dominante e legível;
- garrafa, narguilé e mangueira são reconhecidos imediatamente;
- existe uma única mangueira terminando em uma única piteira;
- o fundo externo é preto e não apresenta halo azul;
- a versão em tons de cinza preserva a hierarquia;
- os detalhes laterais não viram ruído ou pontilhismo;
- a fumaça é mínima e não parece uma aura atmosférica;
- não há elementos natalinos, slogans ou símbolos extras.

## Validação técnica

Executados no branch de trabalho:

```text
python scripts/validate_assets.py
python scripts/validate_repository.py
git diff --check
```

Os dois PNGs de `assets/logos/` foram validados quanto a formato, dimensões, decodificação e SHA-256. Também foram conferidas versões reduzidas de 128 px e 64 px e uma leitura em tons de cinza.

## Status de promoção

O responsável aprovou esta versão para ser usada como logo original. A alteração foi preparada em branch própria e deve ser promovida por pull request, mantendo o histórico de `main` intacto.

## Limitações de provenance

Não foram preservados seed ou parâmetros internos do gerador. O registro mantém as referências, decisões, hash local e critérios necessários para orientar novas produções, mas não promete reprodução pixel a pixel.
