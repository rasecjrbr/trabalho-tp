import json
import random

nome_arquivo = 'animes.json'

def lerArquivo() -> list:
    arq = open(nome_arquivo, 'r', encoding='utf-8')
    data = arq.read()
    return json.loads(data)


def salvarArquivo(animes: list):
    arq = open(nome_arquivo, 'w+', encoding='utf-8')
    data = json.dumps(animes, indent=4)
    arq.write(data)
    arq.close()

def gerarid():
    data = lerArquivo()
    datalista = []
    if len(data) == 0:
        return 0
    else:
        for i in range(len(data)):
            datalista.append(data[i]['id'])
    return max(datalista)
    

def cadastrar() -> dict:
    anime = {}
    anime['id'] = gerarid()+1
    anime['nome'] = str(input('Nome do anime: '))
    anime['genero'] = str(input('Gênero do anime: '))
    anime['lancamento'] = str(input('Data de lançamento do anime: '))
    anime['autor'] = str(input('Autor do anime: '))
    anime['status'] = str(input('Status: '))
    anime['origem'] = str(input('Origem do anime: '))
    

    animes = lerArquivo()
    animes.append(anime)
    salvarArquivo(animes)

def vertodos() -> list:
    arq = open(nome_arquivo, 'r', encoding='utf-8')
    data = arq.read()
    animes = json.loads(data)

    for anime in animes:
        print(f'ID: {anime["id"]}')
        print(f'Nome: {anime["nome"]}')
        print(f'Gênero: {anime["genero"]}')
        print(f'Lançamento: {anime["lancamento"]}')
        print(f'autor: {anime["autor"]}')
        print(f'Status: {anime["status"]}')
        print(f'Origem: {anime["origem"]}')
        print(50 * '*')

    salvarArquivo(animes)

        
def deletaranime() -> list:
    animes = lerArquivo()

    for anime in animes:
        print(f'ID: {anime["id"]} - {anime["nome"]}')
        print(50 * '-')
    
    selecionar = int(input('Digite o ID do anime que deseja deletar!\n'))
    
    for i in range(len(animes)):
        if animes[i]['id'] == selecionar:
            print(f'Anime deletado!')
            del(animes[i])
            break
        
    salvarArquivo(animes)

def alterarAnime():
    animes = lerArquivo()

    for anime in animes:
        print(f'ID: {anime["id"]} - {anime["nome"]}')
        print(50 * '-')

    selecionar = int(input('Digite o ID do anime que deseja alterar!\n'))
    menu = int(input('''Selecione o atributo que deseja alterar!
    1 - nome
    2 - genero
    3 - lancamento
    4 - autor
    5 - status
    6 - origem
    
    Digite a opção desejada: '''))

    
    
    for i in range(len(animes)):
        if animes[i]['id'] == selecionar:
            if menu == 1:
                animes[i]['nome'] = input('Digite o novo nome: ')
            if menu == 2:
                animes[i]['genero'] = input('Digite o novo genero: ')
            if menu == 3:
                animes[i]['lancamento'] = input('Digite a nova data de lançamento: ')
            if menu == 4:
                animes[i]['autor'] = input('Digite o novo autor: ')
            if menu == 5:
                animes[i]['status'] = input('Digite o novo status: ')
            if menu == 6:
                animes[i]['origem'] = input('Digite a nova origem: ')

    salvarArquivo(animes)

def selecionarAnime():
    animes = lerArquivo()

    vertodos()

    menu = int(input('''Selecione o atributo do anime que deseja ver os detalhes!\n'
    1 - ID
    2 - Nome
    3 - Gênero
    4 - Lançamento
    5 - Autor
    6 - Status
    7 - Origem
    
    Digite a opção desejada: '''))

    
    while True:
        if menu == 1:
            recebido = int(input('Digite o ID do anime desejado: '))
            for i in range(len(animes)):
                if animes['id'] == recebido:
                    print(animes[i])
                    break
                else:
                    print('Anime não encontrado! Tente novamente.')
        if menu == 2:
            recebido = input('Digite o nome: ')
        if menu == 3:
            recebido = input('Digite o gênero: ')
        if menu == 4:
            recebido = input('Digite a data de lançamento(dd/mm/aaaa): ')
        if menu == 5:
            recebido = input('Digite o autor: ')
        if menu == 6:
            recebido = input('Digite o status: ')
        if menu == 7:
            recebido = input('Digite a origem: ')

    salvarArquivo(animes)

# def selecionarAnime(propriedade, valor):
#     if propriedade == 1:
#         propriedade = 'id'
#     elif propriedade == 2:
#         propriedade = 'nome'
#     animes = lerArquivo()

#     for anime in animes:
#         if anime[propriedade] == valor:
#             return anime

#     return None

# anime = selecionarAnime('nome', 'José do Teste')
# if None != anime:
#     printarAnime(anime)
# else:
#     print("hsduhsuhdfbusf")