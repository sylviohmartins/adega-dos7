# Adega dos 7

Repositório oficial para organização, evolução e preservação da identidade visual da **Adega dos 7**, incluindo assets, variações temáticas, prompts, skills, agentes e documentação do processo de design.

<p align="center">
  <img src="assets/logos/natal-2026.png" alt="Adega dos 7 — Natal 2026" width="480">
</p>

<p align="center">
  <a href="https://www.instagram.com/adega.dos7/">Instagram · @adega.dos7</a>
</p>

## Objetivo

O repositório funciona como **fonte de verdade da identidade visual** e também como base operacional para designers e agentes de IA criarem novas artes sem perder contexto, consistência ou rastreabilidade.

A abordagem adotada é:

> **Recognition first. Theme second.**

Uma variação sazonal deve continuar imediatamente reconhecível como **ADEGA DOS 7**. O tema complementa a marca; não a substitui.

## Princípios da identidade

Elementos centrais atualmente tratados como referência da marca:

- composição em formato de emblema;
- texto **ADEGA DOS** claramente legível;
- número **7** como assinatura visual dominante;
- garrafa como elemento central;
- narguilé como elemento característico;
- mangueira e piteira com lógica visual/física coerente;
- acabamento detalhado e premium;
- variações temáticas aplicadas de forma controlada.

## Como uma nova arte é construída

O fluxo não pula do briefing diretamente para a imagem final.

```text
BRIEFING
   ↓
DESIGN PACKET / BLUEPRINT
   ↓
PROMPT DE PRODUÇÃO
   ↓
PRIMEIRA SAÍDA = RASCUNHO
   ↓
REVISÃO DE DESIGN + ANOMALIAS DE IA
   ↓
EDIÇÃO/CORREÇÃO
   ↓
TESTES DE CONTEXTO
   ↓
VALIDAÇÃO TÉCNICA
   ↓
COMMIT / PUSH
   ↓
VALIDAÇÃO REMOTA
```

O **Design Packet** funciona como o rascunho/planta do designer: registra hierarquia, composição, zonas do canvas, relações entre objetos, paleta, tipografia, safe areas, negative space e critérios de aprovação antes da geração final.

Processo completo: **[docs/image-construction-workflow.md](docs/image-construction-workflow.md)**.

## Arquitetura para agentes de IA

O repositório separa contexto persistente de conhecimento carregado sob demanda e usa adaptadores finos para diferentes agentes:

```text
AGENTS.md
│   fonte canônica de instruções gerais
│
├── CLAUDE.md
│   adaptador para Claude Code
│
├── GEMINI.md
│   adaptador para Gemini CLI
│
├── .github/copilot-instructions.md
│   contexto persistente para Copilot
│
├── .github/instructions/
│   └── assets.instructions.md
│       regras específicas para arquivos visuais
│
├── .github/skills/
│   └── image-production/SKILL.md
│       workflow especializado de produção visual
│
├── .github/agents/
│   └── art-director.agent.md
│       diretor de arte especializado
│
└── .github/prompts/
    ├── design-blueprint.prompt.md
    ├── create-themed-image.prompt.md
    └── review-image.prompt.md
```

Essa separação evita repetir um prompt gigante em todas as tarefas e reduz divergência entre ferramentas. Veja **[docs/agent-compatibility.md](docs/agent-compatibility.md)**.

## Disciplinas de design consideradas

O processo de revisão contempla, quando aplicável:

- brand strategy e identidade visual;
- direção de arte;
- graphic/visual design;
- composição, grids e equilíbrio;
- visual hierarchy;
- tipografia;
- teoria e psicologia da cor;
- ilustração e iconografia;
- UX aplicada a reconhecimento e contexto de uso;
- UI/digital presentation;
- acessibilidade e inclusive design;
- social media design;
- packaging/print/prepress;
- design QA;
- engenharia de prompt para imagens.

Critérios detalhados: **[docs/design-system.md](docs/design-system.md)**.

## Prompt universal

Para criar ou adaptar uma imagem para **qualquer tema**, use:

- **[docs/image-generation-prompt.md](docs/image-generation-prompt.md)** — prompt mestre universal;
- **[.github/prompts/design-blueprint.prompt.md](.github/prompts/design-blueprint.prompt.md)** — cria o rascunho/planta antes da arte;
- **[.github/prompts/create-themed-image.prompt.md](.github/prompts/create-themed-image.prompt.md)** — transforma o blueprint em produção;
- **[.github/prompts/review-image.prompt.md](.github/prompts/review-image.prompt.md)** — revisão adversarial da saída.

## Provenance: como cada imagem foi criada

Cada arte relevante pode ter um registro de design contendo:

- objetivo e contexto;
- referências;
- invariantes e variáveis;
- blueprint;
- topologia dos objetos;
- paleta e tipografia;
- iterações;
- problemas encontrados;
- decisões de correção;
- critérios de aprovação;
- dimensões e hashes;
- limitações de reprodutibilidade.

Registro da versão atual:

- **[Natal 2026 — Design Packet e provenance](docs/assets/natal-2026.md)**

Template para novas artes:

- **[docs/templates/asset-design-record.md](docs/templates/asset-design-record.md)**

## Estrutura atual

```text
.
├── AGENTS.md
├── CLAUDE.md
├── GEMINI.md
├── .gitattributes
├── README.md
├── .github/
│   ├── agents/
│   ├── instructions/
│   ├── prompts/
│   ├── skills/
│   ├── workflows/
│   └── copilot-instructions.md
├── assets/
│   └── logos/
│       └── natal-2026.png
├── docs/
│   ├── assets/
│   │   └── natal-2026.md
│   ├── templates/
│   │   └── asset-design-record.md
│   ├── agent-compatibility.md
│   ├── asset-management.md
│   ├── design-system.md
│   ├── image-construction-workflow.md
│   ├── image-generation-prompt.md
│   └── references.md
└── scripts/
    └── validate_assets.py
```

## Convenção de nomes

Identidade-base:

```text
original.png
```

Variações temáticas:

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

- minúsculas;
- sem espaços;
- hífen como separador;
- sem `final`, `v2`, `definitivo`, `corrigido` etc.;
- o histórico do Git é responsável pelas revisões.

## Gestão segura de imagens

Arquivos raster são binários e não devem ser gravados por operações destinadas a conteúdo UTF-8.

Antes e depois de qualquer alteração em `assets/`, validar:

1. formato real;
2. dimensões;
3. tamanho em bytes;
4. estrutura/decodificação completa;
5. SHA-256;
6. preview/download remoto após o push.

Validação local:

```bash
python scripts/validate_assets.py
```

O GitHub Actions executa a mesma validação automaticamente quando assets ou o validador mudam.

Detalhes: **[docs/asset-management.md](docs/asset-management.md)**.

## Referências de mercado

A arquitetura de agentes e os critérios de design foram baseados em documentação e referências de OpenAI/Codex, GitHub Copilot, Anthropic Agent Skills/Claude Code, Gemini CLI, Nielsen Norman Group, Apple Human Interface Guidelines e WCAG.

Veja **[docs/references.md](docs/references.md)**.

## Regra de conclusão

Uma arte só é considerada concluída quando estiver:

- visualmente coerente;
- fiel à identidade;
- sem anomalias estruturais;
- adequada aos principais contextos de uso;
- tecnicamente íntegra;
- corretamente versionada e validada no remoto.
