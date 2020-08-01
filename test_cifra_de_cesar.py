import Cifras.cifra_de_cesar as cifra_de_cesar
'''
Arquivo de testes automatizados !
Para testar o programa, é preciso que a biblioteca PyTest esteja instalada em seu computador.
Para instalar, execute no terminal: pip install -U pytest
Depois disso, coloque o terminal para rodar na pasta principal do programa e execute
o comando: pytest
'''


# Opção: APENAS LETRAS
def test_cifra_de_cesar_apenas_letras_chave_1():
    assert cifra_de_cesar.encriptar_modo_apenas_letras(['1'],'abc') == 'bcd'
    assert cifra_de_cesar.traduzir_modo_apenas_letras(['1'], 'bcd') == 'abc'

def test_cifra_de_cesar_apenas_letras_chave_invalida_vazia():
    assert cifra_de_cesar.encriptar_modo_apenas_letras([''], 'abc') == cifra_de_cesar.erro_chave
    assert cifra_de_cesar.encriptar_modo_apenas_letras([''], 'abc') == cifra_de_cesar.erro_chave

def test_cifra_de_cesar_apenas_letras_chave_invalida_negativa():
    assert cifra_de_cesar.encriptar_modo_apenas_letras(['-1'], 'a') == cifra_de_cesar.erro_chave
    assert cifra_de_cesar.traduzir_modo_apenas_letras(['-1'], 'a') == cifra_de_cesar.erro_chave

def test_cifra_de_cesar_apenas_letras_chave_invalida_texto():
    assert cifra_de_cesar.encriptar_modo_apenas_letras(['texto'], 'a') == cifra_de_cesar.erro_chave
    assert cifra_de_cesar.traduzir_modo_apenas_letras(['texto'], 'a') == cifra_de_cesar.erro_chave

def test_cifra_de_cesar_apenas_letras_chave_invalida_naointeiro():
    assert cifra_de_cesar.encriptar_modo_apenas_letras(['1.2'], 'a') == cifra_de_cesar.erro_chave
    assert cifra_de_cesar.traduzir_modo_apenas_letras(['2.4'], 'a') == cifra_de_cesar.erro_chave

def test_cifra_de_cesar_apenas_letras_mensagem_invalida():
    assert cifra_de_cesar.encriptar_modo_apenas_letras(['1'], '') == cifra_de_cesar.erro_mensagem
    assert cifra_de_cesar.traduzir_modo_apenas_letras(['1'], '') == cifra_de_cesar.erro_mensagem

def test_cifra_de_cesar_apenas_letras_volta_alfabeto():
    assert cifra_de_cesar.encriptar_modo_apenas_letras(['1'], 'z') == 'a'
    assert cifra_de_cesar.traduzir_modo_apenas_letras(['1'], 'a') == 'z'

def test_cifra_de_cesar_apenas_letras_maiusc_minusc():
    assert cifra_de_cesar.encriptar_modo_apenas_letras(['1'], 'aAbBcCdD') == 'bBcCdDeE'
    assert cifra_de_cesar.traduzir_modo_apenas_letras(['1'], 'bBcCdDeE') == 'aAbBcCdD'

def test_cifra_de_cesar_apenas_letras_caracteres_especiais():
    assert cifra_de_cesar.encriptar_modo_apenas_letras(['1'], 'áéíóú!? aeiou') == 'áéíóú!? bfjpv'
    assert cifra_de_cesar.traduzir_modo_apenas_letras(['1'], 'áéíóú!? bfjpv') == 'áéíóú!? aeiou'

def test_cifra_de_cesar_apenas_letras_chave_maior():
    assert cifra_de_cesar.encriptar_modo_apenas_letras(['10'], 'az') == 'kj'
    assert cifra_de_cesar.traduzir_modo_apenas_letras(['10'], 'kj') == 'az'

def test_cifra_de_cesar_apenas_letras_texto_grande_1():
    assert cifra_de_cesar.encriptar_modo_apenas_letras(['1'], 
    'abcdefghijklmnopqrstuvwxyz') == 'bcdefghijklmnopqrstuvwxyza'
    assert cifra_de_cesar.traduzir_modo_apenas_letras(['1'], 
    'bcdefghijklmnopqrstuvwxyza') == 'abcdefghijklmnopqrstuvwxyz'

def test_cifra_de_cesar_apenas_letras_texto_grande_2():
    assert cifra_de_cesar.encriptar_modo_apenas_letras(['7'],
    'Bom dia, Boa tarde, Boa noite!') == 'Ivt kph, Ivh ahykl, Ivh uvpal!'
    assert cifra_de_cesar.traduzir_modo_apenas_letras(['7'],
    'Ivt kph, Ivh ahykl, Ivh uvpal!') == 'Bom dia, Boa tarde, Boa noite!'


# OPÇÃO: VÁRIOS CARACTERES
def test_cifra_de_cesar_varios_caracteres_chave_1():
    assert cifra_de_cesar.encriptar_modo_varios_caracteres(['1'], 'a') == 'b'
    assert cifra_de_cesar.traduzir_modo_varios_caracteres(['1'], 'b') == 'a'

def test_cifra_de_cesar_varios_caracteres_chave_invalida_vazia():
    assert cifra_de_cesar.encriptar_modo_varios_caracteres([''], 'abc') == cifra_de_cesar.erro_chave
    assert cifra_de_cesar.traduzir_modo_varios_caracteres([''], 'abc') == cifra_de_cesar.erro_chave

def test_cifra_de_cesar_varios_caracteres_chave_invalida_negativa():
    assert cifra_de_cesar.encriptar_modo_varios_caracteres(['-1'], 'a') == cifra_de_cesar.erro_chave
    assert cifra_de_cesar.traduzir_modo_varios_caracteres(['-1'], 'a') == cifra_de_cesar.erro_chave

def test_cifra_de_cesar_varios_caracteres_chave_invalida_texto():
    assert cifra_de_cesar.encriptar_modo_varios_caracteres(['texto'], 'a') == cifra_de_cesar.erro_chave
    assert cifra_de_cesar.traduzir_modo_varios_caracteres(['texto'], 'a') == cifra_de_cesar.erro_chave

def test_cifra_de_cesar_varios_caracteres_chave_invalida_naointeiro():
    assert cifra_de_cesar.encriptar_modo_varios_caracteres(['1.2'], 'a') == cifra_de_cesar.erro_chave
    assert cifra_de_cesar.traduzir_modo_varios_caracteres(['1.2'], 'a') == cifra_de_cesar.erro_chave

def test_cifra_de_cesar_varios_caracteres_mensagem_invalida():
    assert cifra_de_cesar.encriptar_modo_varios_caracteres(['1'], '') == cifra_de_cesar.erro_mensagem
    assert cifra_de_cesar.traduzir_modo_varios_caracteres(['1'], '') == cifra_de_cesar.erro_mensagem

def test_cifra_de_cesar_varios_caracteres_volta():
    assert cifra_de_cesar.encriptar_modo_varios_caracteres(['1'], '˞˝') == ' ˞'
    assert cifra_de_cesar.traduzir_modo_varios_caracteres(['1'],' ˞') == '˞˝'

def test_cifra_de_cesar_varios_caracteres_maiusc_minus():
    assert cifra_de_cesar.encriptar_modo_varios_caracteres(['1'], 'aAbBcCdD') == 'bBcCdDeE'
    assert cifra_de_cesar.traduzir_modo_varios_caracteres(['1'], 'bBcCdDeE') == 'aAbBcCdD'

def test_cifra_de_cesar_varios_caracteres_caracteres_especiais():
    assert cifra_de_cesar.encriptar_modo_varios_caracteres(['1'], 'áéíóú!? abc') == 'âêîôû"@!bcd'
    assert cifra_de_cesar.traduzir_modo_varios_caracteres(['1'], 'âêîôû"@!bcd') == 'áéíóú!? abc'

def test_cifra_de_cesar_varios_caracteres_acima_do_limite():
    assert cifra_de_cesar.encriptar_modo_varios_caracteres(['1'], '˟') == '˟'
    assert cifra_de_cesar.traduzir_modo_varios_caracteres(['1'], '˟') == '˟'

def test_cifra_de_cesar_varios_caracteres_chave_maior():
    assert cifra_de_cesar.encriptar_modo_varios_caracteres(['123'], 'a') == 'ÿ'
    assert cifra_de_cesar.traduzir_modo_varios_caracteres(['123'], 'ÿ') == 'a'

def test_cifra_de_cesar_varios_caracteres_texto_grande_1():
    assert cifra_de_cesar.encriptar_modo_varios_caracteres(['123'],
    'Olá ! Será que troca letras com acentos também ? E espaços ? Vamos testar agora !'
    ) == 'íĊŜ¾¿¾ñăĐŜ¾ďēă¾ĒĐčāÿ¾ĊăĒĐÿđ¾āčċ¾ÿāăČĒčđ¾ĒÿċĀŤċ¾Ý¾ã¾ăđĎÿŢčđ¾Ý¾ôÿċčđ¾ĒăđĒÿĐ¾ÿąčĐÿ¾¿'
    assert cifra_de_cesar.traduzir_modo_varios_caracteres(['123'],
    'íĊŜ¾¿¾ñăĐŜ¾ďēă¾ĒĐčāÿ¾ĊăĒĐÿđ¾āčċ¾ÿāăČĒčđ¾ĒÿċĀŤċ¾Ý¾ã¾ăđĎÿŢčđ¾Ý¾ôÿċčđ¾ĒăđĒÿĐ¾ÿąčĐÿ¾¿'
    ) == 'Olá ! Será que troca letras com acentos também ? E espaços ? Vamos testar agora !'

def test_cifra_de_cesar_apenas_letras_enript_texto_grande_2():
    assert cifra_de_cesar.encriptar_modo_varios_caracteres(['321'],
    'Legal ! Parece que está tudo funcionando corretamente, vamos ver como o texto fica movendo mais ainda !!!'
    ) == 'ưǉǋǅǐƄƅƄƴǅǖǉǇǉƄǕǙǉƄǉǗǘȢƄǘǙǈǓƄǊǙǒǇǍǓǒǅǒǈǓƄǇǓǖǖǉǘǅǑǉǒǘǉƐƄǚǅǑǓǗƄǚǉǖƄǇǓǑǓƄǓƄǘǉǜǘǓƄǊǍǇǅƄǑǓǚǉǒǈǓƄǑǅǍǗƄǅǍǒǈǅƄƅƅƅ'
    assert cifra_de_cesar.traduzir_modo_varios_caracteres(['321'],
    'ưǉǋǅǐƄƅƄƴǅǖǉǇǉƄǕǙǉƄǉǗǘȢƄǘǙǈǓƄǊǙǒǇǍǓǒǅǒǈǓƄǇǓǖǖǉǘǅǑǉǒǘǉƐƄǚǅǑǓǗƄǚǉǖƄǇǓǑǓƄǓƄǘǉǜǘǓƄǊǍǇǅƄǑǓǚǉǒǈǓƄǑǅǍǗƄǅǍǒǈǅƄƅƅƅ'
    ) == 'Legal ! Parece que está tudo funcionando corretamente, vamos ver como o texto fica movendo mais ainda !!!'
