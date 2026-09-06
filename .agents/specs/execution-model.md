# Modelo de execução orientado por GitHub

## Objetivo

Usar agentes de IA, GitHub e GitHub Actions como um loop verificável para evolução da identidade visual da **ADEGA DOS 7**.

## Máquina de estados

`DISCOVER -> PLAN -> BRANCH -> CHANGE -> PULL_REQUEST -> VALIDATE -> DIAGNOSE -> REVISE -> REVIEW -> PROMOTION_DECISION`

Para criação visual, `CHANGE` contém um subfluxo obrigatório:

`BRIEF -> DESIGN_PACKET -> PRODUCTION_PROMPT -> DRAFT -> DESIGN_QA -> CONSERVATIVE_EDIT -> CONTEXT_TESTS -> EXPORT`

## Sequência

1. **Discover** — leia `AGENTS.md`, regras aplicáveis, estado atual do repositório, referências e provenance relevante.
2. **Plan** — defina objetivo observável, invariantes, variáveis, riscos, critérios de aceite e validação.
3. **Branch** — trabalhe fora de `main`.
4. **Change** — faça a menor mudança completa que entrega o objetivo.
5. **Pull request** — abra PR para tornar checks e review parte do feedback.
6. **Validate** — execute validação técnica e de política; para assets, valide também dimensões, estrutura e hashes.
7. **Diagnose** — investigue o erro exato; não deduza causa apenas pelo status vermelho.
8. **Revise** — corrija a causa raiz sem enfraquecer critérios.
9. **Review** — use lentes de marca, design, coerência física, acessibilidade, produção e provenance.
10. **Promotion decision** — aplique `.agents/rules/change-promotion.md`.

## Paralelismo

Use subagentes ou trabalho paralelo apenas para frentes independentes, como pesquisa temática, auditoria de acessibilidade e revisão de provenance. Integração final deve ser revalidada como um todo.

## Política de falha

- Não silencie checks para obter CI verde.
- Não declare validação não executada como aprovada.
- Não substitua evidência por impressão visual vaga.
- Se o ambiente não puder executar um check, registre a limitação e faça a melhor verificação equivalente disponível.

## Eficiência

Prefira contexto progressivo, passos reversíveis, PRs pequenos, evidências estruturadas e revisão localizada. Para uma base visual já aprovada, prefira edição conservadora a regeneração integral.
