# locadoraandre

Sistema de locadora em Python com MySQL.

## Visão geral

O projeto implementa uma aplicação de terminal para cadastro e manutenção de filmes em uma tabela `Filmes` no MySQL. A organização está dividida em três camadas simples:

- `locadoraappv3.py`: arquivo principal, responsável pela execução do menu e pelo fluxo da aplicação.
- `operacoeslocadora.py`: concentra as regras de negócio ligadas às opções do menu.
- `operacoesbd.py`: encapsula as operações de conexão e execução de comandos SQL no banco de dados.

## Funcionamento de `locadoraappv3.py`

O arquivo `locadoraappv3.py` é o ponto de entrada da aplicação.

Fluxo de execução:

1. Importa todas as funções de `operacoeslocadora.py`.
2. Cria uma conexão com o banco por meio da função `criarConexao('localhost', 'root', 'Unifacisa12!', 'locadora')`.
3. Exibe um menu em loop com as operações disponíveis.
4. Lê a opção digitada pelo usuário.
5. Direciona a execução para a função correspondente.
6. Encerra o programa quando a opção `7` é informada.
7. Fecha a conexão com `encerrarConexao(conexao)`.

Menu disponível:

- `1) Listar`: exibe todos os filmes cadastrados.
- `2) Inserir`: cadastra um novo filme.
- `3) Pesquisar pelo Código`: busca um filme pelo código.
- `4) Atualizar`: altera o título de um filme existente.
- `5) Excluir`: remove um filme pelo código.
- `6) Quantidade`: mostra a quantidade total de filmes cadastrados.
- `7) Sair`: finaliza a aplicação.

## Relação entre o menu e os métodos de `operacoeslocadora.py`

O arquivo `operacoeslocadora.py` usa as funções de `operacoesbd.py` para executar as ações no banco. Cada opção do menu chama um método específico:

### `listarFilmes(conexao)`

- Executa o SQL `select * from Filmes`.
- Usa `listarBancoDados` para recuperar todos os registros.
- Exibe no terminal o título e o ano de cada filme.
- Caso não existam registros, informa que nenhum filme foi encontrado.

### `inserirNovoFilme(conexao)`

- Solicita ao usuário o nome, a sinopse e o ano do filme.
- Executa o SQL `insert into Filmes (titulo, sinopse, ano) values (%s,%s,%s);`.
- Usa `insertNoBancoDados` para gravar o novo registro.
- Exibe o código gerado para o filme inserido.

### `pesquisarFilmePeloCodigo(conexao)`

- Solicita o código do filme.
- Executa o SQL `select * from Filmes where codigo = %s`.
- Usa `listarBancoDados` passando o código como parâmetro.
- Se encontrar o registro, mostra o nome e o ano de lançamento.
- Caso contrário, informa que nenhum filme foi encontrado.

### `substituirFilme(conexao)`

- Solicita o código do filme que será alterado.
- Solicita o novo título.
- Executa o SQL `UPDATE Filmes SET titulo = %s WHERE codigo = %s`.
- Usa `atualizarBancoDados` para efetivar a alteração.
- Verifica a quantidade de linhas afetadas para confirmar se o código existe.

### `removerFilmePeloCodigo(conexao)`

- Solicita o código do filme a ser removido.
- Executa o SQL `delete from Filmes where codigo = %s`.
- Usa `excluirBancoDados` para remover o registro.
- Valida a quantidade de linhas afetadas para informar se a remoção ocorreu.

### `obterQuantidadeFilmes(conexao)`

- Executa o SQL `select count(*) from Filmes;`.
- Usa `listarBancoDados` para recuperar o total de registros.
- Exibe a quantidade atual de filmes cadastrados.

## Uso da biblioteca `operacoesbd.py`

O arquivo `operacoesbd.py` funciona como uma camada de acesso ao banco de dados. Ele evita que o arquivo principal ou as regras da locadora precisem lidar diretamente com cursores, `commit`, `rollback` e tratamento de exceções.

### `criarConexao(endereco, usuario, senha, bancodedados)`

- Abre a conexão com o MySQL usando `mysql.connector.connect`.
- Recebe host, usuário, senha e nome do banco.
- Em caso de erro, exibe a mensagem e retorna `None`.

### `encerrarConexao(connection)`

- Fecha a conexão com o banco, se ela existir.

### `insertNoBancoDados(connection, sql, dados)`

- Executa inserções no banco com `prepared=True`.
- Usa `commit()` quando a operação é bem-sucedida.
- Em caso de erro, executa `rollback()`.
- Retorna o identificador do último registro inserido.

### `listarBancoDados(connection, sql, params=None)`

- Executa consultas `SELECT`.
- Aceita parâmetros opcionais para consultas parametrizadas.
- Retorna a lista de resultados obtidos com `fetchall()`.
- Em caso de falha, retorna uma lista vazia.

### `atualizarBancoDados(connection, sql, dados)`

- Executa comandos de atualização como `UPDATE`.
- Realiza `commit()` após a alteração.
- Em caso de erro, faz `rollback()`.
- Retorna a quantidade de linhas afetadas.

### `excluirBancoDados(connection, sql, dados)`

- Executa comandos de remoção como `DELETE`.
- Realiza `commit()` quando a exclusão é concluída.
- Em caso de erro, faz `rollback()`.
- Retorna a quantidade de linhas afetadas.

## Dependências e observações

- A aplicação depende da biblioteca `mysql-connector-python`.
- É necessário existir um banco chamado `locadora` com a tabela `Filmes`.
- A conexão com o banco está configurada diretamente no código principal.
- Como o menu usa `int(input(...))`, entradas não numéricas podem gerar erro de execução.
