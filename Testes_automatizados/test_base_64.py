from Cifras import base_64
import base64
import dicionarios

# BASE_64
def test_base64_7bits():
    assert base_64.codif2_base_64('a') == 'YQ=='
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
    assert base_64.codif2_base_64(
    'Agórá cóm máis caractéres espécias !! Máx 16 bits - ౻óaU౻౻ႫaáoíႫჇჇaí'
    ) == 'QWfDs3LDoSBjw7NtIG3DoWlzIGNhcmFjdMOpcmVzIGVzcMOpY2lhcyAhISBNw6F4IDE2IGJpdHMgLSDgsbvDs2FV4LG74LG74YKrYcOhb8Ot4YKr4YOH4YOHYcOt'
    assert base_64.traduzir_base_64(
    'QWfDs3LDoSBjw7NtIG3DoWlzIGNhcmFjdMOpcmVzIGVzcMOpY2lhcyAhISBNw6F4IDE2IGJpdHMgLSDgsbvDs2FV4LG74LG74YKrYcOhb8Ot4YKr4YOH4YOHYcOt'
    ) == 'Agórá cóm máis caractéres espécias !! Máx 16 bits - ౻óaU౻౻ႫaáoíႫჇჇaí'

def test_base64_texto_grande_4():
    with open('teste_longo_base_64.txt', 'r', encoding='utf-8') as arquivo_teste:
        texto_teste = arquivo_teste.read().split('\n')
        texto_normal = texto_teste[0]
        texto_encriptado = texto_teste[1]
    
    assert base_64.codif2_base_64(texto_normal) == texto_encriptado
    assert base_64.traduzir_base_64(texto_encriptado) == texto_normal
