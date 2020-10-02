import dicionarios
import Cifras.utilidades_cifras as utilidades_cifras

# Dicionário necessário para realizar as conversões na base hexadecimal.
dicionario_hexa = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8',
                   9:'9', 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F',
                   '0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
                   '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}

dicionario_hexa_bin = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5': '0101',
                       '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'a': '1010', 'b': '1011',
                       'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'}

def transformar_texto_para_binario(mensagem):
    return retornar_texto_encriptado(mensagem, converter_decimal_para_binario)

def transformar_texto_para_octal(mensagem):
    return retornar_texto_encriptado(mensagem, converter_decimal_para_octal)

def transformar_texto_para_decimal(mensagem):
    return retornar_texto_encriptado(mensagem, converter_para_decimal)

def transformar_texto_para_hexadecimal(mensagem):
    return retornar_texto_encriptado(mensagem, converter_decimal_para_hexadecimal)

def transformar_binario_para_texto(mensagem):
    return retornar_texto_traduzido(mensagem, converter_binario_para_decimal)

def transformar_octal_para_texto(mensagem):
    return retornar_texto_traduzido(mensagem, converter_octal_para_decimal)

def transformar_decimal_para_texto(mensagem):
    return retornar_texto_traduzido(mensagem, verificar_num_decimal)

def transformar_hexadecimal_para_texto(mensagem):
    return retornar_texto_traduzido(mensagem, converter_hexadecimal_para_decimal)

def retornar_texto_encriptado(mensagem, funcao_encriptadora):
    if not mensagem:
        return dicionarios.retorna_erro_mensagem()
    mensagem_encriptada = ''
    for caractere in mensagem:
        mensagem_encriptada += funcao_encriptadora(ord(caractere)) + ' '
    return mensagem_encriptada.strip()


def retornar_texto_traduzido(mensagem, funcao_tradutora):
    if not mensagem:
        return dicionarios.retorna_erro_mensagem()
    mensagem_traduzida = ''
    for numero in mensagem.split():
        valor_UNICODE = funcao_tradutora(numero)
        if not valor_UNICODE or valor_UNICODE >= utilidades_cifras.LIMITE_UNICODE_PYTHON: 
            # Ocorreu um erro na troca da base númerica escolhida para a base decimal.
            return dicionarios.retorna_erro_mensagem()
        mensagem_traduzida += chr(valor_UNICODE)
    return mensagem_traduzida


def converter_para_decimal(numero_decimal):
    return str(numero_decimal)

def converter_decimal_para_binario(numero_decimal):
    valor_binario = ''
    while numero_decimal != 0:
        valor_binario = str(numero_decimal % 2) + valor_binario
        numero_decimal = int(numero_decimal / 2)
    return valor_binario


def converter_decimal_para_octal(numero_decimal):
    valor_octal = ''
    while numero_decimal != 0:
        valor_octal = str(numero_decimal % 8) + valor_octal
        numero_decimal = int(numero_decimal / 8)
    return valor_octal


def converter_decimal_para_hexadecimal(numero_decimal):
    valor_hexadecimal = ''
    while numero_decimal != 0:
        valor_hexadecimal = dicionario_hexa[numero_decimal % 16] + valor_hexadecimal
        numero_decimal = int(numero_decimal / 16)
    return valor_hexadecimal


def converter_binario_para_decimal(numero_binario):
    numero_decimal = 0
    numero_binario = reversed(numero_binario)  # Inverter o número para começar da direita para a esquerda (da menor base para a maior).
    for potencia, digito in enumerate(numero_binario):
        if int(digito) < 0 or int(digito) > 1:  # O numero lido não é um número binário.
            return False
        numero_decimal += int(digito) * 2 ** potencia
    return numero_decimal


def converter_octal_para_decimal(numero_octal):
    numero_decimal = 0
    numero_octal = reversed(numero_octal)
    for potencia, digito in enumerate(numero_octal):
        if int(digito) < 0 or int(digito) > 7:
            return False
        numero_decimal += int(digito) * 8 ** potencia
    return numero_decimal


def converter_hexadecimal_para_decimal(numero_hexadecimal):
    numero_decimal = 0
    numero_hexadecimal = reversed(numero_hexadecimal)
    for potencia, digito in enumerate(numero_hexadecimal):
        try:
            numero_decimal += dicionario_hexa[digito] * 16 ** potencia
        except:
            return False
    return numero_decimal

def converter_hexa_para_binario(codigo_hexa):
    return dicionario_hexa_bin[codigo_hexa]

def verificar_num_decimal(numero_decimal):
    try:
        return int(numero_decimal)
    except:
        return False