import json
import os
import time

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
    if len(data) == 0:
        return 1
    else:
        return data[-1]["_Anime__id"] + 1

class Anime:
    __id: int
    __nome: str
    __genero: str
    __lancamento: str
    __autor: str    
    __status: str
    __origem: str

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getGenero(self):
        return self.__genero

    def setGenero(self, genero):
        self.__genero = genero

    def getLancamento(self):
        return self.__lancamento

    def setLancamento(self, lancamento):
        self.__lancamento = lancamento

    def getAutor(self):
        return self.__autor

    def setAutor(self, autor):
        self.__autor = autor

    def getStatus(self):
        return self.__status

    def setStatus(self, status):
        self.__status = status

    def getOrigem(self):
        return self.__origem

    def setOrigem(self, origem):
        self.__origem = origem

    def cadastrar(self) -> dict:
        os.system('cls')
        self.setId(gerarid())
        self.setNome(str(input('Nome do anime: ')))
        self.setGenero(str(input('Gênero do anime: ')))
        self.setLancamento(str(input('Data de lançamento do anime: ')))
        self.setAutor(str(input('Autor do anime: ')))
        self.setStatus(str(input('Status: ')))
        self.setOrigem(str(input('Origem do anime: ')))
        print('''-----------------------------
    Anime cadastrado com sucesso!''')
        time.sleep(1)
        animes = lerArquivo()
        animes.append(self.__dict__)
        salvarArquivo(animes)

    def vertodos() -> list:
        arq = open(nome_arquivo, 'r', encoding='utf-8')
        data = arq.read()
        animes = json.loads(data)

        print('--------------------------------------------------')
        print('Este são todos os animes que estão no sistema!')
        print('--------------------------------------------------')
        for anime in animes:
            print(f'ID: {anime["_Anime__id"]}')
            print(f'Nome: {anime["_Anime__nome"]}')
            print(f'Gênero: {anime["_Anime__genero"]}')
            print(f'Lançamento: {anime["_Anime__lancamento"]}')
            print(f'autor: {anime["_Anime__autor"]}')
            print(f'Status: {anime["status"]}')
            print(f'Origem: {anime["_Anime__origem"]}')
            print('--------------------------------------------------')

        salvarArquivo(animes)
        
    def deletaranime() -> list:
        os.system('cls')
        animes = lerArquivo()

        for anime in animes:
            print(f'ID: {anime["id"]} - {anime["nome"]}')
            print(50 * '-')
        
        selecionar = int(input('Digite o ID do anime que deseja deletar: '))
        
        for i in range(len(animes)):
            if animes[i]['id'] == selecionar:
                print(f'Anime deletado!')
                del(animes[i])
                break
            
        salvarArquivo(animes)

    def alterarAnime():
        os.system('cls')
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

        propriedade = int(input('''Selecione o atributo do anime que deseja ver os detalhes!\n
    1 - ID
    2 - Nome
    3 - Gênero
    4 - Lançamento
    5 - Autor
    6 - Status
    7 - Origem
        
    Digite a opção desejada: '''))
        valor = input("Digite a resposta da opção que desejou: ")

        if propriedade == 1:
            propriedade = 'id'
        elif propriedade == 2:
            propriedade = 'nome'
        elif propriedade == 3:
            propriedade = 'genero'
        elif propriedade == 4:
            propriedade = 'lancamento'
        elif propriedade == 5:
            propriedade = 'autor'
        elif propriedade == 6:
            propriedade = 'atatus'
        elif propriedade == 7:
            propriedade = 'origem'
        
        cont = 0
        while True:
            for anime in animes:
                if str(anime[propriedade]) == valor:
                    print(anime)
                    cont += 1
            if cont == 0:
                print('Opção inválida!')
            break

anime = Anime()