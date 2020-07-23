import Cifras.subst_simples as subst_simples
'''
Arquivo de testes automatizados !
Para testar o programa, é preciso que a biblioteca PyTest esteja instalada em seu computador.
Para instalar, execute no terminal: pip install -U pytest
Depois disso, coloque o terminal para rodar na pasta principal do programa e execute
o comando: pytest
'''


# OPÇÃO: APENAS LETRAS
def test_subst_simples_apenas_letras_troca_1_letra():
    assert subst_simples.encriptar_modo_apenas_letras(['a', 'b'], 'abcdef') == 'bacdef'
    assert subst_simples.traduzir_modo_apenas_letras(['a', 'b'], 'bacdef') == 'abcdef'

def test_subst_simples_apenas_letras_chave_invalida_vazia():
    assert subst_simples.encriptar_modo_apenas_letras(['', ''], 'abc') == 'Chave inválida !'
    assert subst_simples.traduzir_modo_apenas_letras(['', ''], 'abc') == 'Chave inválida !'

def test_subst_simples_apenas_letras_chave_invalida_caractere_especial_1():
    assert subst_simples.encriptar_modo_apenas_letras(['!?1', 'abc'], 'abcde') == 'Chave inválida !'
    assert subst_simples.traduzir_modo_apenas_letras(['!?1', 'abc'], 'abcde') == 'Chave inválida !'

def test_subst_simples_apenas_letras_chave_invalida_caractere_especial_2():
    assert subst_simples.encriptar_modo_apenas_letras(['abc', '!?1'], 'abcde') == 'Chave inválida !'
    assert subst_simples.traduzir_modo_apenas_letras(['abc', '!?1'], 'abcde') == 'Chave inválida !'

def test_subst_simples_apenas_letras_chave_invalida_duplicada_1():
    assert subst_simples.encriptar_modo_apenas_letras(['aAb', 'bed'], 'abcde') == 'Chave inválida !'
    assert subst_simples.traduzir_modo_apenas_letras(['aAb', 'bed'], 'abcde') == 'Chave inválida !'

def test_subst_simples_apenas_letras_chave_invalida_duplicada_2():
    assert subst_simples.encriptar_modo_apenas_letras(['bed', 'aAb'], 'abcde') == 'Chave inválida !'
    assert subst_simples.traduzir_modo_apenas_letras(['bed', 'aAb'], 'abcde') == 'Chave inválida !'

def test_subst_simples_apenas_letras_chave_invalida_tamanho_diferentes_1():
    assert subst_simples.encriptar_modo_apenas_letras(['abc', 'tg'], 'abcde') == 'Chave inválida !'
    assert subst_simples.traduzir_modo_apenas_letras(['abc', 'tg'], 'abcde') == 'Chave inválida !'

def test_subst_simples_apenas_letras_chave_invalida_tamanho_diferente_2():
    assert subst_simples.encriptar_modo_apenas_letras(['tg', 'abc'], 'abcde') == 'Chave inválida !'
    assert subst_simples.traduzir_modo_apenas_letras(['tg', 'abc'], 'abcde') == 'Chave inválida !'

def test_subst_simples_apenas_letras_mensagem_invalida():
    assert subst_simples.encriptar_modo_apenas_letras(['ab', 'tg'], '') == 'Mensagem inválida !'
    assert subst_simples.traduzir_modo_apenas_letras(['ab', 'tg'], '') == 'Mensagem inválida !'

def test_subst_simples_apenas_letras_maiusc_minusc():
    assert subst_simples.encriptar_modo_apenas_letras(['a', 'b'], 'aA') == 'bB'
    assert subst_simples.traduzir_modo_apenas_letras(['a', 'b'], 'bB') == 'aA'

def test_subst_simples_apenas_letras_caracter_especial_mensagem():
    assert subst_simples.encriptar_modo_apenas_letras(['abc', 'def'], '!?.^123 oi') == '!?.^123 oi'
    assert subst_simples.traduzir_modo_apenas_letras(['abc', 'def'], '!?.^123 oi') == '!?.^123 oi'

def test_subst_simples_apenas_letras_troca_mais_caracteres():
    assert subst_simples.encriptar_modo_apenas_letras(['bcdat', 'opqrz'], 'atenção amigos !') == 'rzençãb rmigbs !'
    assert subst_simples.traduzir_modo_apenas_letras(['bcdat', 'opqrz'], 'rzençãb rmigbs !') == 'atenção amigos !'

def test_subst_simples_apenas_letras_texto_maior_1():
    assert subst_simples.encriptar_modo_apenas_letras(['abcdefghijklmnopqrstuvwxyz', 'fhizdlmnavgewptubxjrqocsky'],
    'Tudo bem com voce ?') == 'Rqzt hdw itw otid ?'
    assert subst_simples.traduzir_modo_apenas_letras(['abcdefghijklmnopqrstuvwxyz', 'fhizdlmnavgewptubxjrqocsky'],
    'Rqzt hdw itw otid ?') == 'Tudo bem com voce ?'

def test_subst_simples_apenas_letras_texto_maior_2():
    assert subst_simples.encriptar_modo_apenas_letras(['abcdefghijklmnopqrstuvwxyz', 'neruzjxpgfabcowvdqyihtslmk'],
    'Por favor, me responda !') == 'Vwq jntwq, cz qzyvwoun !'
    assert subst_simples.traduzir_modo_apenas_letras(['abcdefghijklmnopqrstuvwxyz', 'neruzjxpgfabcowvdqyihtslmk'],
    'Vwq jntwq, cz qzyvwoun !') == 'Por favor, me responda !'


# OPÇÃO: VÁRIOS CARACTERES
def test_subst_simples_varios_caracteres_troca_1_letra():
    assert subst_simples.encriptar_modo_varios_caracteres(['a', 'b'], 'abcdef') == 'bacdef'
    assert subst_simples.traduzir_modo_varios_caracteres(['a', 'b'], 'bacdef') == 'abcdef'

def test_subst_simples_varios_caracteres_chave_invalida_vazia():
    assert subst_simples.encriptar_modo_varios_caracteres(['', ''], 'abc') == 'Chave inválida !'
    assert subst_simples.traduzir_modo_varios_caracteres(['', ''], 'abc') == 'Chave inválida !'

def test_subst_simples_varios_caracteres_chave_invalida_caractere_especial_1():
    assert subst_simples.encriptar_modo_varios_caracteres(['!?1', 'abc'], 'abcde!?1') == '!?1deabc'
    assert subst_simples.traduzir_modo_varios_caracteres(['!?1', 'abc'], '!?1deabc') == 'abcde!?1'

def test_subst_simples_varios_caracteres_chave_invalida_caractere_especial_2():
    assert subst_simples.encriptar_modo_varios_caracteres(['abc', '!?1'], 'abcde!?1') == '!?1deabc'
    assert subst_simples.traduzir_modo_varios_caracteres(['abc', '!?1'], '!?1deabc') == 'abcde!?1'

def test_subst_simples_varios_caracteres_chave_invalida_duplicada_1():
    assert subst_simples.encriptar_modo_varios_caracteres(['aAb', 'bed'], 'abcde') == 'Chave inválida !'
    assert subst_simples.traduzir_modo_varios_caracteres(['aAb', 'bed'], 'bdcbA') == 'Chave inválida !'

def test_subst_simples_varios_caracteres_chave_invalida_duplicada_2():
    assert subst_simples.encriptar_modo_varios_caracteres(['bed', 'aAb'], 'abcde') == 'Chave inválida !'
    assert subst_simples.traduzir_modo_varios_caracteres(['bed', 'aAb'], 'bacbA') == 'Chave inválida !'

def test_subst_simples_varios_caracteres_chave_invalida_tamanho_diferentes_1():
    assert subst_simples.encriptar_modo_varios_caracteres(['abc', 'tg'], 'abcde') == 'Chave inválida !'
    assert subst_simples.traduzir_modo_varios_caracteres(['abc', 'tg'], 'abcde') == 'Chave inválida !'

def test_subst_simples_varios_caracteres_chave_invalida_tamanho_diferente_2():
    assert subst_simples.encriptar_modo_varios_caracteres(['tg', 'abc'], 'abcde') == 'Chave inválida !'
    assert subst_simples.traduzir_modo_varios_caracteres(['tg', 'abc'], 'abcde') == 'Chave inválida !'

def test_subst_simples_varios_caracteres_mensagem_invalida():
    assert subst_simples.encriptar_modo_varios_caracteres(['ab', 'tg'], '') == 'Mensagem inválida !'
    assert subst_simples.traduzir_modo_varios_caracteres(['abc', 'tg'], '') == 'Mensagem inválida !'

def test_subst_simples_varios_caracteres_maiusc_minusc():
    assert subst_simples.encriptar_modo_varios_caracteres(['a', 'b'], 'aA') == 'bA'
    assert subst_simples.traduzir_modo_varios_caracteres(['a', 'b'], 'bA') == 'aA'

def test_subst_simples_varios_caracteres_caracter_especial_mensagem():
    assert subst_simples.encriptar_modo_varios_caracteres(['abc', 'def'], '!?.^123 oi') == '!?.^123 oi'
    assert subst_simples.traduzir_modo_varios_caracteres(['abc', 'def'], '!?.^123 oi') == '!?.^123 oi'

def test_subst_simples_varios_caracteres_troca_mais_caracteres():
    assert subst_simples.encriptar_modo_varios_caracteres(['bcdat', 'opqrz'], 'atenção amigos !') == 'rzençãb rmigbs !'
    assert subst_simples.traduzir_modo_varios_caracteres(['bcdat', 'opqrz'], 'rzençãb rmigbs !') == 'atenção amigos !'

def test_subst_simples_varios_caracteres_texto_maior_1():
    assert subst_simples.encriptar_modo_varios_caracteres(['abcdefghijklmnopqrstuvwxyz', 'fhizdlmnavgewptubxjrqocsky'],
    'Ué ? Esse exemplo não é igual ao da cifra de substituição simples no modo apenas letras ? Não, as maiusculas não serão trocadas se você não pedir!'
    ) == 'Ué ? Ejjd dsdwuet pãt é amqfe ft zf ialxf zd jqhjrarqaçãt jawuedj pt wtzt fudpfj edrxfj ? Nãt, fj wfaqjiqefj pãt jdxãt rxtifzfj jd otiê pãt udzax!'
    assert subst_simples.traduzir_modo_varios_caracteres(['abcdefghijklmnopqrstuvwxyz', 'fhizdlmnavgewptubxjrqocsky'],
    'Ué ? Ejjd dsdwuet pãt é amqfe ft zf ialxf zd jqhjrarqaçãt jawuedj pt wtzt fudpfj edrxfj ? Nãt, fj wfaqjiqefj pãt jdxãt rxtifzfj jd otiê pãt udzax!'
    ) == 'Ué ? Esse exemplo não é igual ao da cifra de substituição simples no modo apenas letras ? Não, as maiusculas não serão trocadas se você não pedir!'

def test_subst_simples_apenas_letras_texto_maior_2():
    assert subst_simples.encriptar_modo_varios_caracteres(['abcdefghijklmnopqrstuvwxyz !?.,', 'qwertyuiopasdfghjklzxcvbnm!., ?'],
    'Vamos trocar outros caracteres agora ! Testando, 1, 2, 3 ... Funcionou ?'
    ) == 'Vqdgl!zkgeqk!gxzkgl!eqkqeztktl!qugkq!.!Ttlzqfrg?!1?!2?!3!   !Fxfeogfgx!,'
    assert subst_simples.traduzir_modo_varios_caracteres(['abcdefghijklmnopqrstuvwxyz !?.,', 'qwertyuiopasdfghjklzxcvbnm!., ?'],
    'Vqdgl!zkgeqk!gxzkgl!eqkqeztktl!qugkq!.!Ttlzqfrg?!1?!2?!3!   !Fxfeogfgx!,'
    ) == 'Vamos trocar outros caracteres agora ! Testando, 1, 2, 3 ... Funcionou ?'
