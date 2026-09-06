---
name: repository-discovery
description: Mapeia rapidamente o repositório da ADEGA DOS 7 antes de uma mudança, identificando fontes de verdade, assets, regras, prompts, provenance, riscos e validações aplicáveis. Use ao entrar em um escopo desconhecido ou quando o impacto da solicitação ainda não estiver claro.
---

# Repository Discovery

## Objetivo

Construir contexto suficiente para agir sem especular e sem carregar o repositório inteiro.

## Procedimento

1. Leia `AGENTS.md`.
2. Identifique os paths diretamente afetados.
3. Leia a regra/skill mais próxima do escopo.
4. Para mudanças visuais, leia `docs/design-system.md` e o provenance do asset relevante em `docs/assets/`, se existir.
5. Para arquivos binários, leia `docs/asset-management.md`.
6. Para configuração de agentes, leia `.agents/config.json`, `.agents/README.md` e `docs/agent-compatibility.md`.
7. Identifique checks existentes em `.github/workflows/` e `scripts/`.
8. Produza um mapa curto de impacto: arquivos, dependências, riscos, checks e gates humanos.

## Regras

- Nunca responda sobre conteúdo de arquivo que não foi lido quando a resposta depende dele.
- Não assuma que README e árvore real estão sincronizados; confira os paths.
- Não pré-carregue todas as skills.
- Diferencie fatos observados de inferências.

## Saída

Entregue ou mantenha internamente um mapa com:

- objetivo;
- fontes de verdade;
- paths afetados;
- invariantes;
- riscos;
- validações;
- skill seguinte recomendada.
