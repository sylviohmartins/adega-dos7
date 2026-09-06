# Memória e contexto durável

A memória do repositório existe para preservar conhecimento verificável da **ADEGA DOS 7**, não para arquivar conversas.

## Pode ser persistido

- invariantes de marca aprovados;
- decisões de design com fonte/provenance;
- convenções de nomenclatura;
- limitações técnicas comprovadas;
- decisões de arquitetura de agentes;
- fatos públicos verificados com fonte e data;
- lições operacionais que evitam repetir falhas, como corrupção de binários.

## Não deve ser persistido

- transcrições de chats;
- raciocínio privado de modelos;
- dados pessoais sem necessidade;
- secrets, tokens ou credenciais;
- suposições não validadas;
- estado temporário de uma tarefa em andamento.

## Requisitos de uma memória durável

Cada entrada deve indicar:

- fato/decisão;
- fonte ou evidência;
- data da última validação;
- escopo;
- condição de obsolescência quando aplicável.

Estado transitório pertence a `.agents/runs/`. Provenance específico de uma arte pertence a `docs/assets/`.
