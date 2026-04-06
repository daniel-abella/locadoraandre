# 🎬 locadoraandre

Sistema de locadora em Python com MySQL 🍿

## ✨ Visão geral

Este projeto implementa uma aplicação de terminal para cadastro e manutenção de filmes em uma tabela `Filmes` no MySQL. A estrutura foi separada em três partes para deixar o código mais organizado e fácil de entender:

- `locadoraappv3.py`: arquivo principal, responsável por iniciar o programa e controlar o menu.
- `operacoeslocadora.py`: reúne as funcionalidades da locadora, como listar, inserir, pesquisar, atualizar e excluir filmes.
- `operacoesbd.py`: faz a ponte com o banco de dados, executando comandos SQL e controlando a conexão.

## 🚀 Funcionamento de `locadoraappv3.py`

O arquivo `locadoraappv3.py` é a porta de entrada da aplicação. É ele quem liga tudo e mantém o programa rodando até o usuário escolher sair.

### 🔄 Fluxo de execução

1. Importa todas as funções de `operacoeslocadora.py`.
2. Cria uma conexão com o banco usando `criarConexao('localhost', 'root', 'Unifacisa12!', 'locadora')`.
3. Exibe um menu interativo no terminal.
4. Lê a opção escolhida pelo usuário.
5. Chama a função correspondente à opção selecionada.
6. Repete esse processo até que a opção `7` seja escolhida.
7. Fecha a conexão com `encerrarConexao(conexao)` e encerra o programa.

### 📋 Menu disponível

- `1) Listar`: mostra todos os filmes cadastrados 🎞️
- `2) Inserir`: cadastra um novo filme ➕
- `3) Pesquisar pelo Código`: procura um filme pelo código 🔎
- `4) Atualizar`: altera o título de um filme ✏️
- `5) Excluir`: remove um filme do cadastro 🗑️
- `6) Quantidade`: mostra quantos filmes existem no banco 📊
- `7) Sair`: finaliza a aplicação 👋

## 🎯 Relação entre o menu e os métodos de `operacoeslocadora.py`

O arquivo `operacoeslocadora.py` concentra a lógica de negócio da locadora. Cada opção do menu chama um método específico, e esses métodos usam `operacoesbd.py` para conversar com o banco de dados.

### 🎞️ `listarFilmes(conexao)`

- Executa o SQL `select * from Filmes`.
- Usa `listarBancoDados` para buscar todos os registros.
- Exibe no terminal o título e o ano de cada filme.
- Se não houver filmes cadastrados, informa isso ao usuário.

### ➕ `inserirNovoFilme(conexao)`

- Pede ao usuário o nome, a sinopse e o ano do filme.
- Executa o SQL `insert into Filmes (titulo, sinopse, ano) values (%s,%s,%s);`.
- Usa `insertNoBancoDados` para salvar o novo filme.
- Mostra o código gerado após a inserção.

### 🔎 `pesquisarFilmePeloCodigo(conexao)`

- Solicita o código do filme.
- Executa o SQL `select * from Filmes where codigo = %s`.
- Usa `listarBancoDados` com o código informado como parâmetro.
- Se encontrar o filme, exibe o nome e o ano de lançamento.
- Se não encontrar, informa que nenhum filme foi localizado.

### ✏️ `substituirFilme(conexao)`

- Solicita o código do filme que será alterado.
- Pede o novo título.
- Executa o SQL `UPDATE Filmes SET titulo = %s WHERE codigo = %s`.
- Usa `atualizarBancoDados` para aplicar a mudança.
- Verifica quantas linhas foram afetadas para saber se o código realmente existe.

### 🗑️ `removerFilmePeloCodigo(conexao)`

- Solicita o código do filme a ser removido.
- Executa o SQL `delete from Filmes where codigo = %s`.
- Usa `excluirBancoDados` para apagar o registro.
- Confirma o resultado com base na quantidade de linhas afetadas.

### 📊 `obterQuantidadeFilmes(conexao)`

- Executa o SQL `select count(*) from Filmes;`.
- Usa `listarBancoDados` para consultar a quantidade total.
- Exibe o número atual de filmes cadastrados.

## 🛠️ Uso da biblioteca `operacoesbd.py`

O arquivo `operacoesbd.py` funciona como a camada de acesso ao banco de dados. Em vez de espalhar SQL e controle de conexão pelo projeto inteiro, ele centraliza essas responsabilidades em funções reutilizáveis.

Isso deixa o código mais limpo, mais organizado e mais fácil de manter 💡

### 🔌 `criarConexao(endereco, usuario, senha, bancodedados)`

- Abre a conexão com o MySQL usando `mysql.connector.connect`.
- Recebe host, usuário, senha e nome do banco.
- Se houver erro na conexão, exibe a mensagem e retorna `None`.

### 🔒 `encerrarConexao(connection)`

- Fecha a conexão com o banco, se ela existir.

### 💾 `insertNoBancoDados(connection, sql, dados)`

- Executa inserções com `prepared=True`.
- Usa `commit()` quando tudo ocorre bem.
- Se ocorrer erro, executa `rollback()`.
- Retorna o identificador do último registro inserido.

### 📚 `listarBancoDados(connection, sql, params=None)`

- Executa consultas do tipo `SELECT`.
- Aceita parâmetros opcionais em consultas parametrizadas.
- Retorna os resultados com `fetchall()`.
- Se houver falha, retorna uma lista vazia.

### 🔄 `atualizarBancoDados(connection, sql, dados)`

- Executa comandos como `UPDATE`.
- Faz `commit()` após a alteração.
- Se houver erro, faz `rollback()`.
- Retorna a quantidade de linhas afetadas.

### ❌ `excluirBancoDados(connection, sql, dados)`

- Executa comandos como `DELETE`.
- Faz `commit()` quando a exclusão é concluída.
- Se houver erro, faz `rollback()`.
- Retorna a quantidade de linhas afetadas.

## 📌 Dependências e observações

- A aplicação depende da biblioteca `mysql-connector-python`.
- É necessário existir um banco chamado `locadora` com a tabela `Filmes`.
- A conexão com o banco está configurada diretamente no código principal.
- Como o menu usa `int(input(...))`, entradas não numéricas podem gerar erro de execução.

## 🎉 Resumo rápido

Se fosse resumir o projeto em uma frase: este é um sistema de locadora em terminal que usa Python para a lógica da aplicação e MySQL para armazenar os filmes cadastrados.

Simples, direto e funcional 🚀
