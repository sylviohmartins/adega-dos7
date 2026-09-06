# Prompt mestre universal para geração e adaptação de imagens

Este template foi criado para gerar imagens novas ou adaptar uma identidade visual existente a qualquer tema, mantendo clareza de objetivo, coerência semântica, controle de composição e critérios explícitos de qualidade.

## Como usar

Preencha os campos entre `<...>` e escolha um dos modos:

- **Modo A — criação do zero**: quando não existe uma imagem-base obrigatória;
- **Modo B — adaptação/edição**: quando existe uma referência que deve ser preservada;
- **Modo C — variação temática de marca**: quando a identidade deve permanecer reconhecível e o tema entrar como camada secundária.

Para a identidade da **ADEGA DOS 7**, o Modo C parte de `assets/logos/original.png`, que é a matriz canônica. Um arquivo como `assets/logos/natal-2026.png` é saída temática derivada; nunca use uma variação sazonal como fonte para redefinir a identidade-base.

---

## PROMPT MESTRE

### 0. PAPEL

Atue como diretor de arte, designer de identidade visual, ilustrador e revisor de qualidade visual.

Sua tarefa é produzir uma imagem profissional, visualmente coerente e tecnicamente limpa, evitando objetos sem função, duplicações, deformações, texto incorreto e elementos que não façam sentido físico ou semântico.

### 1. MODO DE EXECUÇÃO

Modo: `<A | B | C>`

- **A — criar do zero**: use apenas a descrição e as referências conceituais fornecidas.
- **B — editar/adaptar imagem existente**: trate a imagem-base como fonte principal e altere somente o que for solicitado.
- **C — adaptar identidade a um tema**: preserve primeiro o reconhecimento da marca; aplique o tema depois, de forma integrada e controlada.

### 2. OBJETIVO

Criar `<tipo de imagem>` com o tema `<tema>` para `<finalidade/canal>`.

A imagem deve comunicar imediatamente:

- `<mensagem principal>`;
- `<sensação desejada>`;
- `<elementos indispensáveis>`.

### 3. CONTEXTO E REFERÊNCIAS

Referência visual principal: `<imagem ou descrição>`

Referências secundárias: `<opcional>`

Se houver uma imagem-base obrigatória:

- preserve composição, proporções, elementos-chave e identidade, salvo instrução contrária;
- não redesenhe elementos aprovados sem necessidade;
- não invente detalhes que conflitem com a referência;
- trate a referência como fonte de verdade visual.

Quando a referência for a identidade-base da **ADEGA DOS 7**, registre explicitamente o caminho do master, o hash disponível e a separação entre invariantes permanentes e camada temática variável.

### 4. HIERARQUIA VISUAL

Prioridade 1: `<elemento principal>`

Prioridade 2: `<elemento secundário>`

Prioridade 3: `<elementos de apoio>`

O elemento principal deve dominar a leitura. Elementos temáticos e decorativos nunca devem competir com o foco central.

### 5. COMPOSIÇÃO

Formato: `<1:1 | 4:5 | 9:16 | 16:9 | outro>`

Enquadramento: `<centralizado | close-up | plano aberto | outro>`

Estrutura: `<simétrica | assimétrica | circular | editorial | cinematográfica | outro>`

Espaço negativo: `<baixo | médio | alto>`

Margens e áreas de segurança: `<definir quando necessário>`

Evite cortes acidentais, tangências ruins, objetos fundidos e elementos sem origem clara.

### 6. ELEMENTOS OBRIGATÓRIOS

Incluir exatamente:

- `<elemento 1>`;
- `<elemento 2>`;
- `<elemento 3>`.

Para objetos conectados ou funcionais, respeitar lógica física e estrutural.

Exemplos de validação:

- um narguilé com uma única saída deve ter uma única mangueira e uma única piteira;
- cabos devem conectar-se a pontos plausíveis;
- alças, braços, rodas, garrafas, bocais e acessórios não devem aparecer duplicados sem intenção;
- objetos não devem surgir do nada nem atravessar outros objetos de forma impossível.

### 7. ELEMENTOS PROIBIDOS

Não incluir:

- `<elementos proibidos específicos>`;
- objetos duplicados sem função;
- texto aleatório;
- símbolos inventados;
- ornamentos excessivos;
- deformações anatômicas ou geométricas;
- peças flutuantes;
- conexões fisicamente incoerentes;
- detalhes genéricos que descaracterizem a identidade.

### 8. TEMA

Tema principal: `<tema>`

Traduzir o tema por meio de:

- paleta;
- materiais;
- iluminação;
- textura;
- ornamentos;
- atmosfera;
- contexto visual.

Evite depender de texto para explicar o tema quando a direção de arte puder comunicá-lo visualmente.

Para adaptações de marca:

> Recognition first. Theme second.

### 9. PALETA E MATERIAIS

Paleta principal:

- `<cor 1>`;
- `<cor 2>`;
- `<cor 3>`.

Cores de apoio: `<opcional>`

Materiais/acabamentos: `<dourado metálico, vidro, madeira, tecido, papel, aço, etc.>`

Evite combinações cromáticas que remetam acidentalmente a outro tema, marca, país, evento ou campanha não desejada.

### 10. ILUMINAÇÃO E ATMOSFERA

Iluminação: `<soft studio | cinematic | warm | dramatic | daylight | etc.>`

Contraste: `<baixo | médio | alto>`

Atmosfera: `<premium | clean | vintage | futurista | festiva | editorial | etc.>`

### 11. ESTILO VISUAL

Direção estética:

`<palavras-chave de estilo>`

Exemplo:

`premium branding, sophisticated emblem, detailed vector-style illustration, metallic accents, controlled highlights, high contrast, production-quality artwork`

### 12. TIPOGRAFIA E TEXTO

Texto obrigatório: `<texto exato>`

Texto opcional: `<texto opcional ou NENHUM>`

Regras:

- reproduzir exatamente a grafia solicitada;
- não inventar palavras;
- não adicionar slogan não solicitado;
- preservar hierarquia e legibilidade;
- se não houver texto solicitado, não gerar texto decorativo.

### 13. QUALIDADE E SAÍDA

Resultado esperado:

- alta resolução;
- bordas limpas;
- detalhes nítidos;
- composição equilibrada;
- aparência profissional;
- sem artefatos de geração;
- sem elementos truncados;
- pronto para `<uso pretendido>`.

### 14. CHECKLIST DE COERÊNCIA ANTES DE FINALIZAR

Revise silenciosamente a imagem e corrija qualquer falha antes de concluir:

1. O tema está evidente sem dominar o assunto principal?
2. O foco visual está correto?
3. Todos os objetos obrigatórios existem?
4. Existe algum objeto duplicado sem motivo?
5. Toda mangueira, cabo, alça ou conexão possui origem e destino claros?
6. Há peças flutuantes ou formas fundidas de maneira impossível?
7. O texto está exatamente correto?
8. Há símbolos, estrelas, ornamentos ou palavras que não foram solicitados?
9. A paleta comunica o tema correto e evita associações indesejadas?
10. A imagem mantém a identidade da referência quando aplicável?
11. O enquadramento está completo e sem cortes acidentais?
12. O resultado parece uma decisão de design intencional, e não uma colagem de elementos gerados pela IA?

### 15. CRITÉRIO DE SUCESSO

O resultado será considerado aprovado somente se, ao primeiro olhar, uma pessoa entender:

> `<frase que resume a percepção desejada>`

Sem precisar explicar elementos incoerentes, excessivos ou ambíguos.

---

## Versão compacta

```text
Use <referência, se houver> como referência visual principal.

Crie/edite uma imagem de <tipo> com tema <tema>, destinada a <uso>.

Preserve obrigatoriamente: <elementos/identidade>.
Inclua exatamente: <elementos obrigatórios>.
Não inclua: <elementos proibidos>.

Hierarquia: <principal> > <secundário> > <apoio>.
Formato: <proporção>.
Composição: <descrição>.
Paleta: <cores>.
Materiais: <acabamentos>.
Iluminação: <tipo>.
Estilo: <direção estética>.
Texto exato: <texto ou NENHUM>.

Garanta coerência física e semântica: não duplique objetos, não crie peças flutuantes, mantenha conexões claras entre componentes e não invente texto ou símbolos. Revise e corrija anomalias antes de finalizar.

Critério de sucesso: <percepção desejada>.
High-resolution, production-quality, clean edges, coherent details, professional finish.
```

## Regra para identidade de marca

Quando houver uma marca ou logo já aprovado:

```text
Preserve recognition first. Apply the theme second. Do not redesign what does not need to change.
```
