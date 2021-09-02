class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    def dar_like(self):
        self.__likes += 1
    
    @property
    def nome(self):
        return self.__nome

    @property
    def likes(self):
        return self.__likes

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()
    

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @property
    def likes(self):
        return self.__likes

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

harrypotter = Filme("harry potter", "2010", 120)
print(f"Nome: {harrypotter.nome} - Ano: {harrypotter.ano}"
f" - Temporadas: {harrypotter.duracao} - Likes: {harrypotter.likes}")

dark = Serie("dark", "2018", 3)
dark.dar_like()
dark.dar_like()
print(f"Nome: {dark.nome} - Ano: {dark.ano}"
f" - Temporadas: {dark.temporadas} - Likes: {dark.likes}")
