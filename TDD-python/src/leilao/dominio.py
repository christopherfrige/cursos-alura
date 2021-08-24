import sys

class Usuario:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        # Números arbitrários para comparação
        self.maior_lance = sys.float_info.min
        self.menor_lance = sys.float_info.max

    def propoe (self, lance: Lance):
        # O lance será valido se nao houverem lances ainda, ou o ultimo lance tem usuario
        if not self.__lances or self.__lances[-1].usuario != lance.usuario:
            if lance.valor > self.maior_lance:
                self.maior_lance = lance.valor
            if lance.valor < self.menor_lance:
                self.menor_lance = lance.valor

            self.__lances.append(lance)
        else:
            raise ValueError("O mesmo usuário não pode propor dois lances seguindos!")

    @property
    def lances(self):
        # Retorna uma cópia da lista (cópia rasa)
        return self.__lances[:]
