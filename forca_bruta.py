import cesar


def forca_bruta_cesar(mensagem):  # Testa as 26 chaves possiveis da cifra de cesar em uma determinada mensagem.
    for chave in range(1, 27):
        print(f'Testando chave: {chave}')
        print(cesar.cifra_de_cesar(str(chave), mensagem, modo_traducao=True))