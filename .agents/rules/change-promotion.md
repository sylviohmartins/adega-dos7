# Promoção de mudanças

O repositório da **ADEGA DOS 7** não está acoplado a deploy automático de produção, mas alterações podem afetar diretamente ativos oficiais de marca. Por isso, promoção é baseada em risco de marca.

## Fluxo padrão

`BRANCH -> CHANGE -> PULL_REQUEST -> VALIDATE -> REVIEW -> PROMOTION_DECISION`

## Requer aprovação humana explícita

- mudança de invariantes da identidade;
- substituição de asset já aprovado;
- definição de novo logo primário;
- remoção destrutiva de asset oficial;
- incorporação de skill/plugin/MCP/hook externo ao repositório;
- mudança que altera o significado público da marca.

## Pode ser promovido após checks e revisão

- correções documentais sem mudança de identidade;
- melhorias de scripts e validações;
- ajustes de compatibilidade entre agentes;
- prompts/skills internos que não alterem ativos aprovados.

## Regras

- Não escreva diretamente em `main` por padrão.
- Abra PR cedo para tornar CI e review parte do loop.
- Falha de CI deve levar a diagnóstico e correção, não ao enfraquecimento do gate.
- Merge automático permanece desabilitado por padrão.
- Uma autorização explícita do responsável da marca pode satisfazer o gate humano para a mudança específica descrita.
