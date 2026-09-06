# Gestão segura de arquivos de identidade visual

Este documento define o fluxo recomendado para adicionar, substituir e validar logos e outras imagens no repositório sem perda de qualidade, corrupção ou truncamento.

## Princípios

1. **Preservar o arquivo fonte**: o master deve ser armazenado sem alterações involuntárias de resolução, compressão, perfil de cor ou metadados relevantes.
2. **Tratar imagens raster como binário**: PNG, JPG, JPEG, WEBP e GIF nunca devem ser manipulados como UTF-8 ou texto.
3. **Validar antes e depois do commit**: presença no Git não é suficiente; tamanho, formato e integridade precisam ser conferidos.
4. **Git controla revisões**: evitar sufixos como `final`, `final2`, `v3` ou `definitivo`. O histórico do repositório é a fonte de verdade das revisões.
5. **Separar master de derivados quando necessário**: versões comprimidas para redes sociais ou web não devem substituir o master de maior qualidade.

## Convenção de nomes

Para variações sazonais:

```text
<tema>-<ano>.<extensão>
```

Exemplos:

```text
natal-2026.png
copa-2026.png
ano-novo-2027.png
carnaval-2027.png
```

Para a identidade-base:

```text
original.png
```

Usar nomes em minúsculas, sem espaços e com hífen como separador.

## Linhagem entre master e variações

O arquivo `assets/logos/original.png` é o master canônico da marca. Arquivos sazonais, como `assets/logos/natal-2026.png`, são derivados do master e não devem ser tratados como sua fonte de identidade.

```text
original.png  →  camada temática controlada  →  <tema>-<ano>.png
```

Ao criar uma nova variação, não altere o master para acomodar o tema. Registre no provenance quais invariantes foram preservados e quais variáveis foram adicionadas.

## Fluxo seguro para arquivos binários

### 1. Validar o arquivo fonte

Antes do upload, confirmar pelo menos:

- tipo real do arquivo;
- dimensões;
- proporção;
- tamanho em bytes;
- capacidade de decodificação completa;
- SHA-256.

Exemplo em ambiente Unix:

```bash
file assets/logos/original.png
sha256sum assets/logos/original.png
file assets/logos/natal-2026.png
sha256sum assets/logos/natal-2026.png
```

Com ImageMagick disponível:

```bash
identify assets/logos/natal-2026.png
```

Também é válido usar Pillow ou outra biblioteca confiável para validar largura, altura e decodificação completa.

### 2. Fazer o upload sem conversão textual

Métodos preferidos, em ordem prática:

1. Git normal (`git add`, `git commit`, `git push`) usando o arquivo binário real;
2. Codex ou outro ambiente com acesso ao filesystem e ao repositório;
3. upload manual pela interface do GitHub;
4. GitHub Git Data API usando um blob com **Base64 completo**, somente quando a ferramenta utilizada consegue transportar e validar o payload inteiro sem truncamento.

### 3. O que não fazer

Nunca:

- usar uma ação documentada como criação/edição de **arquivo UTF-8** para gravar PNG/JPG;
- inserir Base64 como texto dentro de um arquivo `.png`;
- enviar Base64 parcial;
- reconstruir o arquivo a partir de screenshot ou preview;
- aplicar OCR a uma imagem apenas para transportá-la;
- reduzir qualidade ou resolução sem requisito explícito;
- considerar o upload concluído apenas porque o commit foi criado.

## Validação pós-upload

Após o commit/push:

1. confirmar que o caminho remoto existe;
2. conferir o tamanho remoto em bytes;
3. abrir o preview completo;
4. baixar o arquivo remoto quando possível;
5. comparar o SHA-256 remoto com o arquivo fonte;
6. confirmar que dimensões e formato continuam os mesmos.

Quando não for possível calcular SHA-256 remoto pela integração usada, ao menos validar tamanho, blob SHA do Git, preview completo e download manual.

## Particularidade do GitHub Connector no ChatGPT

Algumas ações do conector GitHub são wrappers específicos para **conteúdo UTF-8** (`create_file` / `update_file`). Essas ações são adequadas para Markdown, JSON, YAML e código, mas não devem ser usadas para PNG/JPG.

Para binários, só é seguro usar a operação de blob quando o conteúdo Base64 completo puder ser entregue sem truncamento e depois validado. Se a ferramenta não oferecer essa garantia, usar Git/Codex ou upload manual.

## `.gitattributes`

O repositório declara imagens raster como `binary`, evitando normalização de fim de linha, merges textuais e diffs inadequados.

## Política de Git LFS

Git LFS não é necessário apenas porque um PNG possui alguns megabytes. Adotar LFS quando o volume de binários grandes começar a impactar significativamente clone, histórico ou armazenamento. Não migrar arquivos existentes para LFS sem necessidade e planejamento.

## Checklist de conclusão

- [ ] nome e caminho seguem a convenção;
- [ ] arquivo fonte abre integralmente;
- [ ] formato e dimensões foram validados;
- [ ] hash local foi registrado quando necessário;
- [ ] upload ocorreu como binário real;
- [ ] tamanho remoto é coerente;
- [ ] preview remoto está completo;
- [ ] hash remoto foi comparado quando possível;
- [ ] relação master → variação está documentada;
- [ ] commit descreve a alteração de forma objetiva.
