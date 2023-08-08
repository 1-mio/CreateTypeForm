## Criando um Formulário no Typeform via API

### Estrutura Geral:

- **title**: Título para o formulário.
- **type**: Tipo de formulário.
- **settings**: Especifica as configurações e metadados do formulário.
- **cui_settings**: Especifica as configurações da conversação.
- **theme**: Tema a ser usado no formulário.
- **workspace**: Espaço de trabalho que contém o formulário.
- **hidden**: Array de Campos Ocultos a serem usados no formulário.
- **variables**: Objeto que rastreia a pontuação total ou preço.
- **welcome_screens**: Array de objetos que especificam as configurações da tela de boas-vindas.
- **thankyou_screens**: Array de objetos que especificam as configurações da tela de agradecimento.
- **fields**: Array de objetos que especificam os campos a serem usados no formulário.
- **logic**: Array de objetos Logic Jump a serem usados no formulário.

### Detalhes dos Campos (`fields`):

- **ref**: Nome legível para referenciar o campo.
- **title**: Nome único atribuído ao campo neste formulário.
- **type**: Tipo de campo. Valores válidos incluem: `calendly`, `contact_info`, `date`, `dropdown`, `email`, `file_upload`, `group`, `legal`, `long_text`, `matrix`, `multiple_choice`, `nps`, `number`, `opinion_scale`, `payment`, `phone_number`, `picture_choice`, `ranking`, `rating`, `short_text`, `statement`, `website`, `yes_no`.
- **properties**: Propriedades específicas do campo, como descrição, escolhas, anexos, etc.
- **validations**: Validações para o campo, como se é obrigatório, comprimento máximo, etc.

#### Exemplos de Propriedades de Campos:

1. **Dropdown**:
   - **description**: Descrição para exibir para o campo.
   - **choices**: Escolhas de resposta. Disponível para ranking, dropdown, multiple_choice e picture_choice.
   - **randomize**: Verdadeiro se as opções de resposta devem ser apresentadas em uma nova ordem aleatória para cada respondente.
   - **alphabetical_order**: Verdadeiro se as opções de resposta do dropdown devem ser listadas em ordem alfabética.

2. **Date**:
   - **description**: Descrição para exibir para o campo.
   - **structure**: Formato para mês, data e ano na resposta.
   - **separator**: Caractere a ser usado entre mês, dia e ano na resposta.

3. **Email**:
   - **description**: Descrição para exibir para o campo.

4. **File Upload**:
   - **description**: Descrição para exibir para o campo.

#### Logic Jumps (`logic`):

- **type**: Especifica se o Logic Jump é baseado em um campo de pergunta ou Campo Oculto.
- **ref**: Referência ao campo que aciona o Logic Jump.
- **actions**: Array de objetos que definem o comportamento do Logic Jump.

#### Configurações (`settings`):

- **language**: Idioma a ser usado no formulário.
- **is_public**: Verdadeiro se o formulário é público.
- **progress_bar**: Base para a barra de progresso exibida na tela.
- **show_progress_bar**: Verdadeiro para exibir a barra de progresso no typeform.
- **show_typeform_branding**: Verdadeiro para exibir a marca Typeform no typeform.
- **show_time_to_complete**: Verdadeiro para exibir o tempo estimado para completar um typeform nas telas de boas-vindas.

Estes atributo/propriedades são apenas alguns dos muitos que a API Typeform Create oferece, ela é muito rica em recursos e permite uma personalização detalhada para o forms. [Documentação oficial](https://www.typeform.com/developers/create/reference/create-form/) 