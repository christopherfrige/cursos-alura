class Cliente:
    def __init__(self, nome):
        self.__nome = nome
    
    # Propriedade para um get
    @property
    def nome(self):
        print("chamando @property nome()")
        return self.__nome.title()

    # Propriedade para um set
    @nome.setter
    def nome(self, nome):
        print("chamando setter nome()")
        self.__nome = nome

pass