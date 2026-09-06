---
name: documentation
description: Mantém documentação, provenance, prompts e instruções de agentes da ADEGA DOS 7 consistentes, concisos e sem fontes concorrentes. Use ao alterar README, docs, AGENTS.md, skills, prompts, custom agents ou registros de assets.
---

# Documentation

## Princípios

- `AGENTS.md` é a entrada canônica compartilhável.
- `.agents/` contém regras, specs, skills, memória e estado estruturado.
- `docs/` contém conhecimento detalhado e provenance.
- adaptadores específicos de ferramenta devem permanecer finos.
- a marca é escrita como **ADEGA DOS 7** em texto humano.

## Antes de editar

1. identifique a fonte de verdade do assunto;
2. procure duplicações e links dependentes;
3. preserve informação factual e provenance;
4. evite transformar suposição em regra.

## Depois de editar

- valide links/path citados;
- execute `python scripts/validate_repository.py`;
- confirme que README descreve somente arquivos realmente presentes;
- atualize `docs/references.md` quando uma decisão depender de fonte externa nova;
- atualize provenance de asset quando uma decisão visual material mudar.

## Estilo

Prefira instruções curtas, testáveis e específicas. Use documentação extensa apenas onde a complexidade justifique. Não replique o mesmo bloco em `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` e `.github/copilot-instructions.md`.
