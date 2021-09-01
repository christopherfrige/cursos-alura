from src.leilao.dominio import Usuario, Leilao
import pytest
from src.leilao.excecoes import LanceInvalido

# Funciona como se fosse um SetUp
@pytest.fixture
def chris():
    return Usuario("Chris", 100.0)

@pytest.fixture
def leilao():
    return Leilao("Celular")


def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_lance(chris, leilao):
    chris.propoe_lance(leilao, 50.0)

    assert chris.carteira == 50.0

def test_deve_permitir_propor_lance_quando_o_valor_é_menor_que_o_valor_da_carteira(chris, leilao):
    chris.propoe_lance(leilao, 1.0)

    assert chris.carteira == 99.0

def test_deve_permitir_propor_lance_quando_o_valor_é_igual_ao_valor_da_carteira(chris, leilao):
    chris.propoe_lance(leilao, 100.0)

    assert chris.carteira == 0.0
    
def test_nao_deve_permitir_propor_lance_com_valor_maior_que_o_da_carteira(chris, leilao):
    with pytest.raises(LanceInvalido):
        chris.propoe_lance(leilao, 200.0)
