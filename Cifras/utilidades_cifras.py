MIN_MINUSCULA = 97

MAX_MINUSCULA= 122

MIN_MAIUSCULA = 65

MAX_MAIUSCULA = 90

TAMANHO_ALFABETO = 26

ALFABETO_MAIUSCULO = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

ALFABETO_MINUSCULO = 'abcdefghijklmnopqrstuvwxyz'

FINAL_UNICODE = 734

frequencia_alfabeto_pt = {'a': 14.63, 'e':12.57, 'o':10.73, 's':7.81, 'r':6.53, 'i':6.18, 'n':5.05, 'd':4.99,
                          'm':4.74, 'u':4.63, 't':4.34, 'c':3.88, 'l':2.78, 'p':2.52, 'v':1.67, 'g':1.3,
                          'h':1.28, 'q':1.20, 'b':1.04, 'f':1.02, 'z':0.47, 'j':0.4, 'x':0.21, 'k':0.02,
                          'y':0.01, 'w':0.01}


def criar_dicionario_caracteres_imprimiveis(limite):
    valor_atual = 0
    dicionario_unicode = {}
    for valor_unicode in range(32, limite + 1):
        if chr(valor_unicode).isprintable():
            dicionario_unicode[chr(valor_unicode)] = valor_atual
            dicionario_unicode[valor_atual] = chr(valor_unicode)
            valor_atual += 1
    return dicionario_unicode
