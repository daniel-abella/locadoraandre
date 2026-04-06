from operacoeslocadora import *

opcao = 1
conexao = criarConexao('localhost',"root", "Unifacisa12!","locadora")

while opcao != 7:
    print("\n::: Locadora :::")
    print("\n1) Listar \n2) Inserir \n3) Pesquisar pelo Código \n4) Atualizar \n5) Excluir \n6) Quantidade \n7) Sair")

    opcao = int(input("Digite a sua opção: "))

    if opcao == 1:
        listarFilmes(conexao)

    elif opcao == 2:
        inserirNovoFilme(conexao)

    elif opcao == 3:
        pesquisarFilmePeloCodigo(conexao)

    elif opcao == 4:
        substituirFilme(conexao)

    elif opcao == 5:
        removerFilmePeloCodigo(conexao)

    elif opcao == 6:
        obterQuantidadeFilmes(conexao)

    elif opcao != 7:
        print("Opção Inválida")

encerrarConexao(conexao)
print("Obrigado por usar o App.")