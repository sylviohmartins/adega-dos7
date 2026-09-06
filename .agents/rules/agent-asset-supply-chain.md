# Supply chain de assets para agentes

Não copie ou instale skill, MCP, plugin, hook, custom agent, prompt pack ou extensão apenas porque é popular.

Use `.agents/skills/agent-asset-vetting/SKILL.md` e registre avaliações relevantes conforme `.agents/schemas/agent-asset-assessment.schema.json`.

Pipeline mínimo:

`DISCOVER -> SOURCE_VERIFY -> LICENSE -> STATIC_REVIEW -> PERMISSIONS -> OVERLAP -> SANDBOX -> BENCHMARK -> DECISION`

Avalie:

1. origem e identidade do mantenedor;
2. licença e obrigações de redistribuição;
3. atividade de manutenção e maturidade;
4. permissões de filesystem, shell, rede, navegador, secrets e contas externas;
5. scripts de instalação, postinstall, downloads dinâmicos e binários;
6. risco de prompt injection, exfiltração, alteração indevida de arquivos ou bypass de políticas;
7. dependências e cadeia transitiva quando houver código executável;
8. sobreposição com capacidades já existentes no repositório;
9. valor incremental demonstrável para o fluxo visual da **ADEGA DOS 7**;
10. possibilidade de adaptar apenas os princípios úteis em vez de vendorizar o asset inteiro.

Classificações:

- `ADOPT`: incorporar após revisão e validação;
- `ADAPT`: usar como referência arquitetural e implementar versão local mínima;
- `TRIAL`: testar isoladamente antes de decisão;
- `REJECT`: não usar por risco, licença, overlap ou baixo valor;
- `SUPERSEDED`: capacidade já atendida localmente.

Stars, downloads, rankings e presença em marketplaces são sinais de descoberta, não autorização.
