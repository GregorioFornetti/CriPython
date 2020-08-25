import Cifras.bases_numericas as bases_numericas
import dicionarios
'''
Arquivo de testes automatizados !
Para testar o programa, é preciso que a biblioteca PyTest esteja instalada em seu computador.
Para instalar, execute no terminal: pip install -U pytest
Depois disso, coloque o terminal para rodar na pasta principal do programa e execute
o comando: pytest
'''

# BINÁRIO
def test_binario_trocar_um_caractere_minusculo():
    assert bases_numericas.transformar_texto_para_binario('a') == '1100001'
    assert bases_numericas.transformar_binario_para_texto('1100001') == 'a'

def test_binario_trocar_um_caractere_maiusculo():
    assert bases_numericas.transformar_texto_para_binario('A') == '1000001'
    assert bases_numericas.transformar_binario_para_texto('1000001') == 'A'

def test_binario_trocar_um_caractere_especial():
    assert bases_numericas.transformar_texto_para_binario('á') == '11100001'
    assert bases_numericas.transformar_binario_para_texto('11100001') == 'á'

def test_binario_traducao_invalido_1():
    assert bases_numericas.transformar_binario_para_texto('1111210') == dicionarios.retorna_erro_mensagem()

def test_binario_traducao_invalido_2():
    assert bases_numericas.transformar_binario_para_texto('1111111111111111111111111') == dicionarios.retorna_erro_mensagem()

def test_binario_mensagem_invalida():
    assert bases_numericas.transformar_texto_para_binario('') == dicionarios.retorna_erro_mensagem()
    assert bases_numericas.transformar_binario_para_texto('') == dicionarios.retorna_erro_mensagem()

def test_binario_texto_grande_1():
    assert bases_numericas.transformar_texto_para_binario('Primeiro texto em binário'
    ) == '1010000 1110010 1101001 1101101 1100101 1101001 1110010 1101111 100000 1110100 1100101 1111000 1110100 1101111 100000 1100101 1101101 100000 1100010 1101001 1101110 11100001 1110010 1101001 1101111'

    assert bases_numericas.transformar_binario_para_texto(
    '1010000 1110010 1101001 1101101 1100101 1101001 1110010 1101111 100000 1110100 1100101 1111000 1110100 1101111 100000 1100101 1101101 100000 1100010 1101001 1101110 11100001 1110010 1101001 1101111'
    ) == 'Primeiro texto em binário'

def test_binario_texto_grande_2():
    assert bases_numericas.transformar_texto_para_binario('Caracteres especiais:*Ü¡˟ɮ'
    ) == '1000011 1100001 1110010 1100001 1100011 1110100 1100101 1110010 1100101 1110011 100000 1100101 1110011 1110000 1100101 1100011 1101001 1100001 1101001 1110011 111010 101010 11011100 10100001 1011011111 1001101110'

    assert bases_numericas.transformar_binario_para_texto(
    '1000011 1100001 1110010 1100001 1100011 1110100 1100101 1110010 1100101 1110011 100000 1100101 1110011 1110000 1100101 1100011 1101001 1100001 1101001 1110011 111010 101010 11011100 10100001 1011011111 1001101110'
    ) == 'Caracteres especiais:*Ü¡˟ɮ'


# OCTAL
def test_octal_trocar_um_caractere_minusculo():
    assert bases_numericas.transformar_texto_para_octal('a') == '141'
    assert bases_numericas.transformar_octal_para_texto('141') == 'a'

def test_octal_trocar_um_caractere_maiusculo():
    assert bases_numericas.transformar_texto_para_octal('A') == '101'
    assert bases_numericas.transformar_octal_para_texto('101') == 'A'

def test_octal_trocar_um_caractere_especial():
    assert bases_numericas.transformar_texto_para_octal('á') == '341'
    assert bases_numericas.transformar_octal_para_texto('341') == 'á'

def test_octal_traducao_invalido_1():
    assert bases_numericas.transformar_octal_para_texto('1238') == dicionarios.retorna_erro_mensagem()

def test_octal_traducao_invalido_2():
    assert bases_numericas.transformar_octal_para_texto('77777777777') == dicionarios.retorna_erro_mensagem()

def test_octal_mensagem_invalida():
    assert bases_numericas.transformar_texto_para_octal('') == dicionarios.retorna_erro_mensagem()
    assert bases_numericas.transformar_octal_para_texto('') == dicionarios.retorna_erro_mensagem()

def test_octal_texto_grande_1():
    assert bases_numericas.transformar_texto_para_octal('Primeiro texto em octal'
    ) == '120 162 151 155 145 151 162 157 40 164 145 170 164 157 40 145 155 40 157 143 164 141 154'

    assert bases_numericas.transformar_octal_para_texto(
    '120 162 151 155 145 151 162 157 40 164 145 170 164 157 40 145 155 40 157 143 164 141 154'
    ) == 'Primeiro texto em octal'

def test_octal_texto_grande_2():
    assert bases_numericas.transformar_texto_para_octal('Caracteres especiais:*Ü¡˟ɮ'
    ) == '103 141 162 141 143 164 145 162 145 163 40 145 163 160 145 143 151 141 151 163 72 52 334 241 1337 1156'

    assert bases_numericas.transformar_octal_para_texto(
    '103 141 162 141 143 164 145 162 145 163 40 145 163 160 145 143 151 141 151 163 72 52 334 241 1337 1156'
    ) == 'Caracteres especiais:*Ü¡˟ɮ'


# HEXADECIMAL
def test_hexadecimal_trocar_um_caractere_minusculo():
    assert bases_numericas.transformar_texto_para_hexadecimal('a') == '61'
    assert bases_numericas.transformar_hexadecimal_para_texto('61') == 'a'

def test_hexadecimal_trocar_um_caractere_maiusculo():
    assert bases_numericas.transformar_texto_para_hexadecimal('A') == '41'
    assert bases_numericas.transformar_hexadecimal_para_texto('41') == 'A'

def test_hexadecimal_trocar_um_caractere_especial():
    assert bases_numericas.transformar_texto_para_hexadecimal('á') == 'E1'
    assert bases_numericas.transformar_hexadecimal_para_texto('E1') == 'á'

def test_hexadecimal_traducao_invalido_1():
    assert bases_numericas.transformar_hexadecimal_para_texto('1ABCDEFG') == dicionarios.retorna_erro_mensagem()

def test_hexadecimal_traducao_invalido_2():
    assert bases_numericas.transformar_hexadecimal_para_texto('FFFFFFFFF') == dicionarios.retorna_erro_mensagem()

def test_hexadecimal_mensagem_invalida():
    assert bases_numericas.transformar_texto_para_hexadecimal('') == dicionarios.retorna_erro_mensagem()
    assert bases_numericas.transformar_hexadecimal_para_texto('') == dicionarios.retorna_erro_mensagem()

def test_hexadecimal_texto_grande_1():
    assert bases_numericas.transformar_texto_para_hexadecimal('Primeiro texto em hexadecimal'
    ) == '50 72 69 6D 65 69 72 6F 20 74 65 78 74 6F 20 65 6D 20 68 65 78 61 64 65 63 69 6D 61 6C'

    assert bases_numericas.transformar_hexadecimal_para_texto(
    '50 72 69 6D 65 69 72 6F 20 74 65 78 74 6F 20 65 6D 20 68 65 78 61 64 65 63 69 6D 61 6C'
    ) == 'Primeiro texto em hexadecimal'

def test_hexadecimal_texto_grande_2():
    assert bases_numericas.transformar_texto_para_hexadecimal('Caracteres especiais:*Ü¡˟ɮ'
    ) == '43 61 72 61 63 74 65 72 65 73 20 65 73 70 65 63 69 61 69 73 3A 2A DC A1 2DF 26E'

    assert bases_numericas.transformar_hexadecimal_para_texto(
    '43 61 72 61 63 74 65 72 65 73 20 65 73 70 65 63 69 61 69 73 3A 2A DC A1 2DF 26E'
    ) == 'Caracteres especiais:*Ü¡˟ɮ'
