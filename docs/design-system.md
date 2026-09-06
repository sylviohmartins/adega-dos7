# Sistema de design visual — ADEGA DOS 7

Este documento organiza as disciplinas de design que devem ser consideradas na criação, revisão e adaptação das artes da **ADEGA DOS 7**. Ele não substitui o julgamento de um designer; funciona como checklist e fonte de critérios para agentes e colaboradores.

## 1. Brand strategy e identidade visual

Objetivo: preservar reconhecimento e consistência ao longo de campanhas e temas.

Fonte de verdade: `assets/logos/original.png` é a identidade-base permanente. Uma peça sazonal, como `assets/logos/natal-2026.png`, deve ser construída como derivação controlada desse master, sem redefinir garrafa, número 7, lettering, narguilé, mangueira, molduras ou lógica cromática principal.

Perguntas de controle:

- A arte ainda é imediatamente reconhecível como **ADEGA DOS 7**?
- Quais elementos são invariantes da marca?
- O tema está complementando ou competindo com a identidade?
- A peça continua coerente quando comparada lado a lado com outras versões?

Princípio:

> **Recognition first. Theme second.**

## 2. Direção de arte

Objetivo: transformar o briefing em uma linguagem visual unificada.

Definir antes da produção:

- atmosfera;
- época/tema;
- materiais;
- nível de sofisticação;
- iluminação;
- densidade de detalhes;
- referências culturais;
- nível de realismo/ilustração;
- regras de ornamento.

Evitar misturar estilos que não tenham uma intenção clara.

## 3. Composição, grid e equilíbrio

Objetivo: criar leitura organizada e previsível.

Avaliar:

- centro óptico;
- massa visual esquerda/direita;
- equilíbrio entre topo, centro e base;
- relações de escala;
- margens e safe areas;
- sobreposição entre elementos;
- fluxo de leitura;
- simetria ou assimetria intencional;
- respiro suficiente entre objetos.

Antes da cor, a composição deve funcionar em blocos simples de claro/escuro.

## 4. Hierarquia visual

Objetivo: deixar evidente onde olhar primeiro, segundo e terceiro.

Use tamanho, contraste, peso, posição, cor, proximidade e agrupamento para estabelecer prioridade.

Para o logo da **ADEGA DOS 7**, uma ordem típica pode ser:

1. assinatura/número **7** e garrafa central;
2. nome **ADEGA DOS**;
3. narguilé e mangueira;
4. ornamentos e tema sazonal.

A ordem pode mudar conforme o briefing, mas nunca por acidente.

## 5. Tipografia

Objetivo: manter legibilidade e identidade.

Regras:

- reproduzir texto exatamente;
- limitar variedade tipográfica;
- preservar hierarquia por escala/peso;
- evitar fontes finas demais em tamanho pequeno;
- testar leitura em thumbnail;
- evitar deformação, letras inventadas e kerning inconsistente;
- não adicionar texto decorativo não solicitado.

Em logos, a forma tipográfica pode ser parte essencial da identidade e deve ser preservada quando a referência exigir.

## 6. Cor e materiais

Objetivo: comunicar tema e marca sem gerar associações acidentais.

Avaliar:

- cor dominante;
- cores de apoio;
- highlights;
- equilíbrio quente/frio;
- contraste;
- saturação;
- associação cultural;
- compatibilidade com fundo e canal;
- materiais (metal, vidro, madeira, papel, tecido etc.).

Não depender apenas de cor para comunicar uma informação importante. Quando necessário, use também forma, contraste, textura ou posição.

## 7. UX aplicada à identidade visual

Mesmo uma imagem estática participa de uma experiência de uso.

Perguntas:

- O usuário reconhece a marca em poucos segundos?
- O significado principal sobrevive em 64–128 px?
- Há excesso de detalhe que só funciona em zoom?
- O logo funciona como avatar circular/quadrado?
- Elementos importantes ficam fora da safe area de recortes sociais?
- A leitura continua clara sobre fundo escuro e claro quando houver variantes?
- O tema é entendido sem precisar de explicação textual?

## 8. UI e apresentação digital

Quando a arte for aplicada em interface:

- preserve contraste entre imagem e controles;
- não coloque detalhes importantes onde overlays costumam aparecer;
- respeite áreas de avatar, cabeçalho e cards;
- evite texto minúsculo rasterizado;
- forneça alt text quando a imagem for publicada em web/app;
- prefira texto real de interface fora da imagem quando não for parte essencial do logo.

## 9. Acessibilidade e inclusive design

Objetivo: tornar a comunicação perceptível em diferentes condições de visão e contexto.

Boas práticas:

- manter contraste suficiente para texto funcional e UI;
- evitar depender exclusivamente de vermelho/verde para diferenciação;
- testar leitura em escala pequena;
- verificar versão em tons de cinza quando útil;
- fornecer descrição textual/alt text para publicação digital;
- tratar texto incorporado ao logo como identidade, mas evitar imagens de texto para conteúdo informativo que poderia ser texto real.

## 10. Ilustração, iconografia e coerência física

Objetivo: evitar artefatos típicos de IA.

Modele objetos e relações antes de gerar.

Para cada objeto funcional, responda:

- o que é?
- quantas unidades existem?
- de onde sai?
- onde termina?
- qual peça conecta a qual?
- está na frente ou atrás de quê?

Exemplo:

```text
NARGUILÉ
  └── 1 saída
       └── 1 mangueira contínua
            └── 1 piteira final
```

Se a imagem mostrar duas mangueiras ou piteiras sem que o briefing peça isso, é uma anomalia.

## 11. Social media design

Avaliar a arte nos cenários reais de uso:

- avatar;
- post quadrado;
- feed 4:5;
- story/reel 9:16;
- thumbnail;
- fundo da interface do Instagram;
- compressão e redução de tamanho.

A master não deve ser deformada para cada canal; crie derivados quando necessário.

## 12. Print, embalagem e produção

Quando houver uso físico:

- verificar resolução suficiente;
- considerar sangria e área segura;
- evitar detalhes menores que a capacidade do processo de impressão;
- prever comportamento de dourado/metálico quando ele for apenas simulado em RGB;
- diferenciar arquivo master digital de arquivo preparado para gráfica;
- não assumir que aparência em tela será idêntica à impressão.

## 13. Design QA

### Bloqueadores

Rejeitar a arte se houver:

- texto/nome incorreto;
- identidade irreconhecível;
- objeto obrigatório ausente;
- duplicação funcional não prevista;
- conexão física impossível;
- corte acidental grave;
- tema confundido com outro contexto;
- arquivo corrompido/truncado.

### Importantes

Corrigir antes de aprovação final:

- hierarquia fraca;
- excesso de ruído;
- contraste insuficiente;
- ornamentos competindo com a marca;
- leitura ruim em tamanho pequeno;
- paleta desequilibrada;
- geometria ou perspectiva inconsistente.

### Polimento

Ajustar quando necessário:

- pequenos reflexos;
- microalinhamentos;
- espaçamento;
- uniformidade de textura;
- brilho e acabamento.

## 14. Rubrica de avaliação sugerida

Para adaptações de marca:

| Critério | Peso |
| --- | ---: |
| Reconhecimento da marca | 25% |
| Coerência estrutural/semântica | 20% |
| Hierarquia e composição | 15% |
| Tradução do tema | 15% |
| Tipografia | 10% |
| Cor/contraste | 10% |
| Produção e contexto de uso | 5% |

A pontuação não substitui os bloqueadores: qualquer bloqueador reprova a arte mesmo com média alta.
