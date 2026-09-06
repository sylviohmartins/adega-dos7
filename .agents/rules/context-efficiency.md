# Eficiência de contexto

Agentes devem usar progressive disclosure para evitar contexto excessivo e divergência entre fontes.

## Ordem recomendada

1. leia `AGENTS.md`;
2. leia o arquivo específico mais próximo do escopo da tarefa;
3. carregue regras em `.agents/rules/` apenas quando aplicáveis;
4. carregue a skill adequada em `.agents/skills/`;
5. abra documentação extensa em `docs/` somente conforme necessário;
6. consulte provenance de assets apenas quando a tarefa tocar aquela arte.

## Regras

- Não pré-carregue todas as skills.
- Não copie documentação longa para prompts ou adaptadores.
- Preserve dados exatos de falhas, hashes, dimensões e evidências; resuma saídas repetitivas de sucesso.
- Para tarefas longas, persista estado estruturado em `.agents/runs/` em vez de depender da memória da conversa.
- Use subagentes somente quando houver trabalho independente, paralelizável ou que se beneficie de contexto isolado.
- Para tarefas simples, prefira execução direta e sequencial.

O objetivo é manter contexto suficiente para decisões corretas sem transformar cada interação em um carregamento integral do repositório.
