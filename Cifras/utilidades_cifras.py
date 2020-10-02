MIN_MINUSCULA = 97

MAX_MINUSCULA= 122

MIN_MAIUSCULA = 65

MAX_MAIUSCULA = 90

TAMANHO_ALFABETO = 26

ALFABETO_MAIUSCULO = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

ALFABETO_MINUSCULO = 'abcdefghijklmnopqrstuvwxyz'

FINAL_UNICODE = 734

LIMITE_UNICODE_PYTHON = 1114112

def criar_dicionario_caracteres_imprimiveis(limite):
    valor_atual = 0
    dicionario_unicode = {}
    for valor_unicode in range(32, limite + 1):
        if chr(valor_unicode).isprintable():
            dicionario_unicode[chr(valor_unicode)] = valor_atual
            dicionario_unicode[valor_atual] = chr(valor_unicode)
            valor_atual += 1
    return dicionario_unicode


def verificar_se_string_possui_apenas_letras(texto):
    for caractere in texto:
        valor_UNICODE = ord(caractere)
        if valor_UNICODE < MIN_MAIUSCULA or (valor_UNICODE > MAX_MAIUSCULA and valor_UNICODE < MIN_MINUSCULA) or valor_UNICODE > MAX_MINUSCULA:
            return False
    return True
