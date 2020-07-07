
def criar_dicionario_caracteres_imprimiveis(limite):
    valor_atual = 0
    dicionario_unicode = {}
    for valor_unicode in range(32, limite + 1):
        if chr(valor_unicode).isprintable():
            dicionario_unicode[chr(valor_unicode)] = valor_atual
            dicionario_unicode[valor_atual] = chr(valor_unicode)
            valor_atual += 1
        else:
            print(valor_unicode)
    return dicionario_unicode

dic = criar_dicionario_caracteres_imprimiveis(733)
print(len(dic)//2)