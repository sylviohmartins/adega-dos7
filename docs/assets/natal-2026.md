# Natal 2026 — Design Packet e provenance

Este documento registra **como a arte `assets/logos/natal-2026.png` foi construída**, quais decisões foram tomadas e quais problemas foram corrigidos ao longo das iterações. Ele serve como referência para designers e agentes futuros.

## Identificação do asset

```text
arquivo: assets/logos/natal-2026.png
formato: PNG
canvas: 1254 × 1254 px
proporção: 1:1
tamanho: 2.031.991 bytes
git blob SHA-1: d66d6bbd05d657a6abd7c9b9186f8b5daaecdefc
SHA-256: f1e71b265888a3f2c2c282245873ec46f9fcf987b58ae64958368c205e33e1d0
```

O blob remoto corresponde ao arquivo final local usado como referência na sessão de criação.

## Objetivo

Criar uma edição de Natal premium do logo **ADEGA DOS 7** sem transformar a marca em um redesign temático.

Percepção desejada:

> **“É exatamente o ADEGA DOS 7, porém em uma edição especial premium de Natal.”**

## Referência e identidade preservada

A construção partiu de uma imagem de referência fornecida na sessão de criação. O arquivo original ainda não está versionado neste repositório.

Elementos tratados como invariantes:

- emblema circular;
- texto `ADEGA DOS` arqueado no topo;
- garrafa central;
- número `7` como assinatura dominante;
- narguilé à esquerda;
- mangueira envolvendo a composição;
- linguagem detalhada/vintage-premium;
- fundo preto e contorno metálico.

## Variáveis temáticas

Foram autorizadas mudanças controladas em:

- paleta;
- iluminação;
- folhas e ornamentos periféricos;
- materiais/reflexos;
- detalhes de fita;
- atmosfera geral.

## Blueprint conceitual

```text
┌──────────────────────────────────┐
│         ADEGA DOS [P2]           │
│       arco superior limpo        │
│                                  │
│  NARGUILÉ [P3]    GARRAFA [P1]   │
│       │               7           │
│       │              [P1]         │
│       ╰──── 1 MANGUEIRA ───────► │
│                     1 PITEIRA     │
│                                  │
│  pinheiro/azevinho/fitas [P4]    │
└──────────────────────────────────┘
```

Hierarquia final:

1. garrafa + número 7;
2. `ADEGA DOS`;
3. narguilé + mangueira + piteira;
4. decoração natalina.

## Topologia funcional

Um dos principais refinamentos foi tornar a mecânica do narguilé inequívoca:

```text
NARGUILÉ
└── 1 saída visível
    └── 1 mangueira contínua
        └── 1 piteira final
```

Versões intermediárias sugeriam duas mangueiras e múltiplas piteiras/peças metálicas. Isso foi considerado anomalia estrutural e removido.

## Evolução da arte

### Iteração 1 — Natal premium

A primeira adaptação introduziu:

- verde profundo;
- dourado;
- bordô;
- pinheiro;
- azevinho;
- luzes quentes;
- ornamentos natalinos.

Problema identificado: foi adicionada uma placa inferior com o texto `EDIÇÃO DE NATAL`, criando um elemento estrutural que não existia no logo original.

### Iteração 2 — remover texto secundário

Decisão:

- remover completamente a placa;
- não substituir por `Feliz Natal`, `Boas Festas` ou `Feliz Ano Novo`;
- fazer o tema ser entendido visualmente.

Princípio reforçado:

> **Recognition first. Theme second.**

### Iteração 3 — limpeza estrutural

Foram identificados elementos gerados pela IA que não faziam sentido:

- estrelas antes/depois de `ADEGA DOS`;
- múltiplos segmentos parecendo mangueiras;
- peças metálicas redundantes;
- múltiplas piteiras;
- conexão pouco clara entre narguilé e mangueira.

Correções:

- remover estrelas;
- manter apenas uma mangueira;
- mostrar claramente a saída do narguilé;
- manter uma única piteira;
- reduzir ornamentos próximos à conexão funcional.

### Iteração 4 — correção de linguagem cromática

Mesmo após a correção estrutural, a combinação de verde, branco e dourado estava lembrando a estética da Copa do Mundo/seleção brasileira.

A direção cromática foi ajustada para afastar essa associação e tornar o Natal inequívoco:

- verde-esmeralda/natalino mais profundo;
- bordô/vinho mais presente;
- dourado metálico como acabamento premium;
- champagne nos highlights;
- branco restrito a reflexos essenciais;
- decoração natalina integrada à estrutura.

## Paleta funcional

| Função | Direção |
| --- | --- |
| Base | preto profundo + verde natalino escuro |
| Identidade/acabamento | dourado metálico |
| Tema secundário | bordô/vinho |
| Highlights | champagne/quente |
| Branco | mínimo, somente quando necessário |

Associação proibida identificada durante revisão:

- combinação verde + amarelo/dourado + branco com leitura esportiva/Brasil/Copa.

## Regras negativas consolidadas

Não utilizar:

- estrelas laterais decorativas sem função;
- texto secundário dentro do emblema;
- mais de uma mangueira;
- mais de uma piteira;
- peças metálicas soltas;
- Papai Noel como elemento principal;
- gorro na garrafa/número 7;
- árvore de Natal ocupando o centro;
- excesso de neve;
- estética cartoon/neon;
- ornamentos que escondam a conexão do narguilé;
- vermelho excessivamente saturado;
- paleta que remeta à Copa/Brasil.

## Critérios que determinaram a aprovação

A versão final foi considerada coerente quando:

- `ADEGA DOS` permaneceu legível;
- número 7 continuou dominante;
- garrafa manteve protagonismo;
- narguilé permaneceu reconhecível;
- uma única mangueira saiu claramente do narguilé;
- uma única piteira encerrou o percurso;
- estrelas e peças redundantes foram removidas;
- Natal passou a ser percebido pela paleta/material/ornamentos, sem texto explicativo;
- a arte deixou de remeter à estética da Copa do Mundo;
- a composição permaneceu premium e equilibrada.

## Como reproduzir ou criar uma nova variação

Não copie apenas o prompt final. Reaplique o processo:

1. leia a referência original;
2. separe invariantes e variáveis;
3. modele a topologia dos objetos;
4. produza blueprint;
5. traduza o novo tema por direção de arte;
6. gere uma primeira proposta;
7. trate a saída como rascunho;
8. procure anomalias estruturais e associações indesejadas;
9. corrija por edição localizada;
10. valide em contexto e tecnicamente.

Consulte `docs/image-construction-workflow.md` e `.github/skills/image-production/SKILL.md` para o processo completo.

## Limitações de provenance

Não foram preservados nesta versão:

- seed específico do gerador;
- parâmetros internos do modelo de imagem;
- arquivo original de referência dentro do repositório.

Esses itens devem ser registrados em futuras produções quando estiverem disponíveis e forem úteis para reprodutibilidade.
