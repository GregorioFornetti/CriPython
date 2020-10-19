import Cifras.utf8 as utf8
import dicionarios


def test_utf8_mensagem_invalida_vazia():
    assert utf8.codificar_texto_para_UTF8('') == dicionarios.retorna_erro_mensagem()
    assert utf8.decodificar_UTF8_para_texto('') == dicionarios.retorna_erro_mensagem()

def test_utf8_mensagem_invalida_tamanho_invalida():
    assert utf8.decodificar_UTF8_para_texto('1010101') == dicionarios.retorna_erro_mensagem()

def test_utf8_mensagem_invalida_codificacao_incorreta():
    assert utf8.decodificar_UTF8_para_texto('10101110') == dicionarios.retorna_erro_mensagem()

def test_utf8_mensagem_invalida_nao_binaria_1():
    assert utf8.decodificar_UTF8_para_texto('10123') == dicionarios.retorna_erro_mensagem()

def test_utf8_mensagem_invalida_nao_binaria_2():
    assert utf8.decodificar_UTF8_para_texto('101011ab') == dicionarios.retorna_erro_mensagem()

def test_utf8_7bits():
    assert utf8.codificar_texto_para_UTF8('a') == '01100001'
    assert utf8.decodificar_UTF8_para_texto('01100001') == 'a'

def test_utf8_11bits():
    assert utf8.codificar_texto_para_UTF8('¥') == '1100001010100101'
    assert utf8.decodificar_UTF8_para_texto('1100001010100101') == '¥'

def test_utf8_16bits():
    assert utf8.codificar_texto_para_UTF8('ऍ') == '111000001010010010001101'
    assert utf8.decodificar_UTF8_para_texto('111000001010010010001101') == 'ऍ'

def test_utf8_21bits():
    assert utf8.codificar_texto_para_UTF8('𐓉') == '11110000100100001001001110001001'
    assert utf8.decodificar_UTF8_para_texto('11110000100100001001001110001001') == '𐓉'

def test_utf8_texto_grande_1():
    assert utf8.codificar_texto_para_UTF8('opa eai tudo bem ?'
    ) == '011011110111000001100001001000000110010101100001011010010010000001110100011101010110010001101111001000000110001001100101011011010010000000111111'

    assert utf8.decodificar_UTF8_para_texto('011011110111000001100001001000000110010101100001011010010010000001110100011101010110010001101111001000000110001001100101011011010010000000111111'
    ) == 'opa eai tudo bem ?'

def test_utf8_texto_grande_2():
    assert utf8.codificar_texto_para_UTF8('Cóm carácteres especiais'
    ) == '0100001111000011101100110110110100100000011000110110000101110010110000111010000101100011011101000110010101110010011001010111001100100000011001010111001101110000011001010110001101101001011000010110100101110011'

    assert utf8.decodificar_UTF8_para_texto('0100001111000011101100110110110100100000011000110110000101110010110000111010000101100011011101000110010101110010011001010111001100100000011001010111001101110000011001010110001101101001011000010110100101110011'
    ) == 'Cóm carácteres especiais'

def test_utf8_texto_grande_3():
    assert utf8.codificar_texto_para_UTF8('Teste: ౻óaU౻౻ႫaáoíႫჇჇaí'
    ) == '0101010001100101011100110111010001100101001110100010000011100000101100011011101111000011101100110110000101010101111000001011000110111011111000001011000110111011111000011000001010101011011000011100001110100001011011111100001110101101111000011000001010101011111000011000001110000111111000011000001110000111011000011100001110101101'

    assert utf8.decodificar_UTF8_para_texto('0101010001100101011100110111010001100101001110100010000011100000101100011011101111000011101100110110000101010101111000001011000110111011111000001011000110111011111000011000001010101011011000011100001110100001011011111100001110101101111000011000001010101011111000011000001110000111111000011000001110000111011000011100001110101101'
    ) == 'Teste: ౻óaU౻౻ႫaáoíႫჇჇaí'