import dicionarios

# Dicionário necessário para realizar as conversões na base hexadecimal.
dicionario_hexa = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8',
                   9:'9', 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F',
                   '0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
                   '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}

def transformar_texto_para_binario(mensagem):
    return retornar_texto_encriptado(mensagem, converter_decimal_para_binario)

def transformar_texto_para_octal(mensagem):
    return retornar_texto_encriptado(mensagem, converter_decimal_para_octal)

def transformar_texto_para_hexadecimal(mensagem):
    return retornar_texto_encriptado(mensagem, converter_decimal_para_hexadecimal)

def transformar_binario_para_texto(mensagem):
    return retornar_texto_traduzido(mensagem, converter_binario_para_decimal)

def transformar_octal_para_texto(mensagem):
    return retornar_texto_traduzido(mensagem, converter_octal_para_decimal)

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
        try:
            mensagem_traduzida += chr(funcao_tradutora(numero))
        except:
            return dicionarios.retorna_erro_mensagem()
    return mensagem_traduzida


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
            return 'Erro'
        numero_decimal += int(digito) * 2 ** potencia
    return numero_decimal


def converter_octal_para_decimal(numero_octal):
    numero_decimal = 0
    numero_octal = reversed(numero_octal)
    for potencia, digito in enumerate(numero_octal):
        if int(digito) < 0 or int(digito) > 7:
            return 'Erro'
        numero_decimal += int(digito) * 8 ** potencia
    return numero_decimal


def converter_hexadecimal_para_decimal(numero_hexadecimal):
    numero_decimal = 0
    numero_hexadecimal = reversed(numero_hexadecimal)
    for potencia, digito in enumerate(numero_hexadecimal):
        try:
            numero_decimal += dicionario_hexa[digito] * 16 ** potencia
        except:
            return 'Erro'
    return numero_decimal
