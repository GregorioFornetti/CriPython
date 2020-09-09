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
def test_base64_7bits():
    assert base_64.codificar_base_64('a') == 'YQ=='
    assert base_64.traduzir_base_64('YQ==') == 'a'

def test_base64_11bits():
    assert base_64.codificar_base_64('¥') == 'wqU='
    assert base_64.traduzir_base_64('wqU=') == '¥'

def test_base64_16bits():
    assert base_64.codificar_base_64('ऍ') == '4KSN'
    assert base_64.traduzir_base_64('4KSN') == 'ऍ'

def test_base64_21bits(): 
    assert base_64.codificar_base_64('𐓉') == '8JCTiQ=='
    assert base_64.traduzir_base_64('8JCTiQ==') == '𐓉'

def test_base64_mensagem_invalida_1():
    assert base_64.codificar_base_64('') == dicionarios.retorna_erro_mensagem()

def test_base64_mensagem_invalida_2():
    assert base_64.traduzir_base_64('!??!') == dicionarios.retorna_erro_mensagem()

def test_base64_texto_grande_1():
    assert base_64.codificar_base_64(
    'Texto normal, sem muitos caracteres especiais, apenas caracteres de 7 bits'
    ) == 'VGV4dG8gbm9ybWFsLCBzZW0gbXVpdG9zIGNhcmFjdGVyZXMgZXNwZWNpYWlzLCBhcGVuYXMgY2FyYWN0ZXJlcyBkZSA3IGJpdHM='
    assert base_64.traduzir_base_64(
    'VGV4dG8gbm9ybWFsLCBzZW0gbXVpdG9zIGNhcmFjdGVyZXMgZXNwZWNpYWlzLCBhcGVuYXMgY2FyYWN0ZXJlcyBkZSA3IGJpdHM='
    ) == 'Texto normal, sem muitos caracteres especiais, apenas caracteres de 7 bits'

def test_base64_texto_grande_2():
    assert base_64.codificar_base_64(
    'Agora cóm cáráctérés especiais. Bóra téstár... Máx 11 bits... ¥©Ȍɬ... Será que vai ?'
    ) == 'QWdvcmEgY8OzbSBjw6Fyw6FjdMOpcsOpcyBlc3BlY2lhaXMuIELDs3JhIHTDqXN0w6FyLi4uIE3DoXggMTEgYml0cy4uLiDCpcKpyIzJrC4uLiBTZXLDoSBxdWUgdmFpID8='
    assert base_64.traduzir_base_64(
    'QWdvcmEgY8OzbSBjw6Fyw6FjdMOpcsOpcyBlc3BlY2lhaXMuIELDs3JhIHTDqXN0w6FyLi4uIE3DoXggMTEgYml0cy4uLiDCpcKpyIzJrC4uLiBTZXLDoSBxdWUgdmFpID8='
    ) == 'Agora cóm cáráctérés especiais. Bóra téstár... Máx 11 bits... ¥©Ȍɬ... Será que vai ?'

def test_base64_texto_grande_3():
    assert base_64.codificar_base_64(
    'Agórá cóm máis caractéres espécias !! Máx 16 bits - ౻óaU౻౻ႫaáoíႫჇჇaí'
    ) == 'QWfDs3LDoSBjw7NtIG3DoWlzIGNhcmFjdMOpcmVzIGVzcMOpY2lhcyAhISBNw6F4IDE2IGJpdHMgLSDgsbvDs2FV4LG74LG74YKrYcOhb8Ot4YKr4YOH4YOHYcOt'
    assert base_64.traduzir_base_64(
    'QWfDs3LDoSBjw7NtIG3DoWlzIGNhcmFjdMOpcmVzIGVzcMOpY2lhcyAhISBNw6F4IDE2IGJpdHMgLSDgsbvDs2FV4LG74LG74YKrYcOhb8Ot4YKr4YOH4YOHYcOt'
    ) == 'Agórá cóm máis caractéres espécias !! Máx 16 bits - ౻óaU౻౻ႫaáoíႫჇჇaí'

def test_base64_texto_grande_4():
    assert base_64.codificar_base_64(
    'Agórá sla, O MAXIMO: 21 bits: 𑇣sd౻Ⴧ𐐀áó౻adჇ𐐀á౻. Espero que funcione...'
    ) == 'QWfDs3LDoSBzbGEsIE8gTUFYSU1POiAyMSBiaXRzOiDwkYejc2Tgsbvhg4fwkJCAw6HDs+Cxu2Fk4YOH8JCQgMOh4LG7LiBFc3Blcm8gcXVlIGZ1bmNpb25lLi4u'
    assert base_64.traduzir_base_64(
    'QWfDs3LDoSBzbGEsIE8gTUFYSU1POiAyMSBiaXRzOiDwkYejc2Tgsbvhg4fwkJCAw6HDs+Cxu2Fk4YOH8JCQgMOh4LG7LiBFc3Blcm8gcXVlIGZ1bmNpb25lLi4u'
    ) == 'Agórá sla, O MAXIMO: 21 bits: 𑇣sd౻Ⴧ𐐀áó౻adჇ𐐀á౻. Espero que funcione...'