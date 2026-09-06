---
name: agent-asset-vetting
description: Avalia skills, prompts, custom agents, MCPs, plugins, hooks e extensões de terceiros antes de incorporá-los ao ecossistema da ADEGA DOS 7. Use ao pesquisar marketplaces, GitHub ou documentação externa para ampliar capacidades de agentes.
---

# Agent Asset Vetting

## Objetivo

Separar descoberta de adoção. Um asset externo pode inspirar arquitetura sem ser copiado ou instalado.

## Pipeline

`DISCOVER -> SOURCE_VERIFY -> LICENSE -> STATIC_REVIEW -> PERMISSIONS -> OVERLAP -> SANDBOX -> BENCHMARK -> DECISION`

## Checklist

### Origem

- mantenedor identificável;
- repositório/fonte original;
- documentação atual;
- atividade recente quando manutenção for relevante.

### Licença

- licença explícita;
- compatibilidade com uso/adaptação;
- obrigações de attribution/NOTICE quando houver cópia.

### Segurança

- filesystem;
- shell;
- rede;
- navegador;
- secrets;
- contas externas;
- install/postinstall;
- downloads dinâmicos;
- prompt injection/exfiltração.

### Valor

- qual problema da **ADEGA DOS 7** resolve;
- o que já existe localmente;
- se uma adaptação menor é suficiente;
- benefício mensurável em qualidade, segurança, velocidade ou consistência.

## Decisão

Registre conforme `.agents/schemas/agent-asset-assessment.schema.json`:

- `ADOPT`;
- `ADAPT`;
- `TRIAL`;
- `REJECT`;
- `SUPERSEDED`.

## Regra de licenciamento

Quando apenas princípios conceituais forem úteis, prefira reimplementação original e documente a fonte de inspiração. Se houver cópia/adaptação de conteúdo licenciado, preserve as obrigações aplicáveis.

## Gate

Incorporação de terceiro ao repositório é uma mudança de promoção controlada e requer aprovação humana conforme `.agents/rules/change-promotion.md`.
