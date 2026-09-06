# AGENTS.md

## Missão do repositório

Este repositório é a fonte de verdade para a identidade visual da **Adega dos 7**, suas variações temáticas e o processo usado para concebê-las, validá-las e versioná-las.

## Antes de trabalhar

Leia apenas o necessário para a tarefa:

- identidade e princípios visuais: `docs/design-system.md`;
- construção de uma arte do briefing ao arquivo final: `docs/image-construction-workflow.md`;
- prompt mestre: `docs/image-generation-prompt.md`;
- arquivos binários, upload e validação: `docs/asset-management.md`;
- referências e decisões de arquitetura de agentes: `docs/references.md`.

Para tarefas de criação/adaptação de imagens, carregue também a skill `.github/skills/image-production/SKILL.md` quando o ambiente oferecer Agent Skills.

## Regras permanentes

1. **Reconhecimento da marca primeiro; tema depois.** Não redesenhe elementos aprovados sem necessidade explícita.
2. Não pule do briefing para a arte final. Produza primeiro um **Design Packet**/blueprint conforme `docs/image-construction-workflow.md`.
3. Modele objetos funcionais e suas conexões antes da geração. Não aceite mangueiras, cabos, piteiras, alças ou peças duplicadas/sem origem lógica.
4. Texto em imagem deve reproduzir exatamente a grafia solicitada. Não invente slogans, símbolos, estrelas ou palavras.
5. Revise composição, hierarquia, tipografia, cor, acessibilidade, coerência física, uso em diferentes tamanhos e produção/exportação.
6. PNG/JPG/WEBP/GIF são binários. Nunca os grave usando operações documentadas como UTF-8/texto.
7. Para qualquer arquivo visual novo ou substituído, valide o arquivo fonte e o remoto. Um commit criado não prova integridade.
8. Não use nomes `final`, `v2`, `definitivo` etc. O Git é o histórico de versões.
9. O README deve refletir apenas arquivos realmente presentes na `main`.
10. Mudanças de documentação/configuração devem ser coerentes entre si, sem duplicar grandes blocos de regras. Prefira links para a fonte de verdade.

## Ciclo de trabalho obrigatório

```text
ENTENDER → BLUEPRINT → PRODUZIR → REVISAR → VALIDAR → CORRIGIR → REVALIDAR → VERSIONAR → VALIDAR REMOTO
```

## Critérios bloqueadores

Uma arte não pode ser considerada pronta se houver qualquer um destes problemas:

- nome/texto incorreto;
- elemento obrigatório ausente;
- objeto funcional duplicado sem intenção;
- conexão física impossível ou ambígua;
- corte acidental de elemento importante;
- associação cromática que contradiga o tema/briefing;
- identidade descaracterizada;
- arquivo truncado, corrompido ou não decodificável;
- validação remota não realizada quando houve upload/substituição.

## Validação técnica

Quando houver alterações em `assets/`, execute:

```bash
python scripts/validate_assets.py
```

Se o ambiente não puder executar o script, realize verificações equivalentes e documente a limitação.
