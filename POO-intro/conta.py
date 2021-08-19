class Conta:
    #Construtor
    def __init__(self, numero, titular, saldo, limite):
        print(f"Construindo objeto... {self}")
        # Encapsulamento
        # O "__" serve para transformar o atributo em privado
        # Para ser utilizado só dentro da classe
        # Só é possível chamar com por exemplo "_Conta__saldo"
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    #Método 
    def extrato(self):
        print (f"Saldo {self.__saldo} do titular {self.__titular}")

    def depositar(self, valor):
        self.__saldo += valor

    # Método privado, usado apenas para validação do saque
    def __pode_sacar(self, valor_a_sacar):
        return valor_a_sacar <= self.__saldo

    def sacar(self, valor):
        if (self.pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("Saldo insuficiente para saque")

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
    
    # Getters e Setters
    # Get sempre tem um return, set altera um valor
    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite 

    # Método estático, ou seja, é da classe - não precisando do objeto
    # Tomar cuidado, usar sabiamente (quando é um dado que todos métodos usam)
    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {"BB": "001", "Caixa": "104", "Bradesco": "237"}

print("pausa")