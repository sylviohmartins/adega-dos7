# Adega dos 7

Repositório oficial para organização, versionamento e preservação das identidades visuais da **Adega dos 7**, incluindo logo-base, variações sazonais e materiais derivados.

<p align="center">
  <img src="assets/logos/natal-2026.png" alt="Adega dos 7 — Natal 2026" width="480">
</p>

<p align="center">
  <a href="https://www.instagram.com/adega.dos7/">Instagram · @adega.dos7</a>
</p>

## Sobre a marca

A presença pública da **Adega dos 7** no Instagram está associada a **São Paulo, SP** e reforça uma comunicação baseada em confiança, originalidade dos produtos, lacre e cuidado com a experiência do cliente.

Este repositório funciona como fonte de verdade para a evolução da identidade visual, evitando arquivos espalhados, nomes ambíguos e perda de rastreabilidade entre versões.

## Princípios da identidade visual

As variações devem continuar imediatamente reconhecíveis como **ADEGA DOS 7**.

Elementos centrais da identidade:

- composição em formato de emblema;
- texto **ADEGA DOS** claramente legível;
- número **7** como assinatura visual dominante;
- garrafa como elemento central;
- narguilé como elemento característico;
- uma única mangueira funcional, com origem e piteira visualmente coerentes;
- acabamento detalhado e premium;
- temas sazonais como camada complementar, nunca como substituição da identidade.

> **Recognition first. Theme second.**

## Estrutura atual

```text
.
├── .gitattributes
├── README.md
├── assets/
│   └── logos/
│       └── natal-2026.png
└── docs/
    ├── asset-management.md
    └── image-generation-prompt.md
```

Novos arquivos devem ser adicionados à estrutura somente quando existirem de fato no repositório; o README não deve anunciar assets ainda não versionados.

## Convenção de nomes

Identidade-base:

```text
original.png
```

Variações temáticas/sazonais:

```text
<tema>-<ano>.<extensão>
```

Exemplos:

```text
copa-2026.png
natal-2026.png
ano-novo-2027.png
carnaval-2027.png
```

Regras:

- nomes em minúsculas;
- sem espaços;
- usar hífen como separador;
- não usar `final`, `final2`, `v2`, `definitivo` ou equivalentes;
- revisões são controladas pelo histórico do Git.

## Gestão segura de imagens

Arquivos raster são tratados explicitamente como **binários** por meio do `.gitattributes`.

Antes e depois de qualquer upload/substituição, validar:

1. formato real do arquivo;
2. dimensões e proporção;
3. tamanho em bytes;
4. decodificação completa da imagem;
5. integridade por hash quando possível;
6. preview remoto completo após o push.

Não utilizar operações destinadas a conteúdo UTF-8 para gravar PNG/JPG. Não converter imagens em texto, não usar Base64 parcial e não considerar a tarefa concluída apenas porque o commit foi criado.

O procedimento detalhado está em **[docs/asset-management.md](docs/asset-management.md)**.

## Geração e adaptação de novas artes

Para manter consistência entre futuras campanhas, o repositório contém um prompt mestre reutilizável para:

- criar imagens do zero;
- editar uma imagem existente;
- adaptar o logo para qualquer tema;
- controlar composição, hierarquia, paleta e tipografia;
- detectar objetos duplicados, conexões sem sentido e outros artefatos comuns de geração por IA;
- definir critérios objetivos de aprovação antes de considerar uma arte concluída.

Consulte **[docs/image-generation-prompt.md](docs/image-generation-prompt.md)**.

## Fluxo recomendado

```text
REFERÊNCIA / BRIEFING
        ↓
GERAÇÃO OU EDIÇÃO
        ↓
REVISÃO VISUAL E SEMÂNTICA
        ↓
VALIDAÇÃO TÉCNICA DO ARQUIVO
        ↓
COMMIT / PUSH
        ↓
VALIDAÇÃO DO ARQUIVO REMOTO
```

Uma arte só deve ser considerada concluída quando estiver **visualmente aprovada e tecnicamente íntegra** no repositório.
