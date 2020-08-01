import Cifras.cifra_de_vigenere as cifra_de_vigenere
'''
Arquivo de testes automatizados !
Para testar o programa, é preciso que a biblioteca PyTest esteja instalada em seu computador.
Para instalar, execute no terminal: pip install -U pytest
Depois disso, coloque o terminal para rodar na pasta principal do programa e execute
o comando: pytest
'''


# OPÇÃO: APENAS LETRAS
def test_cifra_de_vigenere_apenas_letras_chave_1():
    assert cifra_de_vigenere.encriptar_modo_apenas_letras(['b'], 'abcdef') == 'bcdefg'
    assert cifra_de_vigenere.traduzir_modo_apenas_letras(['b'], 'bcdefg') == 'abcdef'

def test_cifra_de_vigenere_apenas_letras_chave_2():
    assert cifra_de_vigenere.encriptar_modo_apenas_letras(['bca'], 'abcdef') == 'bdcegf'
    assert cifra_de_vigenere.traduzir_modo_apenas_letras(['bca'], 'bdcegf') == 'abcdef'

def test_cifra_de_vigenere_apenas_letras_chave_invalida_vazia():
    assert cifra_de_vigenere.encriptar_modo_apenas_letras([''], 'abc') == cifra_de_vigenere.erro_chave_apenas_letras
    assert cifra_de_vigenere.traduzir_modo_apenas_letras([''], 'abc') == cifra_de_vigenere.erro_chave_apenas_letras

def test_cifra_de_vigenere_apenas_letras_chave_invalida_caractere_especial():
    assert cifra_de_vigenere.encriptar_modo_apenas_letras(['abcé'], 'abc') == cifra_de_vigenere.erro_chave_apenas_letras
    assert cifra_de_vigenere.traduzir_modo_apenas_letras(['abcé'], 'abc') == cifra_de_vigenere.erro_chave_apenas_letras

def test_cifra_de_vigenere_apenas_letras_mensagem_invalida():
    assert cifra_de_vigenere.encriptar_modo_apenas_letras(['abc'], '') == cifra_de_vigenere.erro_mensagem
    assert cifra_de_vigenere.traduzir_modo_apenas_letras(['abc'], '') == cifra_de_vigenere.erro_mensagem

def test_cifra_de_vigenere_apenas_letras_maiusc_minusc():
    assert cifra_de_vigenere.encriptar_modo_apenas_letras(['AbCdE'], 'aBcDe') == 'aCeGi'
    assert cifra_de_vigenere.traduzir_modo_apenas_letras(['AbCdE'], 'aCeGi') == 'aBcDe'

def test_cifra_de_vigenere_apenas_letras_caracteres_especiais():
    assert cifra_de_vigenere.encriptar_modo_apenas_letras(['bcd'], 'abc ! ? áé .,') == 'bdf ! ? áé .,'
    assert cifra_de_vigenere.traduzir_modo_apenas_letras(['bcd'], 'bdf ! ? áé .,') == 'abc ! ? áé .,'

def test_cifra_de_vigenere_apenas_letras_ignorar_andamento_chave_quando_encontrar_caract_especial():
    assert cifra_de_vigenere.encriptar_modo_apenas_letras(['abc'], 'abc !í.,áé abc') == 'ace !í.,áé ace'
    assert cifra_de_vigenere.traduzir_modo_apenas_letras(['abc'], 'ace !í.,áé ace') == 'abc !í.,áé abc'

def test_cifra_de_vigenere_apenas_letras_volta():
    assert cifra_de_vigenere.encriptar_modo_apenas_letras(['bc'], 'zy yz') == 'aa zb'
    assert cifra_de_vigenere.traduzir_modo_apenas_letras(['bc'], 'aa zb') == 'zy yz'

def test_cifra_de_vigenere_apenas_letras_chave_maior():
    assert cifra_de_vigenere.encriptar_modo_apenas_letras(['flx'], 'oi alo') == 'tt xqz'
    assert cifra_de_vigenere.traduzir_modo_apenas_letras(['flx'], 'tt xqz') == 'oi alo'

def test_cifra_de_vigenere_apenas_letras_texto_1():
    assert cifra_de_vigenere.encriptar_modo_apenas_letras(['ataque'],
    'Vamos invadir a base deles amanhã !') == 'Vtmem mnoatcv a uaiy heeei uqaghã !'
    assert cifra_de_vigenere.traduzir_modo_apenas_letras(['ataque'],
    'Vtmem mnoatcv a uaiy heeei uqaghã !') == 'Vamos invadir a base deles amanhã !'

def test_cifra_de_vigenere_apenas_letras_texto_2():
    assert cifra_de_vigenere.encriptar_modo_apenas_letras(['covid'],
    'Cuidado para não se contaminar !' == 'Eidldfc kiuc bãj ah ecibdowiiu !')
    assert cifra_de_vigenere.traduzir_modo_apenas_letras(['covid'],
    'Eidldfc kiuc bãj ah ecibdowiiu !' == 'Cuidado para não se contaminar !')


# OPÇÃO: VÁRIOS CARACTERES
def test_cifra_de_vigenere_varios_caracteres_chave_1():
    assert cifra_de_vigenere.encriptar_modo_varios_caracteres(['!'], 'abcde') == 'bcdef'
    assert cifra_de_vigenere.traduzir_modo_varios_caracteres(['!'], 'bcdef') == 'abcde'

def test_cifra_de_vigenere_varios_caracteres_chave_2():
    assert cifra_de_vigenere.encriptar_modo_varios_caracteres(['!"#'], 'abcde') == 'bdfeg'
    assert cifra_de_vigenere.traduzir_modo_varios_caracteres(['!"#'], 'bdfeg') == 'abcde'

def test_cifra_de_vigenere_varios_caracteres_chave_invalida_vazia():
    assert cifra_de_vigenere.encriptar_modo_varios_caracteres([''], 'abc') == cifra_de_vigenere.erro_chave_varios_caracteres
    assert cifra_de_vigenere.traduzir_modo_varios_caracteres([''], 'abc') == cifra_de_vigenere.erro_chave_varios_caracteres

def test_cifra_de_vigenere_varios_caracteres_chave_invalida_acima_do_limite():
    assert cifra_de_vigenere.encriptar_modo_varios_caracteres(['˟'], 'abc') == cifra_de_vigenere.erro_chave_varios_caracteres
    assert cifra_de_vigenere.traduzir_modo_varios_caracteres(['˟'], 'abc') == cifra_de_vigenere.erro_chave_varios_caracteres

def test_cifra_de_vigenere_varios_caracteres_mensagem_invalida():
    assert cifra_de_vigenere.encriptar_modo_varios_caracteres(['abc'], '') == cifra_de_vigenere.erro_mensagem
    assert cifra_de_vigenere.traduzir_modo_varios_caracteres(['abc'], '') == cifra_de_vigenere.erro_mensagem

def test_cifra_de_vigenere_varios_caracteres_mensagem_acima_do_limite():
    assert cifra_de_vigenere.encriptar_modo_varios_caracteres(['abc'], '˟˟˟˟') == '˟˟˟˟'
    assert cifra_de_vigenere.traduzir_modo_varios_caracteres(['abc'], '˟˟˟˟') == '˟˟˟˟'

def test_cifra_de_vigenere_varios_caracteres_maiusc_minusc():
    assert cifra_de_vigenere.encriptar_modo_varios_caracteres(['Aa'], 'AaaA') == 'bÅ¤¤'
    assert cifra_de_vigenere.traduzir_modo_varios_caracteres(['Aa'], 'bÅ¤¤') == 'AaaA'

def test_cifra_de_vigenere_varios_caracteres_verificar_andamento_com_caractere_acima_do_limite():
    assert cifra_de_vigenere.encriptar_modo_varios_caracteres(['!"'], 'a˟a˟a˟a') == 'b˟c˟b˟c'
    assert cifra_de_vigenere.traduzir_modo_varios_caracteres(['!"'], 'b˟c˟b˟c') == 'a˟a˟a˟a'

def test_cifra_de_vigenere_varios_caracteres_volta():
    assert cifra_de_vigenere.encriptar_modo_varios_caracteres(['!"'], '˞˝') == '  '
    assert cifra_de_vigenere.traduzir_modo_varios_caracteres(['!"'], '  ') == '˞˝'

def test_cifra_de_vigenere_varios_caracteres_texto_1():
    assert cifra_de_vigenere.encriptar_modo_varios_caracteres(['testando'],
    'Vamos ver como que essa cifra está funcionando ! Será que está trocando tudo ?'
    ) == 'ÍÉãæ×nÝ×éeÙæÑàdãìÍsÜ×äÈoÚÑÜéÅnÌåëĦsÝÙßÊÛæÖ×åÈàdpt»ÛéĢnØçÜeÛêØįdæé×ÙØÒÕÖoëÝÚæa°'
    assert cifra_de_vigenere.traduzir_modo_varios_caracteres(['testando'],
    'ÍÉãæ×nÝ×éeÙæÑàdãìÍsÜ×äÈoÚÑÜéÅnÌåëĦsÝÙßÊÛæÖ×åÈàdpt»ÛéĢnØçÜeÛêØįdæé×ÙØÒÕÖoëÝÚæa°'
    ) == 'Vamos ver como que essa cifra está funcionando ! Será que está trocando tudo ?'

def test_cifra_de_vigenere_varios_caracteres_texto_2():
    assert cifra_de_vigenere.encriptar_modo_varios_caracteres(['cháves diférentes!'],
    'Vamos testar agora com uma chave diferente, com espaços e acentos.'
    ) == '¼ÌĮèÛstÌßÝĪçeÒÞ×èbcÎİæeëmÈiÌıÖÞÖtÌßgËÝĦçÜÛ,dÏØĶrÍäçÉĺpÙhĦvÉÙeÕàØļ¢'
    assert cifra_de_vigenere.traduzir_modo_varios_caracteres(['cháves diférentes!'],
    '¼ÌĮèÛstÌßÝĪçeÒÞ×èbcÎİæeëmÈiÌıÖÞÖtÌßgËÝĦçÜÛ,dÏØĶrÍäçÉĺpÙhĦvÉÙeÕàØļ¢'
    ) == 'Vamos testar agora com uma chave diferente, com espaços e acentos.'
