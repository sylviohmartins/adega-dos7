# AGENTS.md

## Missão

Manter este repositório como fonte de verdade da identidade visual e do processo de produção da **ADEGA DOS 7**. Preservar reconhecimento, coerência de marca, provenance e integridade dos assets é mais importante do que volume de mudanças ou criatividade não solicitada.

Este é o arquivo canônico de instruções para agentes de IA.

## Hierarquia de instruções

Para trabalho no repositório, use esta ordem:

1. pedido explícito do usuário/responsável da marca;
2. `AGENTS.md` mais próximo do arquivo, se houver;
3. este `AGENTS.md` raiz;
4. regra aplicável em `.agents/rules/`;
5. skill específica em `.agents/skills/`;
6. documentação/provenance existente em `docs/`;
7. implementação/configuração local;
8. documentação oficial da ferramenta instalada.

`CLAUDE.md`, `GEMINI.md` e `.github/copilot-instructions.md` são adaptadores de compatibilidade e não devem virar fontes concorrentes.

## Nome da marca

Em texto humano, documentação, prompts, relatórios e metadados, escreva sempre **ADEGA DOS 7** em maiúsculas. O identificador técnico do repositório `adega-dos7` permanece em minúsculas apenas quando necessário em URLs, paths e comandos.

## Modelo de execução

Siga `.agents/specs/execution-model.md`.

Fluxo padrão:

`DISCOVER -> PLAN -> BRANCH -> CHANGE -> PULL_REQUEST -> VALIDATE -> DIAGNOSE -> REVISE -> REVIEW -> PROMOTION_DECISION`

Para produção visual:

`BRIEF -> THEME_RESEARCH? -> DESIGN_PACKET -> PRODUCTION -> DRAFT -> DESIGN_QA -> CONSERVATIVE_EDIT -> CONTEXT_TESTS -> EXPORT -> VALIDATE`

Trabalhe fora de `main` por padrão. Abra PR para tornar CI e review parte do loop. Falha de validação é feedback: diagnostique e corrija a causa, não enfraqueça o gate.

Para tarefas longas, multi-requisito ou multiagente, use `.agents/specs/completion-contract.md`, `.agents/skills/task-completion/SKILL.md` e estado em `.agents/runs/`.

## Contexto progressivo

Leia primeiro:

1. `README.md`;
2. `docs/design-system.md` quando houver impacto visual;
3. `docs/image-construction-workflow.md` para criação/edição de imagem;
4. `docs/asset-management.md` para binários;
5. provenance específico em `docs/assets/` quando tocar uma arte existente.

Depois carregue apenas as regras/skills necessárias. Siga `.agents/rules/context-efficiency.md`.

## Roteamento de skills

- escopo desconhecido / mapa de impacto: `.agents/skills/repository-discovery/SKILL.md`;
- pedido complexo / critérios de aceite: `.agents/skills/planning/SKILL.md`;
- tarefa longa / requisitos e evidências: `.agents/skills/task-completion/SKILL.md`;
- criação ou adaptação visual: `.agents/skills/image-production/SKILL.md`;
- revisão adversarial de design: `.agents/skills/design-review/SKILL.md`;
- upload, substituição e integridade de binários: `.agents/skills/asset-management/SKILL.md`;
- skill/plugin/MCP/hook/agente externo: `.agents/skills/agent-asset-vetting/SKILL.md`;
- documentação, provenance e instruções: `.agents/skills/documentation/SKILL.md`.

## Comandos de validação

Use os scripts do repositório:

```bash
python scripts/validate_repository.py
python scripts/validate_assets.py
```

Execute `validate_assets.py` quando `assets/` mudar. Execute `validate_repository.py` para mudanças de documentação, prompts, agents, skills, schemas, workflows ou configuração.

Nunca declare que um check passou se ele não foi executado.

## Regras permanentes de marca e design

Siga `.agents/rules/brand-integrity.md`.

1. **Reconhecimento primeiro; tema depois.**
2. Não pule do briefing para a arte final: produza Design Packet/blueprint.
3. Quando o tema exigir pesquisa, faça Theme Research Pack antes da direção final.
4. Modele objetos funcionais e suas conexões; não aceite duplicações ou peças sem origem lógica.
5. Texto em imagem deve corresponder exatamente ao briefing aprovado.
6. Revise hierarquia, composição, tipografia, cor, acessibilidade, coerência física, small-size legibility e contexto de uso.
7. Quando a base estiver boa, prefira edição localizada a regeneração integral.
8. Tema e decoração não podem descaracterizar a **ADEGA DOS 7**.

## Gestão de assets

PNG, JPG, JPEG, WEBP e GIF são binários. Nunca os grave usando operação documentada como UTF-8/texto.

Para qualquer asset novo ou substituído:

- valide fonte, formato, dimensões, tamanho e decodificação;
- calcule SHA-256 quando possível;
- preserve bytes quando o objetivo for apenas versionamento/upload;
- valide o remoto após o push;
- não considere um commit como prova de integridade.

Não use `final`, `v2`, `definitivo` etc. no nome do asset. O Git é o histórico.

## Memória e provenance

Siga `.agents/rules/memory-and-context.md`.

- decisões duráveis precisam de fonte/evidência e data de validação;
- não persista transcrições de conversa, secrets ou raciocínio privado;
- estado transitório pertence a `.agents/runs/`;
- provenance de uma arte pertence a `docs/assets/`;
- fatos públicos não verificáveis não devem virar claims do repositório.

## Supply chain de agentes

Antes de incorporar skill, MCP, plugin, hook, custom agent, extensão, harness ou prompt pack externo, siga `.agents/rules/agent-asset-supply-chain.md` e `.agents/skills/agent-asset-vetting/SKILL.md`.

Rankings, stars e installs são sinais de descoberta, não autorização. Prefira `ADAPT` quando apenas princípios arquiteturais forem úteis.

## Gates humanos

Siga `.agents/rules/change-promotion.md`.

Exigem aprovação humana explícita, entre outros:

- mudança de invariantes da marca;
- substituição de asset aprovado;
- novo logo primário;
- remoção destrutiva de asset oficial;
- incorporação de asset externo de agente;
- mudança material no significado público da marca.

## Pull requests e evidência de conclusão

Preferir Conventional Commits. PRs e relatórios finais devem cobrir objetivo, arquivos, checks executados/não executados, requisitos, impacto de marca/design, integridade de assets, provenance, rollback e riscos.

Use `.agents/rules/completion-and-evidence.md`. Em tarefas rastreadas, `DONE` exige evidência concreta.

## Atalhos proibidos

Não:

- redesenhe elemento aprovado sem necessidade;
- invente texto, símbolo ou claim;
- aceite objeto funcional duplicado ou conexão impossível;
- use API textual para gravar binário;
- esconda falha de validação;
- instale asset externo sem vetting;
- transforme informação não verificada em fato;
- mantenha fontes de instrução concorrentes e divergentes.
