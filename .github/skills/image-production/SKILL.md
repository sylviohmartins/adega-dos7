---
name: image-production
description: Planeja, constrói, revisa e valida imagens e variações da identidade visual da Adega dos 7. Use para criar ou adaptar qualquer arte, tema sazonal, campanha, logo ou peça visual do briefing ao arquivo final.
---

# Image Production Skill

## Objetivo

Transformar um briefing visual em uma arte coerente e verificável sem pular diretamente para a geração final.

## Fontes de verdade

Leia conforme necessário:

- `../../../docs/design-system.md` — princípios e disciplinas de design;
- `../../../docs/image-construction-workflow.md` — processo completo e Design Packet;
- `../../../docs/image-generation-prompt.md` — prompt mestre;
- `../../../docs/asset-management.md` — exportação, upload e validação binária.

## Fluxo obrigatório

### 1. Entender

Extraia do pedido:

- objetivo e uso;
- público/contexto;
- tema;
- referências obrigatórias;
- invariantes que não podem mudar;
- variáveis que podem mudar;
- elementos obrigatórios/proibidos;
- texto exato;
- formato e canais de uso.

Se faltar algo não bloqueante, faça uma suposição conservadora e registre-a no Design Packet.

### 2. Construir o Design Packet

Antes de qualquer prompt final, produza:

1. **Brief resumido** — uma frase de objetivo e uma frase de percepção desejada.
2. **Invariantes vs. variáveis** — o que permanece e o que pode ser tematizado.
3. **Hierarquia visual** — prioridade 1, 2 e 3.
4. **Mapa de objetos** — elementos e relações funcionais entre eles.
5. **Blueprint do canvas** — zonas, safe area, centro óptico, fluxo de leitura e caminho de elementos conectados.
6. **Estudo de valores** — claro/escuro e contraste antes da cor.
7. **Paleta e materiais** — cores dominantes, apoio, highlights e acabamentos.
8. **Tipografia** — texto exato, hierarquia, arco/alinhamento e legibilidade.
9. **Regras negativas** — erros e associações que devem ser evitados.
10. **Critérios de aceite** — bloqueadores e testes finais.

Use um esquema ASCII simples quando ajudar a esclarecer a construção, por exemplo:

```text
┌──────────────────────────────┐
│         TEXTO / ARCO         │
│                              │
│  OBJETO A    FOCO CENTRAL    │
│      ╲          │            │
│       ╲         │            │
│        ╰── fluxo/conexão ──► │
│       BASE / ELEMENTOS       │
└──────────────────────────────┘
```

O blueprint descreve relações e proporções; não precisa ser artisticamente bonito.

### 3. Traduzir tema em design

Não trate tema como uma lista de enfeites. Traduza-o por:

- paleta;
- luz;
- textura;
- materiais;
- atmosfera;
- ornamentos controlados;
- contexto cultural apropriado.

Para identidade de marca: **Recognition first. Theme second.**

### 4. Montar o prompt de produção

Use `docs/image-generation-prompt.md` como base e incorpore o Design Packet.

O prompt deve deixar explícitos:

- referência principal;
- objetivo;
- composição;
- hierarquia;
- elementos obrigatórios;
- relações físicas;
- texto exato;
- tema/paleta;
- elementos proibidos;
- critérios de qualidade;
- critérios de rejeição.

### 5. Revisar a primeira saída

Faça uma auditoria por categorias:

- identidade/branding;
- hierarquia e composição;
- coerência física e semântica;
- tipografia;
- cor e contraste;
- acessibilidade e legibilidade;
- anomalias típicas de IA;
- adaptação ao canal/tamanho;
- acabamento e produção.

Liste problemas concretos, não impressões vagas.

### 6. Corrigir em edição conservadora

Quando a base estiver boa, prefira edição localizada em vez de regenerar tudo.

Preserve regiões aprovadas e descreva precisamente:

- o que remover;
- o que reconstruir;
- o que não tocar;
- como validar a correção.

### 7. Validar em múltiplos contextos

Quando aplicável, confira:

- avatar/thumbnail pequeno;
- feed social;
- fundo claro e escuro;
- impressão;
- recorte seguro;
- leitura monocromática/sem depender apenas de cor.

### 8. Exportar e versionar

Antes de concluir:

- preserve o master;
- siga `docs/asset-management.md`;
- execute `python scripts/validate_assets.py` quando houver arquivo em `assets/`;
- valide remoto após o push.

## Bloqueadores de aprovação

Rejeite a arte se houver:

- texto incorreto;
- elemento obrigatório ausente;
- duplicação funcional não solicitada;
- conexão impossível ou ambígua;
- foco visual incorreto;
- identidade perdida;
- tema confundido com outra campanha/associação;
- corte acidental relevante;
- arquivo inválido ou truncado.
