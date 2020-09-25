# Boas vindas ao repositório do projeto TING(Trybe is not Google)!

Você já usa o GitHub diariamente para desenvolver os exercícios, certo? Agora, para desenvolver os projetos, você deverá seguir as instruções a seguir. Fique atento a cada passo, e se tiver qualquer dúvida, nos envie por _Slack_! #vqv 🚀

Aqui você vai encontrar os detalhes de como estruturar o desenvolvimento do seu projeto a partir desse repositório, utilizando uma branch específica e um _Pull Request_ para colocar seus códigos.

---

## Instruções para entregar seu projeto:

### ANTES DE COMEÇAR A DESENVOLVER:

1. Clone o repositório

- `git clone git@github.com:tryber/sd-0x-ting.git`.
- Entre na pasta do repositório que você acabou de clonar:
  - `sd-0x-ting`

2. Crie o ambiente virtual para o projeto

- `python3 -m venv .venv && source .venv/bin/activate`

3. Instale as dependências

- `python3 -m pip install -r requirements.txt`

4. Crie uma branch a partir da branch `main`

- Verifique que você está na branch `main`
  - Exemplo: `git branch`
- Se não estiver, mude para a branch `main`
  - Exemplo: `git checkout main`
- Agora crie uma branch à qual você vai submeter os `commits` do seu projeto
  - Você deve criar uma branch no seguinte formato: `nome-github-nome-do-projeto`
  - Exemplo: `git checkout -b exemplo-ting`

5. Adicione as mudanças ao _stage_ do Git e faça um `commit`

- Verifique que as mudanças ainda não estão no _stage_
  - Exemplo: `git status` (deve aparecer listada a pasta _exemplo_ em vermelho)
- Adicione o novo arquivo ao _stage_ do Git
  - Exemplo:
    - `git add .` (adicionando todas as mudanças - _que estavam em vermelho_ - ao stage do Git)
    - `git status` (deve aparecer listado o arquivo _exemplo/README.md_ em verde)
- Faça o `commit` inicial
  - Exemplo:
    - `git commit -m 'iniciando o projeto ting'` (fazendo o primeiro commit)
    - `git status` (deve aparecer uma mensagem tipo _nothing to commit_ )

6. Adicione a sua branch com o novo `commit` ao repositório remoto

- Usando o exemplo anterior: `git push -u origin exemplo-project-name`

7. Crie um novo `Pull Request` _(PR)_

- Vá até a página de _Pull Requests_ do [repositório no GitHub](https://github.com/tryber/sd-0x-ting/pulls)
- Clique no botão verde _"New pull request"_
- Clique na caixa de seleção _"Compare"_ e escolha a sua branch **com atenção**
- Clique no botão verde _"Create pull request"_
- Adicione uma descrição para o _Pull Request_ e clique no botão verde _"Create pull request"_
- **Não se preocupe em preencher mais nada por enquanto!**
- Volte até a [página de _Pull Requests_ do repositório](https://github.com/tryber/sd-0x-ting/pulls) e confira que o seu _Pull Request_ está criado

---

## Entregáveis

Para entregar o seu projeto você deverá criar um _Pull Request_ neste repositório. Este _Pull Request_ deverá conter os arquivos apresentados na sessão: [Desenvolvimento e testes](#desenvolvimento-e-testes).

Lembre-se que você pode consultar nosso conteúdo sobre [Git & GitHub](https://app.betrybe.com/course/fundamentals/git) sempre que precisar!

---

## O que deverá ser desenvolvido

A `Trybe` lhe convida para implementar um programa que simule o algoritmo de indexação de documentos similar ao do google. Ou seja, um programa que permita anexar arquivos de texto e posteriormente opere funções de busca sobre tais arquivos

> Com a quantidade de informações disponíveis na Web, encontrar o que você precisa seria quase impossível sem nenhuma ajuda para classificá-las. Os sistemas de classificação do Google organizam centenas de bilhões de páginas da Web, no índice da pesquisa, para fornecer os resultados mais úteis e relevantes em uma fração de segundo. Além disso tudo, a a Google também precisa se preocupar em apresentar os resultados de uma maneira que ajude você a encontrar o que está procurando com mais facilidade ainda.

#### Analisar palavras

> Compreender o significado da sua pesquisa é crucial para retornarmos boas respostas. Por isso, para encontrar páginas com informações relevantes, nosso primeiro passo é analisar o significado das palavras na consulta de pesquisa. Desenvolvemos modelos linguísticos para decifrar as sequências de palavras que precisamos procurar no índice.

Não iremos nos apegar a análise de significados ou busca por sinônimos. Nosso objetivo será identificar ocorrências de termos em arquivos _TXT_. Neste contexto, devemos criar um programa que permita anexar arquivos de texto e posteriormente operar funções de busca sobre tais arquivos.

Sendo assim o programa deverá possuir dois módulos:

- Modo gerenciamento de arquivos;

- Modo de buscas.

---

## Desenvolvimento e testes

Este repositório já contém um _template_ com a estrutura de diretórios e arquivos, tanto de código quanto de teste criados. Há também o diretório `statics` que contém os arquivos necessários para realização de testes, caso julgue necessário, sinta-se à vontade para criar novos arquivos ou editar o conteúdo dos arquivos existentes. Veja abaixo:

```md
.
├── statics
│   ├── arquivo_teste.txt
│   ├── novo_paradigma_globalizado.txt
│   └── novo_paradigma_globalizado-min.txt
├── tests
├── ting_file_management
│   ├── file_management.py
│   └── file_process.py
├── ting_word_searches
│   └── word_search.py
├── README.md
├── requirements.txt
└── setup.cfg
```

Apesar do projeto já possuir uma estrutura base, você quem deve implementar tanto as funções quanto os testes (_extra_). Novos arquivos podem ser criados conforme a necessidade.

Para executar os testes, lembre-se de primeiro **criar e ativar o ambiente virtual**, além de também instalar as dependências do projeto. Isso pode ser feito através dos comandos:

```bash
$ python3 -m venv .venv

$ source .venv/bin/activate

$ python3 -m pip install -r requirements.txt
```

O arquivo `requirements.txt` contém todos as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`. Com as dependências já instaladas, para executar os testes basta usar o comando:

```bash
$ python3 -m pytest
```

Se quiser saber mais sobre a instalação de dependências com `pip`, veja esse artigo: https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1

Para verificar se você está seguindo o guia de estilo do Python corretamente, execute o comando:

```bash
$ python3 -m flake8
```

---

## Requisitos obrigatórios:

### Pacote `ting_file_management`

#### 1 - Deve haver uma função `txt_importer` dentro do módulo `file_management` capaz de importar notícias a partir de um arquivo TXT, utilizando "\n" como separador. Todas as mensagens de erro devem ir para a `stderr`.

**Exemplo simples de um arquivo txt a ser importado:**

```md
Acima de tudo,
é fundamental ressaltar que a adoção de políticas descentralizadoras nos obriga
à análise do levantamento das variáveis envolvidas.
```

Ao importar um arquivo, ele será adicionado a uma fila. Com isso, ele deve ganhar um identificador (`posicao`) que representa a posição dele na fila. Ou seja, se importarmos o arquivo `teste1.txt`, ele ficará na posição 1 da fila, assim consecutivamente nos demais arquivos.

##### As seguintes verificações serão feitas:

- Caso o arquivo TXT não exista, deve ser exibida a mensagem: "`Arquivo {path_file} não encontrado`";

- Retorno das informações igual ao exemplo abaixo;

- Caso a extensão do arquivo seja diferente de `.txt`, deve ser exibida uma mensagem: "`Formato inválido`".

#### 2 - Deve haver uma função `process` dentro do módulo `file_process` capaz de ler o arquivo carregado na função anterior e efetuar o preprocessamento do conteúdo.

> Observação: ao processar um novo arquivo na fila, o módulo deve ser capaz de retornar informações relacionadas ao arquivo, sendo elas: `nome do arquivo`, `quantidade de linhas` e a `posição do arquivo` dentro da estrutura. 

**Exemplo de retorno**:

```python
{
    "nome_do_arquivo": "arquivo_teste.txt", # Nome do arquivo recém adicionado
    "qtd_linhas": 3,                        # Quantidade de linhas existentes no arquivo
    "posicao": 1                            # Posição do arquivo dentre os demais arquivos adicionados (iniciando em 1)
}
```

##### As seguintes verificações serão feitas:

- Por padrão deve-se ignorar arquivos com o mesmo nome;

- Não deve haver limites de linhas a serem analisadas;

- Em caso de erros, a importação deve ser interrompida e a posição deve ficar disponível para uma nova inserção;

- O exemplo de saída acima deve ser emitido após cada nova inserção válida, via `stdout`.

#### 3 - Deve haver uma função `remove` dentro do módulo `file_process` capaz de remover o primeiro arquivo processado

> Observação: ao remover um arquivo da fila, o módulo deve ser capaz de decrementar a quantidade de arquivos da estrutura.

##### As seguintes verificações serão feitas:

- Por padrão deve-se ignorar a operação caso não hajam arquivos;

- Em caso de erros, a remoção deve ser interrompida e os itens não devem ser alterados, mantendo a imutabilidade da estrutura;

- Em caso de sucesso de remoção, deve ser emitido a mensagem: "`Arquivo {path_file} removido com sucesso`".

#### 4 - Deve haver uma função `file_metadata` dentro do módulo `file_process` capaz de apresentar as informações superficiais dos arquivos processados.

##### As seguintes verificações serão feitas:

- Baseado na posição informada, deve ser apresentado as informações relacionadas ao arquivo, parecido com o apresentado abaixo;

- Em caso da posição não existir, deve ser exibida uma mensagem de erro: "`Posição inválida`" na `stderr`.

**Exemplo de retorno**:

```python
{
    "nome_do_arquivo": "arquivo_teste.txt",
    "qtd_linhas": 3,
    "posicao": 1
}
```

### Pacote `ting_word_searches`

#### 5 - Deve haver uma função `exists_word` dentro do módulo `word_search`, que valide a existência da palavra em todos os arquivos processados. Para cada palavra encontrada, deve-se listar sua linha conforme apresentação abaixo.

##### As seguintes verificações serão feitas:

- A busca deve ser _case insensitive_ e deve retornar uma lista no formato:

```json
[{
  "palavra": "de",
  "arquivo": "arquivo_teste.txt",
  "ocorrencias": [
    {
      "linha": 1
    },
    {
      "linha": 2
    }
  ]
}]
```

- Caso a palavra não seja encontrada em nenhum arquivo, deve-se retornar uma lista vazia.

#### 6 - Deve haver uma função `search_by_word` dentro do módulo `word_search`, que busque a palavra em todos os arquivos processados. Para cada palavra encontrada, deve-se listar sua linha, o conteúdo e o arquivo da ocorrência.

##### As seguintes verificações serão feitas:

- A busca deve ser _case insensitive_ e deve retornar uma lista no formato:

```json
[{
  "palavra": "de",
  "arquivo": "arquivo_teste.txt",
  "ocorrencias": [
    {
      "linha": 1,
      "conteudo": "Acima de tudo,"
    },
    {
      "linha": 2,
      "conteudo": "é fundamental ressaltar que a adoção de políticas descentralizadoras nos obriga"
    }
  ]
}]
```

- Caso a palavra não seja encontrada em nenhum arquivo, deve-se retornar uma lista vazia.

---

## Requisitos bônus:

#### 7 - Análise assintótica no gerenciamento de arquivos.

##### Pacote `ting_file_management`

##### Qual a complexidade do módulo para as operações:

- Inserção de um novo arquivo

- Remover um arquivo da estrutura 

- Visualizar os metadados de um arquivo pela posição

##### Pacote `ting_word_searches`

##### Qual a complexidade do módulo para as operações:

- Consultar uma palavra com a base de arquivos vazia

- Consultar uma palavra com a base possuindo um arquivo que possui apenas a palavra pesquisada

- Consultar uma palavra com a base possuindo N arquivos, onde a palavra procurada não se encontra presente.

---

## Requisitos extras:

⚠️  Requisitos não serão avaliados ⚠️

### Pacote `ting_menu`

#### 8 - Crie um módulo `menu` que deve ser utilizado como um menu de opções, em que cada opção pede as informações necessárias para disparar uma ação. O texto exibido pelo menu deve ser exatamente:

**Dica**: Utilize o `__main__`.

```md
Selecione uma das opções a seguir:

1 - Módulo gerenciamento de arquivos;
2 - Módulo consulta de palavras;
3 - Sair.
```

##### As seguintes verificações serão feitas:

- A mensagem de menu deve ser exibida corretamente;

- Caso a opção `1` seja selecionada, deve-se exibir o submenu do módulo;

- Caso a opção `2` seja selecionada, deve-se exibir o submenu do módulo;

- Caso a opção `3` seja selecionada, deve-se encerrar a execução do script (dica: verifique o `exit code`);

#### 9 - Ao selecionar a opção 1 do menu de opções e inserir as informações necessárias, a ação adequada deve ser disparada.

```md
Selecione uma das opções a seguir:

1 - Iniciar importação a partir de um arquivo TXT;
2 - Visualizar detalhes de arquivo anexado por posição;
3 - Remover arquivo da base;
4 - Voltar ao menu anterior.
5 - Sair.
```

##### As seguintes verificações serão feitas:

- A mensagem de menu deve ser exibida corretamente;

- Caso a opção `1` seja selecionada, deve-se exibir a mensagem "Digite o path do arquivo TXT a ser importado:";

- Caso a opção `2` seja selecionada, deve-se exibir a mensagem "Digite a posição do arquivo a ser detalhado:";

- Caso a opção `3` seja selecionada, deve-se exibir a mensagem "Digite Y para confirmar a remoção ou N para cancelar:";

- Caso a opção `4` seja selecionada, deve-se ser apresentado o menu anterior;

- Caso a opção não exista, exiba a mensagem de erro "Opção inválida" na `stderr`.


#### 10 - Ao selecionar uma opção do menu de opções e inserir as informações necessárias, a ação adequada deve ser disparada e seu resultado deve ser exibido.

##### As seguintes verificações serão feitas:

- Caso a opção `1` seja selecionada, a importação deve ser feita utilizando função `txt_importer`;

- Caso a opção `2` seja selecionada, a apresentação deve ser feita utilizando função `file_metadata`;

- Caso a opção `3` seja selecionada, a remoção deve ser feita utilizando função `remove`;

- Caso a opção `5` seja selecionada, deve-se encerrar a execução do script (dica: verifique o `exit code`);

- Após finalizar a execução de uma ação(exceto a 5), a sessão do script não deve ser encerrada.

#### 11 - Ao selecionar a opção 2 do menu de opções e inserir as informações necessárias, a ação adequada deve ser disparada.

```md
Selecione uma das opções a seguir:

1 - Verificar se palavra existe na base;
2 - Buscar palavra em base;
3 - Voltar ao menu anterior.
4 - Sair.
```

##### As seguintes verificações serão feitas:

- A mensagem de menu deve ser exibida corretamente;

- Caso a opção `1` seja selecionada, deve-se exibir a mensagem "Digite a palavra a ser consultada:";

- Caso a opção `2` seja selecionada, deve-se exibir a mensagem "Digite a palavra a ser consultada:";

- Caso a opção `3` seja selecionada, deve-se ser apresentado o menu anterior;

- Caso a opção `4` seja selecionada, deve-se encerrar a execução do script (dica: verifique o `exit code`);

- Após finalizar a execução de uma ação(exceto a 4), a sessão do script não deve ser encerrada.


#### 12 - Ao selecionar uma opção do menu de opções e inserir as informações necessárias, a ação adequada deve ser disparada e seu resultado deve ser exibido.

##### As seguintes verificações serão feitas:

- A mensagem de menu deve ser exibida corretamente;

- Caso a opção `1` seja selecionada, a consulta deve ser feita utilizando função `exists_word` e seu resultado deve ser impresso em tela;

- Caso a opção `2` seja selecionada, a consulta deve ser feita utilizando função `search_by_word` e seu resultado deve ser impresso em tela;

- Caso a opção não exista, exiba a mensagem de erro "Opção inválida" na `stderr`.

#### 13 - A cobertura de testes unitários do pacote deve ser de no mínimo 90%.

##### Pacote `ting_file_management`

##### As seguintes verificações serão feitas:

- Todos os testes que envolvem mensagens na saída padrão ou de erro, devem ter sua saída redirecionada para _Fakes_ com `StringIO`;

- Todos os testes que envolvem manipulação de arquivos criam _Fakes_ com `StringIO`;

- A cobertura de testes é de no mínimo 90%.

#### Pacote `ting_word_searches`

##### As seguintes verificações serão feitas:

- Todos os testes que envolvem mensagens na saída padrão ou de erro, devem ter sua saída redirecionada para _Fakes_ com `StringIO`;

- Todos os testes que envolvem manipulação de arquivos criam _Fakes_ com `StringIO`;

- A cobertura de testes é de no mínimo 90%.

---

### DURANTE O DESENVOLVIMENTO

- Faça `commits` das alterações que você fizer no código regularmente

- Lembre-se de sempre após um (ou alguns) `commits` atualizar o repositório remoto

- Os comandos que você utilizará com mais frequência são:
  1. `git status` _(para verificar o que está em vermelho - fora do stage - e o que está em verde - no stage)_
  2. `git add` _(para adicionar arquivos ao stage do Git)_
  3. `git commit` _(para criar um commit com os arquivos que estão no stage do Git)_
  4. `git push -u nome-da-branch` _(para enviar o commit para o repositório remoto na primeira vez que fizer o `push` de uma nova branch)_
  5. `git push` _(para enviar o commit para o repositório remoto após o passo anterior)_

---

### DEPOIS DE TERMINAR O DESENVOLVIMENTO (OPCIONAL)

Para sinalizar que o seu projeto está pronto para o _"Code Review"_ dos seus colegas, faça o seguinte:

- Vá até a página **DO SEU** _Pull Request_, adicione a label de _"code-review"_ e marque seus colegas:

  - No menu à direita, clique no _link_ **"Labels"** e escolha a _label_ **code-review**;

  - No menu à direita, clique no _link_ **"Assignees"** e escolha **o seu usuário**;

  - No menu à direita, clique no _link_ **"Reviewers"** e digite `students`, selecione o time `tryber/students-sd-0x`.

Caso tenha alguma dúvida, [aqui tem um video explicativo](https://vimeo.com/362189205).

---

### REVISANDO UM PULL REQUEST

Use o conteúdo sobre [Code Review](https://app.betrybe.com/course/real-life-engineer/code-review) para te ajudar a revisar os _Pull Requests_.

#VQV 🚀
