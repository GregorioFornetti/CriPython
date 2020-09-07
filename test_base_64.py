import Cifras.base_64 as base_64
import dicionarios
'''
Arquivo de testes automatizados !
Para testar o programa, é preciso que a biblioteca PyTest esteja instalada em seu computador.
Para instalar, execute no terminal: pip install -U pytest
Depois disso, coloque o terminal para rodar na pasta principal do programa e execute
o comando: pytest
'''

# BASE_64
def test_base64_menor_ou_igual_7bits():
    assert base_64.codificar_base_64('a') == 'YQ=='
    assert base_64.traduzir_base_64('YQ==') == 'a'

def test_base64_menor_ou_igual_11bits():
    pass

def test_base64_menor_ou_igual_16bits():
    pass

def test_base64_menor_ou_igual_21bits():
    pass

def test_base64_mensagem_invalida():
    pass

def test_base64_texto_grande_1():
    pass

def test_base64_texto_grande_2():
    pass

def test_base64_texto_grande_3():
    pass

def test_base64_texto_grande_4():
    pass