from codigo import *


while True:
    print(10 * '#', 'BEM VINDO AO NOSSO PROGRAMA!', 10 * '#')
    print(50 * '*')
    print('ESCOLHA UMA DAS OPÇÕES ABAIXO.')
    print('''
1 - CADASTRAR ANIME.
2 - ALTERAR CADASTRO.
3 - DELETAR ANIME.
4 - SELECIONAR ANIME POR UM ATRIBUTO.
5 - VER TODOS.
6 - ENCERRAR PROGRAMA.
    ''')
    print(50 * '*')
    funcao = int(input('Digite o número da opção que desejar: '))
    if funcao == 1:
        anime.cadastrar()
    elif funcao == 2:
        anime.alterarAnime()
    elif funcao == 3:
        anime.deletaranime()
    elif funcao == 4:
        anime.selecionarAnime()
    elif funcao == 5:
        anime.vertodos()
    elif funcao == 6:
        break
    else:
        print('CÓDIGO INVÁLIDO!')
