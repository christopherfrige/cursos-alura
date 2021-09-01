# Para executar no terminal é necessário escrever:
# python -m unittest tests/test_leilao.py

from unittest import TestCase
from src.leilao.dominio import Usuario, Lance, Leilao
from src.leilao.excecoes import LanceInvalido

class TestLeilao(TestCase):

    # Será invocado antes de cada método de teste
    # Deixar apenas aquilo que é realmente necessário, se não poderá perder performance
    def setUp(self):
        self.chris = Usuario("Chris", 500.0)
        self.leticia = Usuario("Leticia", 500.0)

        self.lance_leticia = Lance(self.leticia, 300.0)
        self.lance_chris = Lance(self.chris, 100.0)

        self.leilao = Leilao("PC Gamer")

    # Pode ser usado dessa forma também:
    # test_quando_adicionados_em_ordem_crescente_deve_retornar_o_maior_e_o_menor_valor_de_um_lance
    # https://dzone.com/articles/7-popular-unit-test-naming
    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        self.leilao.propoe(self.lance_chris)
        self.leilao.propoe(self.lance_leticia)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 300.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_nao_deve_permitir_propor_lance_em_ordem_decrescente(self):

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_leticia)
            self.leilao.propoe(self.lance_chris)


    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):
        self.leilao.propoe(self.lance_chris)

        self.assertEqual(100.0, self.leilao.menor_lance)
        self.assertEqual(100.0, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        zeca = Usuario("Zeca", 500.0)

        lance_zeca = Lance(zeca, 350.0)

        self.leilao.propoe(self.lance_chris)
        self.leilao.propoe(self.lance_leticia)
        self.leilao.propoe(lance_zeca)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 350.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

        # Fazer um teste que é parecido a outros testes = Classes de equivalência
        # Exemplo: Fazer um teste para validar o maior/menor valor para 4+ lances

    def test_deve_permitir_propor_lance_caso_leilao_nao_tenha_lances(self):
        self.leilao.propoe(self.lance_leticia)

        quantidade_de_lances_atual = len(self.leilao.lances)

        self.assertEqual(1, quantidade_de_lances_atual)

    def test_deve_permitir_propor_lance_caso_ultimo_o_usuario_seja_diferente(self):
        self.leilao.propoe(self.lance_chris)
        self.leilao.propoe(self.lance_leticia)

        quantidade_de_lances_atual = len(self.leilao.lances)
        self.assertEqual(2, quantidade_de_lances_atual)

    def test_nao_deve_permitir_propor_lance_caso_usuario_seja_o_mesmo(self):
        lance_chris_200 = Lance(self.chris, 200.0)

        # Se o ValueError (gerado quando dois lances da mesma pessoa são seguidos) não surgir, o teste irá falhar
        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_chris)
            self.leilao.propoe(lance_chris_200)
