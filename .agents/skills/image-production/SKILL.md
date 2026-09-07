---
name: image-production
description: Planeja, constrói, revisa e valida imagens e variações da identidade visual da ADEGA DOS 7. Use para criar ou adaptar qualquer arte, tema sazonal, campanha, logo ou peça visual do briefing ao arquivo final.
---

# Image Production

## Objetivo

Transformar um briefing em arte coerente, rastreável e verificável sem pular diretamente para a geração final.

## Fontes de verdade

Carregue conforme necessário:

- `../../../docs/design-system.md`;
- `../../../docs/image-construction-workflow.md`;
- `../../../docs/image-generation-prompt.md`;
- `../../../docs/asset-management.md`;
- `../../../.agents/rules/brand-integrity.md`.

## Fluxo

### 1. Entender

Extraia objetivo, público/contexto, tema, referências, invariantes, variáveis, elementos obrigatórios/proibidos, texto exato, formato e canais de uso.

### 2. Definir direção criativa

Antes do layout final, traduza o tema para uma filosofia visual curta: atmosfera, materiais, luz, ritmo, cor e nível de ornamentação. Para variações da marca, essa direção deve ser subordinada à identidade da **ADEGA DOS 7**.

Em um logo sazonal, escreva antes da geração um contrato de transformação interna:

- `PRESERVAR`: contorno, lettering, garrafa/7, narguilé/rosh, fumaça característica, uma mangueira com uma piteira e os arcos estruturais na mesma quantidade, raio e posição;
- `LIMPAR`: tracinhos laterais, raios, barras, ornamentos de rótulo e padrões internos herdados que não sejam estruturais;
- `RECONSTRUIR`: miolo, cores, materiais e ornamentos que comunicarão o novo tema;
- `LIMITE`: nenhuma extensão temática fora do emblema sem autorização explícita.

O tratamento deve ser uma reconstrução interna orientada por pesquisa do tema, não uma camada de enfeites copiada de outra versão sazonal.

### 3. Construir Design Packet

Produza:

1. brief resumido;
2. invariantes vs. variáveis;
3. hierarquia P1/P2/P3/P4;
4. mapa/topologia de objetos e conexões;
5. blueprint do canvas com safe areas e centro óptico;
6. estudo de valores claro/escuro;
7. paleta e materiais;
8. tipografia e texto exato;
9. negative space e densidade;
10. associações indesejadas;
11. regras negativas;
12. mapa `PRESERVAR / LIMPAR / RECONSTRUIR / LIMITE`;
13. critérios de aceite.

Use ASCII/wireframe quando ajudar. O blueprint é uma planta, não a arte final.

### 4. Montar prompt de produção

Use `../../../docs/image-generation-prompt.md` como base. Deixe explícitos referência, composição, hierarquia, relações físicas, texto, paleta, materiais, elementos proibidos, tolerâncias e critérios de rejeição.

### 5. Tratar a primeira saída como rascunho

Nunca considere a primeira renderização final por padrão. Revise:

- identidade/branding;
- hierarquia e composição;
- topologia e coerência física;
- tipografia;
- cor/contraste;
- acessibilidade/legibilidade;
- anomalias típicas de IA;
- adequação ao canal;
- acabamento e produção.

Para uma variação sazonal, confira também a contagem/posição dos arcos, a remoção do resíduo interno e a autenticidade do código visual do tema. Não aprove uma arte que apenas adiciona decoração mantendo o miolo anterior.

### 6. Corrigir conservadoramente

Quando a base estiver boa, prefira edição localizada. Especifique o que remover, reconstruir, preservar e como validar. Não regenere toda a arte para corrigir um defeito localizado sem necessidade.

### 7. Fazer segunda passagem deliberada

Refine alinhamento, proporções, ruído, contraste e materialidade antes de adicionar novos elementos. Melhorar qualidade normalmente significa remover ambiguidade e polir o que já existe, não acumular decoração.

### 8. Testar contexto

Quando aplicável, confira thumbnail/avatar, feed social, fundo claro/escuro, impressão, recorte seguro e leitura sem depender exclusivamente da cor.

### 9. Exportar e versionar

Siga `../../../docs/asset-management.md`, execute `python scripts/validate_assets.py` quando houver asset e valide o remoto após push.

## Bloqueadores

Rejeite se houver texto incorreto, elemento obrigatório ausente, duplicação funcional não solicitada, conexão impossível/ambígua, foco incorreto, perda de identidade, associação temática errada, corte relevante ou arquivo inválido/truncado.

## Princípio

**RECOGNITION FIRST. THEME SECOND. CRAFT THIRD. DECORATION LAST.**
