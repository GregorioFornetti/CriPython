import dicionarios
import Cifras.utilidades_cifras as utilidades_cifras

# Dicionário necessário para realizar as conversões na base hexadecimal.
dicionario_hexa_decimal = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8',
                   9:'9', 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F',
                   '0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
                   '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}

dicionario_hexa_bin = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5': '0101',
                       '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
                       'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111', '0000': '0', '0001': '1',
                       '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7',
                       '1000': '8', '1001': '9', '1010': 'A', '1011': 'B', '1100': 'C', '1101': 'D',
                       '1110': 'E', '1111': 'F'}

dicionario_octal_bin = {'0': '000', '1': '001', '2': '010', '3': '011', '4': '100', '5': '101', '6': '110', '7': '111',
                        '000': '0', '001': '1', '010': '2', '011': '3', '100': '4', '101': '5', '110': '6', '111': '7'}

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

def verificar_num_decimal(numero_decimal):
    if not numero_decimal:
        return False
    
    lista_decimal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for digito_decimal in numero_decimal:
        if digito_decimal not in lista_decimal:
            return False
    return int(numero_decimal)

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
        valor_hexadecimal = dicionario_hexa_decimal[numero_decimal % 16] + valor_hexadecimal
        numero_decimal = int(numero_decimal / 16)
    return valor_hexadecimal


def verificar_num_bin(numero_binario):
    if not numero_binario:
        return False
    
    lista_binario = ['0', '1']
    for digito_binario in numero_binario:
        if digito_binario not in lista_binario:
            return False
    return True

def converter_binario_para_octal(numero_binario):
    numero_octal = ''
    numero_binario = '0' * ((3 - len(numero_binario) % 3) % 3) + numero_binario
    for i in range(2, len(numero_binario), 3):
        numero_octal += dicionario_octal_bin[numero_binario[i-2] + numero_binario[i-1] + numero_binario[i]]
    return numero_octal

def converter_binario_para_decimal(numero_binario):
    numero_decimal = 0
    numero_binario = reversed(numero_binario)  # Inverter o número para começar da direita para a esquerda (da menor base para a maior).
    for potencia, digito in enumerate(numero_binario):
        if int(digito) < 0 or int(digito) > 1:  # O numero lido não é um número binário.
            return False
        numero_decimal += int(digito) * 2 ** potencia
    return numero_decimal

def converter_binario_para_hexadecimal(numero_binario):
    numero_hexadecimal = ''
    numero_binario = '0' * ((4 - len(numero_binario) % 4) % 4) + numero_binario
    for i in range(3, len(numero_binario), 4):
        numero_hexadecimal += dicionario_hexa_bin[numero_binario[i-3] + numero_binario[i-2] + numero_binario[i-1] + numero_binario[i]]
    return numero_hexadecimal


def verificar_num_octal(numero_octal):
    if not numero_octal:
        return False
    
    lista_octal = ['0', '1', '2', '3', '4', '5', '6', '7']
    for digito_octal in numero_octal:
        if digito_octal not in lista_octal:
            return False
    return True

def converter_octal_para_binario(numero_octal, tirar_zeros_esquerda=True):
    numero_binario = ''
    for digito_octal in numero_octal:
        numero_binario += dicionario_octal_bin[digito_octal]
    
    if tirar_zeros_esquerda:
        numero_binario = numero_binario.lstrip('0')
        if not numero_binario:  # Tirou todos os 0 existentes (colocar apenas um para não retornar uma string vazia)
            numero_binario = '0'
    return numero_binario

def converter_octal_para_decimal(numero_octal):
    numero_decimal = 0
    numero_octal = reversed(numero_octal)
    for potencia, digito in enumerate(numero_octal):
        if int(digito) < 0 or int(digito) > 7:
            return False
        numero_decimal += int(digito) * 8 ** potencia
    return numero_decimal

def converter_octal_para_hexadecimal(numero_octal):
    numero_binario = converter_octal_para_binario(numero_octal)
    return converter_binario_para_hexadecimal(numero_binario)


def verificar_num_hexadecimal(numero_hexadecimal):
    if not numero_hexadecimal:
        return False

    lista_hexa = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    for digito_hexa in numero_hexadecimal.upper():
        if digito_hexa not in lista_hexa:
            return False
    return True

def converter_hexadecimal_para_binario(numero_hexadecimal, tirar_zeros_esquerda=True):
    numero_binario = ''
    for digito_hexa in numero_hexadecimal.upper():
        numero_binario += dicionario_hexa_bin[digito_hexa]
    
    if tirar_zeros_esquerda:
        numero_binario = numero_binario.lstrip('0')
        if not numero_binario:
            numero_binario = '0'
    return numero_binario

def converter_hexadecimal_para_decimal(numero_hexadecimal):
    numero_hexadecimal = numero_hexadecimal.upper()
    numero_decimal = 0
    numero_hexadecimal = reversed(numero_hexadecimal)
    for potencia, digito in enumerate(numero_hexadecimal):
        try:
            numero_decimal += dicionario_hexa_decimal[digito] * 16 ** potencia
        except:
            return False
    return numero_decimal

def converter_hexadecimal_para_octal(numero_hexadecimal):
    numero_binario = converter_hexadecimal_para_binario(numero_hexadecimal.upper())
    return converter_binario_para_octal(numero_binario)
