# Processo de construção de imagens

Este processo transforma um pedido visual em uma sequência reproduzível, semelhante ao trabalho de um designer que começa pelo briefing, passa por rascunhos/plantas e só depois finaliza a arte.

## Visão geral

```text
BRIEFING
  ↓
REFERÊNCIAS E RESTRIÇÕES
  ↓
DESIGN PACKET / BLUEPRINT
  ↓
ESTUDO DE VALORES E PALETA
  ↓
PROMPT DE PRODUÇÃO
  ↓
PRIMEIRA SAÍDA
  ↓
CRÍTICA E ANOMALIAS
  ↓
EDIÇÃO/CORREÇÃO
  ↓
TESTES DE USO
  ↓
EXPORTAÇÃO
  ↓
VALIDAÇÃO TÉCNICA
  ↓
COMMIT/PUSH
  ↓
VALIDAÇÃO REMOTA
```

## Etapa 1 — Normalizar o briefing

Registre:

- objetivo;
- tema;
- público/contexto;
- canal de uso;
- formato/proporção;
- referência principal;
- referências secundárias;
- texto exato;
- elementos obrigatórios;
- elementos proibidos;
- restrições de identidade;
- critérios de sucesso.

Não transforme lacunas pequenas em bloqueio. Faça suposições conservadoras e documente-as. Pergunte apenas quando uma informação faltante puder mudar completamente a solução.

## Etapa 2 — Separar invariantes e variáveis

Crie uma tabela:

| Tipo | Exemplos | Regra |
| --- | --- | --- |
| Invariante | nome, número 7, garrafa, narguilé | preservar |
| Estrutural do emblema | contorno, lettering, topologia funcional, arcos estruturais | preservar quantidade, raio e posição relativa |
| Variável controlada | paleta, luz, ornamentos, textura | adaptar ao tema |
| Resíduo interno | tracinhos, raios, barras, ornamentos de rótulo e padrões herdados | limpar ou reconstruir quando não definirem a marca |
| Decorativo | brilhos, folhas, pequenas peças | remover se gerar ruído |

Essa separação evita que uma variação temática vire redesign.

### 2.1 Contrato de transformação interna para logos sazonais

Antes do prompt de produção, escreva quatro listas. Elas impedem que a IA trate todos os pixels do master como obrigatórios ou apenas sobreponha enfeites:

```text
PRESERVAR  = contorno, lettering, garrafa/7, narguilé/rosh, fumaça característica,
             uma mangueira com uma piteira e arcos estruturais existentes;
LIMPAR     = tracinhos laterais, raios, barras, ornamentos de rótulo e preenchimentos
             internos herdados que não sejam parte do arcabouço;
RECONSTRUIR = miolo, paleta, materiais e símbolos necessários para o tema atual;
LIMITE     = toda a transformação permanece dentro do emblema, salvo exceção aprovada.
```

Para `PRESERVAR`, o Design Packet deve registrar a quantidade, o raio e a posição relativa dos arcos. Para `RECONSTRUIR`, o Theme Research Pack deve explicar quais códigos visuais tornam o tema reconhecível no mundo real e quais clichês ou associações devem ser evitados. A direção escolhida também deve ser comparada com Natal, Ano Novo e demais variações existentes; nenhuma paleta ou ornamento é herdado automaticamente.

## Etapa 3 — Modelar a semântica e a topologia dos objetos

Antes do desenho, descreva relações funcionais.

Exemplo:

```text
GARRAFA
└── rótulo
    └── número 7

NARGUILÉ
└── 1 saída
    └── 1 mangueira
        └── 1 piteira
```

Para cada conexão, defina:

- origem;
- destino;
- quantidade;
- continuidade;
- posição relativa;
- o que passa na frente/atrás.

Esse mapa é a principal defesa contra duplicações e peças que “nascem do nada”.

## Etapa 4 — Criar o Design Packet

O Design Packet é o equivalente digital ao rascunho/planta do designer. Ele deve existir antes do prompt final.

### 4.1 Brief de uma linha

> Criar `<peça>` que comunique `<percepção>` preservando `<invariantes>` e traduzindo `<tema>` por `<meios visuais>`.

### 4.2 Hierarquia

```text
P1 — foco principal
P2 — identificação/marca
P3 — elementos funcionais
P4 — decoração/contexto
```

### 4.3 Blueprint do canvas

Exemplo 1:1:

```text
┌────────────────────────────────┐
│        SAFE AREA SUPERIOR      │
│          ADEGA DOS             │
│        arco / identidade       │
│                                │
│  NARGUILÉ      GARRAFA/7       │
│    [P3]           [P1]         │
│      ╲             │           │
│       ╲            │           │
│        ╰──── mangueira ──────► │
│            base [P3]  piteira  │
│  ornamento [P4]   ornamento    │
│        SAFE AREA INFERIOR      │
└────────────────────────────────┘
```

O blueprint deve marcar:

- centro óptico;
- margens;
- zonas de texto;
- zonas de objeto;
- caminhos de conexão;
- sobreposição;
- áreas onde ornamentos são permitidos;
- áreas que devem permanecer limpas.

### 4.4 Proporções aproximadas

Não é necessário precisão CAD, mas use relações úteis:

```text
foco central: ~35–45% da altura útil
texto superior: ~15–20%
narguilé: ~25–35%
mangueira: percurso inferior sem cobrir assinatura principal
ornamentos: camada periférica, nunca dominante
```

Ajuste conforme o briefing.

### 4.5 Estudo de valores

Antes da cor, descreva massas de claro/escuro:

```text
FUNDO        ██████████  muito escuro
EMBLEMA      ███████░░░  escuro/médio
FOCO         ███░░░░░░░  claro
HIGHLIGHTS   █░░░░░░░░░  muito claro
```

O foco deve continuar evidente mesmo em escala de cinza.

### 4.6 Paleta e materiais

Defina função de cada cor, não apenas nomes:

| Função | Cor/material | Uso |
| --- | --- | --- |
| Base | verde-esmeralda profundo | estrutura/fundo interno |
| Identidade | dourado metálico | contorno, assinatura, highlights |
| Tema | bordô | fita/ornamentos controlados |
| Luz | champagne | reflexos e legibilidade |

Inclua associações indesejadas a evitar.

### 4.7 Tipografia

Registre:

- texto exato;
- posição;
- arco/alinhamento;
- caixa alta/baixa;
- prioridade;
- textura/acabamento;
- tamanho mínimo de leitura.

### 4.8 Negative space e safe areas

Defina onde **não** inserir detalhes. O espaço vazio é parte do design.

### 4.9 Critérios bloqueadores

Liste antes da geração. Exemplos:

- duas mangueiras quando deve haver uma;
- texto diferente de `ADEGA DOS`;
- número 7 deformado;
- tema confundido com seleção brasileira/Copa;
- ornamento cobrindo a saída do narguilé.

## Etapa 5 — Montar o prompt de produção

Use `docs/image-generation-prompt.md` e converta o Design Packet em instruções executáveis.

O prompt final deve responder:

1. o que criar/editar;
2. qual referência manda;
3. o que preservar;
4. o que mudar;
5. como organizar o canvas;
6. como os objetos se conectam;
7. quais cores/materiais usar;
8. qual texto exato usar;
9. o que preservar, limpar e reconstruir dentro do emblema;
10. o que evitar, inclusive elementos fora do emblema e códigos de outras campanhas;
11. como reconhecer sucesso no primeiro olhar.

## Etapa 6 — Primeira saída é rascunho, não conclusão

Trate a primeira imagem como proposta de design.

Faça crítica estruturada em três níveis:

### Bloqueadores

Impedem aprovação.

### Importantes

Não quebram a identidade, mas reduzem qualidade.

### Polimento

Melhorias finas.

## Etapa 7 — Auditoria de anomalias de IA

Faça uma varredura específica:

- quantidade de objetos;
- contagem, raio e posição dos arcos estruturais;
- mãos/anatomia quando houver pessoas;
- cabos/mangueiras;
- piteiras/bocais;
- texto e números;
- reflexos incoerentes;
- simetria falsa;
- ornamentos fundidos;
- peças metálicas sem função;
- objetos atravessando outros;
- sombras incompatíveis;
- perspectiva inconsistente;
- detalhes que parecem outra marca/tema.

Em logo sazonal, o finding também deve responder: o miolo foi realmente reconstruído para o tema ou apenas recebeu enfeites? O canvas externo permaneceu limpo? A paleta e os materiais pertencem ao tema atual ou foram carregados de outra variação?

## Etapa 8 — Corrigir por edição localizada

Quando 70–90% da arte estiver correta, prefira editar a região problemática.

Estrutura da instrução:

```text
PRESERVE: regiões A, B, C.
REMOVA: resíduos internos X, Y.
RECONSTRUA: o miolo temático seguindo continuidade de Y.
NÃO TOQUE: texto, garrafa, número 7, etc.
MANTENHA DENTRO: do emblema, sem decoração externa.
VALIDE: arcos, topologia, leitura do tema e condição objetiva após a edição.
```

## Etapa 9 — Testes de contexto

Quando aplicável, teste:

### Thumbnail

Reduza mentalmente/tecnicamente para 64–128 px. A marca ainda é reconhecível?

### Avatar

O recorte circular/quadrado mantém os elementos essenciais?

### Feed/story

Há safe area suficiente?

### Fundo

O contorno se separa do fundo?

### Escala de cinza

A hierarquia sobrevive sem a cor?

### Impressão

Detalhes e contrastes continuam reproduzíveis?

## Etapa 10 — Exportação

Defina:

- master;
- formato;
- dimensões;
- perfil de cor quando necessário;
- derivados por canal;
- naming convention.

O master nunca deve ser substituído silenciosamente por uma versão comprimida.

## Etapa 11 — Validação técnica e versionamento

Siga `docs/asset-management.md` e execute:

```bash
python scripts/validate_assets.py
```

Depois do push, valide remoto.

## Template resumido de Design Packet

```markdown
# Design Packet

## Objetivo
...

## Percepção desejada
...

## Invariantes
- ...

## Variáveis controladas
- ...

## Hierarquia
1. ...
2. ...
3. ...

## Topologia dos objetos
...

## Blueprint
```text
...
```

## Valores claro/escuro
...

## Paleta e materiais
...

## Tipografia
...

## Safe areas / negative space
...

## Proibições
- ...

## Bloqueadores de aprovação
- ...

## Contextos de teste
- ...
```

Esse pacote deve ser suficiente para outro designer/agente entender **como a imagem foi pensada**, e não apenas ver o resultado final.
