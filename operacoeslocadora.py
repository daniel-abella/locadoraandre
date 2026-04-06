from operacoesbd import *

def obterQuantidadeFilmes(conexao):
    consulta = 'select count(*) from Filmes;'

    filmes = listarBancoDados(conexao, consulta)
    print("Atualmente tem(os)", filmes[0][0], "filme(s)")


def removerFilmePeloCodigo(conexao):
    codigoFilme = int(input("Digite o código do filme a ser removido: "))
    consulta = 'delete from Filmes where codigo = %s'
    dados = [codigoFilme]

    linhasAfetadas = excluirBancoDados(conexao, consulta, dados)

    if linhasAfetadas == 0:
        print("Não existe filme para o código informado.")
    else:
        print("Filme removido com sucesso.")


def substituirFilme(conexao):
    codigoFilme = int(input("Digite o código do filme a ser atualizado: "))
    novoTituloFilme = input("Digite o novo titulo do filme: ")

    consulta = 'UPDATE Filmes SET titulo = %s WHERE codigo = %s'
    dados = [novoTituloFilme, codigoFilme]

    linhasAfetadas = atualizarBancoDados(conexao, consulta, dados)

    if linhasAfetadas == 0:
        print("Não existe filme para o código informado.")
    else:
        print("Filme atualizado com sucesso.")


def pesquisarFilmePeloCodigo(conexao):
    codigoFilme = int(input("Digite o código do filme: "))
    consulta = 'select * from Filmes where codigo = %s'
    dados = [codigoFilme]

    filmes = listarBancoDados(conexao, consulta, dados)

    if len(filmes) > 0:
        print("Nome do filme", filmes[0][1], "lançado em", filmes[0][3])
    else:
        print("Nenhum filme foi encontrado para o código informado.")


def inserirNovoFilme(conexao):
    nomeNovoFilme = input("Informe o nome do filme: ")
    sinopseNovoFilme = input("Informe a sinopse do filme: ")
    anoNovoFilme = int(input("Informe o ano do filme: "))

    consulta = 'insert into Filmes (titulo, sinopse, ano) values (%s,%s,%s);'
    dados = [nomeNovoFilme, sinopseNovoFilme, anoNovoFilme]

    codigoNovoFilme = insertNoBancoDados(conexao, consulta, dados)

    print("Filme criado com sucesso! O código é", codigoNovoFilme)


def listarFilmes(conexao):
    consulta = 'select * from Filmes'
    filmes = listarBancoDados(conexao, consulta)

    if len(filmes) > 0:
        print("Lista de Filmes")
        for item in filmes:
            print("Nome do filme", item[1], "lançado no ano", item[3])
    else:
        print("Nenhum filme foi encontrado")