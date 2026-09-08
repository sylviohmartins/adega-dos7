# Natal 2026 — Design Packet, plano de produção e provenance

Este documento registra o plano profissional de criação da arte `assets/logos/natal-2026.png`: briefing, linhagem, invariantes, blueprint, arquitetura de prompts, evolução, QA e critérios de aprovação. Ele deve permitir que outro designer ou agente entenda a intenção sem depender da memória da sessão original.

## 1. Linhagem e papel do asset

`assets/logos/original.png` é o master canônico da identidade da **ADEGA DOS 7**. A arte de Natal é uma variação sazonal derivada desse master:

```text
ORIGINAL — matriz permanente
        │
        ├── preserva forma, objetos, lettering e reconhecimento
        │
        └── adiciona direção de arte de Natal
                │
                └── NATAL 2026 — variação temática
```

A versão Natal não é um redesign, não substitui o master e não deve ser usada para reconstruir a identidade original. Ao criar uma nova campanha, comece novamente por `assets/logos/original.png`.

## 2. Identificação do asset

```text
arquivo: assets/logos/natal-2026.png
formato: PNG
modo: 8-bit sRGB TrueColor
canvas: 1254 × 1254 px
proporção: 1:1
tamanho: 1.992.770 bytes
git blob SHA-1: 93779db0718c0694d8f3e4212f575eac401ae05e
SHA-256: 36ce17914341f47179ebdf9de8e341cdff5d66307c2a66e4fe4d5d600d955479
última correção: 2026-09-08 — normalização do enquadramento e alinhamento da fumaça do rosh
PR da correção: https://github.com/sylviohmartins/adega-dos7/pull/8
CI remoto: Validate visual assets ✅; Repository policy ✅
```

Master de referência:

```text
arquivo: assets/logos/original.png
SHA-256: f2fd213e95022e63829c47afc673fe8989d373b63cba0a742bfa888a77f17703
```

## 3. Briefing de design

### Objetivo

Criar uma edição de Natal premium do logo **ADEGA DOS 7**, preservando a identidade original e fazendo o tema entrar como uma camada visual secundária, controlada e reconhecível.

### Percepção desejada

> **“É exatamente o ADEGA DOS 7, porém em uma edição especial premium de Natal.”**

### Direção de arte

- atmosfera: festiva, sofisticada e acolhedora;
- materiais: vidro, metal, madeira e detalhes de acabamento premium;
- luz: quente, controlada e com highlights legíveis;
- ritmo: detalhado, porém organizado;
- ornamentação: integrada à composição, nunca acumulada sobre os objetos;
- estilo: emblema vintage-premium, ilustrativo e sem aparência cartoon/neon.

## 4. Critérios de sucesso

A variação só é aprovada quando:

- continua imediatamente reconhecível como **ADEGA DOS 7**;
- preserva o mesmo emblema, lettering, garrafa, número `7`, narguilé, mangueira e piteira do master;
- comunica Natal por cor, material, luz e ornamentos, sem precisar de texto explicativo;
- mantém a topologia física dos objetos;
- mantém a fumaça original do rosh visível e reconhecível;
- não introduz ruído, duplicações ou elementos temáticos que roubem o foco;
- funciona em tamanho normal, thumbnail e avatar;
- passa pela validação técnica e pelo registro de provenance.

Princípio de decisão:

> **RECOGNITION FIRST. THEME SECOND.**

## 5. Invariantes e variáveis

### Invariantes obrigatórios

- emblema circular em composição 1:1;
- texto exato `ADEGA DOS` no arco superior;
- garrafa central;
- número `7` como assinatura dominante;
- narguilé à esquerda;
- uma mangueira contínua;
- uma única piteira final;
- fumaça característica do rosh, com a mesma origem, curva, escala e peso visual do master;
- fundo preto e molduras metálicas;
- coerência de escala, encaixe, volumes e conexões;
- identidade de acabamento vintage-premium.

### Variáveis controladas pelo tema

- paleta secundária;
- iluminação e reflexos;
- folhas, pinhas, azevinho e outros ornamentos periféricos;
- fitas e luzes quentes, quando não cobrirem a identidade;
- materiais e pequenos highlights;
- atmosfera festiva;
- densidade de decoração, sempre subordinada à marca.

## 6. Theme Research Pack

Para este tema, a pesquisa foi convertida em códigos visuais simples e riscos de associação:

| Categoria | Decisão |
| --- | --- |
| códigos positivos | verde profundo, bordô/vinho, dourado metálico, champagne, pinheiro, azevinho e luz quente |
| atmosfera | Natal premium, sóbrio e integrado ao emblema |
| evitar | cartoon, neon, neve excessiva, Papai Noel como foco e decoração cobrindo objetos |
| risco cromático | verde + amarelo/dourado + branco pode remeter a Copa/Brasil |
| mitigação | aprofundar verde, incluir bordô/vinho, restringir branco e usar dourado como metal |

## 7. Design Packet / blueprint

### Hierarquia P1–P4

1. **P1 — garrafa + número 7**;
2. **P2 — `ADEGA DOS`**;
3. **P3 — narguilé + mangueira + piteira**;
4. **P4 — decoração natalina e acentos periféricos**.

### Mapa do canvas

```text
┌──────────────────────────────────┐
│         ADEGA DOS [P2]           │
│       arco superior legível       │
│                                  │
│  NARGUILÉ [P3]    GARRAFA [P1]   │
│       │               7           │
│       │              [P1]         │
│       ╰──── 1 MANGUEIRA ───────► │
│                     1 PITEIRA     │
│        decoração temática [P4]   │
└──────────────────────────────────┘
```

Regras de composição:

- manter o centro óptico na garrafa e no `7`;
- deixar o arco superior respirado para o lettering;
- não esconder a saída do narguilé;
- não ocupar a base de modo que a mangueira perca continuidade;
- reservar safe area externa para avatar e recortes quadrados;
- manter ornamentos fora das áreas de maior contraste do nome e do rótulo.

## 8. Arquitetura de prompt

O prompt de produção deve ser montado em blocos, para separar intenção de decoração e facilitar correções:

1. papel: diretor de arte, designer de identidade e revisor visual;
2. referência: `assets/logos/original.png` como fonte de verdade;
3. invariantes: objetos, texto, composição, proporções, topologia e fumaça característica do rosh;
4. direção temática: Natal traduzido por paleta, material, luz e ornamentação;
5. materialidade: vidro, cobre, bronze, madeira, verde profundo e bordô controlado;
6. negativos: duplicações, texto aleatório, ruído, estética esportiva, cartoon/neon e excesso de neve;
7. saída: canvas 1:1, alta resolução, bordas limpas e leitura em thumbnail;
8. QA: tratar a primeira saída como rascunho e corrigir antes da aprovação.

### Prompt-base para futuras variações

```text
Atue como diretor de arte e designer de identidade visual da ADEGA DOS 7.
Use assets/logos/original.png como matriz canônica e preserve reconhecimento antes
de aplicar o tema. Mantenha o emblema circular, o texto exato ADEGA DOS, a garrafa
central, o número 7, o narguilé à esquerda, uma única mangueira contínua, uma
única piteira final e a fumaça compacta e característica do rosh. Preserve escala,
encaixes, materiais e leitura em thumbnail.

Adicione Natal apenas como camada secundária por meio de verde profundo, bordô/vinho,
dourado metálico, champagne, luz quente e ornamentação periférica fina. Não use
texto secundário, placas, slogans, estrelas soltas, peças flutuantes, mangueiras
duplicadas, piteiras duplicadas, Papai Noel como foco, estética cartoon/neon,
neve excessiva ou paleta que remeta à Copa/Brasil.

Entregue um emblema 1:1, premium, detalhado e legível. A primeira renderização é
um rascunho: faça revisão adversarial, corrija anomalias localmente e só então
exporte a versão final.
```

O prompt-base deve ser combinado com o Design Packet específico da campanha e com `docs/image-generation-prompt.md`; não substitui a revisão humana.

## 9. Fluxo de produção e gates

```text
BRIEF
  ↓
DESIGN PACKET + THEME RESEARCH PACK
  ↓
PROMPT DE PRODUÇÃO
  ↓
PRIMEIRA SAÍDA = RASCUNHO
  ↓
DESIGN QA ADVERSARIAL
  ↓
EDIÇÃO LOCALIZADA E CONSERVADORA
  ↓
TESTES DE THUMBNAIL / AVATAR / CONTEXTO
  ↓
EXPORTAÇÃO BINÁRIA + PROVENANCE
  ↓
VALIDAÇÃO LOCAL + PR + VALIDAÇÃO REMOTA
```

Bloqueadores interrompem o fluxo: texto incorreto, identidade perdida, objeto ausente, conexão impossível, duplicação funcional, corte relevante, associação temática errada ou arquivo inválido/truncado.

## 10. Topologia funcional

Um dos principais controles é tornar a mecânica do narguilé inequívoca:

```text
NARGUILÉ
└── 1 saída visível
    └── 1 mangueira contínua
        └── 1 piteira final

ROSH
└── fumaça característica preservada
```

Versões intermediárias sugeriam duas mangueiras ou múltiplas piteiras/peças metálicas. Isso foi tratado como anomalia estrutural e removido.

## 11. Evolução e decisões de revisão

### Iteração 1 — Natal premium

Introduziu verde profundo, dourado, bordô, pinheiro, azevinho, luzes quentes e ornamentos. O problema foi uma placa inferior com `EDIÇÃO DE NATAL`, que criava um elemento estrutural inexistente no master.

### Iteração 2 — remover texto secundário

Decisão: remover a placa e não substituí-la por `Feliz Natal`, `Boas Festas` ou `Feliz Ano Novo`. O tema deveria ser entendido visualmente.

### Iteração 3 — limpeza estrutural

Foram removidos estrelas laterais sem função, múltiplos segmentos de mangueira, peças metálicas redundantes e conexões ambíguas. A saída do narguilé, a mangueira e a piteira passaram a ser verificadas como uma cadeia única.

### Iteração 4 — correção de linguagem cromática

A combinação inicial de verde, dourado e branco lembrava uma estética esportiva/Copa. A paleta foi ajustada para verde natalino profundo, bordô/vinho, dourado metálico, champagne e branco mínimo.

### Iteração 5 — restauração localizada da fumaça do rosh (2026-09-08)

A revisão do asset aprovado identificou que a fumaça característica do rosh não estava presente. Uma edição gerada por IA foi testada com instrução de mudança única, mas a comparação pixel a pixel mostrou drift em toda a composição; essa saída foi rejeitada. A versão selecionada foi composta conservadoramente a partir do wisp do `original.png` sobre a Natal existente. A diferença ficou restrita à região da fumaça: 2.387 pixels alterados, com bounding box de 65 × 115 px após limiarização. Nenhum outro elemento foi redesenhado.

### Iteração 6 — normalização do enquadramento e alinhamento (2026-09-08)

A inspeção comparativa mostrou que o canvas já era `1254 × 1254 px`, mas o emblema natalino estava aproximadamente 18 px acima e 3 px à direita do enquadramento usado por `original.png`, `ano-novo-2027.png` e `carnaval-2027.png`. A correção final aplica somente uma translação inteira de `x=-3 px` e `y=+18 px`, preenchendo o espaço excedente com preto. Não há escala, interpolação, redesenho ou alteração de cor: a fumaça, o rosh e toda a decoração natalina se movem juntos, mantendo suas características.

## 12. Paleta funcional

| Função | Direção |
| --- | --- |
| base | preto profundo + verde natalino escuro |
| identidade/acabamento | dourado metálico |
| tema secundário | bordô/vinho |
| highlights | champagne quente |
| branco | mínimo, apenas reflexos essenciais |

## 13. Regras negativas consolidadas

Não utilizar:

- estrelas laterais decorativas sem função;
- texto secundário dentro do emblema;
- mais de uma mangueira ou piteira;
- peças metálicas soltas;
- Papai Noel como elemento principal;
- gorro na garrafa ou no número `7`;
- árvore de Natal ocupando o centro;
- excesso de neve;
- estética cartoon/neon;
- ornamentos que escondam a conexão do narguilé;
- vermelho excessivamente saturado;
- paleta que remeta à Copa/Brasil.

## 14. QA e evidências de aprovação

A revisão final deve conferir:

- texto `ADEGA DOS` e número `7`;
- hierarquia P1–P4;
- continuidade da mangueira e unicidade da piteira;
- quantidade e função dos objetos;
- contraste, materialidade e associação cromática;
- equilíbrio dos ornamentos;
- presença, origem e curva da fumaça característica do rosh;
- leitura em 128 px e 64 px;
- versão em tons de cinza;
- safe area e uso como avatar;
- formato, dimensões, decodificação, tamanho e SHA-256.

Comandos de validação do repositório:

```bash
python scripts/validate_assets.py
python scripts/validate_repository.py
git diff --check
```

Validação remota: o blob de `assets/logos/natal-2026.png` na branch `fix/natal-logo-frame-2026` confere com `93779db0718c0694d8f3e4212f575eac401ae05e`; `Repository policy` e `Validate visual assets` passaram no PR #8. A substituição continua aguardando aprovação visual humana no PR #8, em modo draft.

## 15. Como reproduzir uma nova edição temática

1. começar por `assets/logos/original.png`;
2. ler `AGENTS.md`, as regras de marca e o `Design System`;
3. preencher um Brief e um Theme Research Pack;
4. separar invariantes de variáveis;
5. modelar a topologia dos objetos;
6. construir o blueprint e definir a hierarquia;
7. montar o prompt por blocos, incluindo negativos e saída técnica;
8. gerar uma primeira proposta e tratá-la como rascunho;
9. fazer revisão adversarial e edição localizada;
10. validar em contexto, tecnicamente e remotamente;
11. registrar decisões, hashes e limitações no provenance;
12. abrir PR sem alterar o master original.

Consulte `.github/prompts/design-blueprint.prompt.md`, `.github/prompts/create-themed-image.prompt.md`, `.github/prompts/review-image.prompt.md`, `.github/prompts/record-provenance.prompt.md` e `docs/image-construction-workflow.md`.

## 16. Limitações de provenance

Não foram preservados nesta versão o seed específico do gerador nem os parâmetros internos do modelo de imagem. A tentativa de edição com `image_gen` foi usada como rascunho, mas rejeitada por alterar pixels fora do rosh. O asset final usa composição raster localizada do wisp original e depois uma translação inteira do quadro, sem reamostragem; isso preserva o restante da Natal e normaliza o enquadramento. O repositório preserva o asset final, o master de origem, o plano, as decisões, os critérios e os hashes; isso permite repetir o processo com controle, mas não promete reprodução pixel a pixel.
