## Test Driven Development (TDD) com Python

Há anotações nos comentários dos arquivos .py do projeto.

**Pytest:**
- É necessário instalar uma biblioteca pelo pip
- Roda os todos os testes com apenas um "pytest" no terminal
- Testes escritos sem necessidade de uma classe de teste
- Tratamento de exceções:
    - with pytest.raises(ValueError):
- É possível criar fixtures para inicializar individualmente em cada função
    - usando @pytest.fixture
    - passando a fixture como parametro da função do teste

**Unittest:**
- Biblioteca nativa do python
- Roda no terminal com python -m unittest tests/test_NOME.py
- Testes escritos dentro de uma classe de teste
- Tratamento de exceções:
    - with self.assertRaises(ValueError):
- SetUp que inicializa a cada teste