import Cifras.cifra_de_cesar as cifra_de_cesar

def forca_bruta_cesar(mensagem):  # Testa as 26 chaves possiveis da cifra de cesar em uma determinada mensagem.
    for chave in range(1, 27):
        print("\n-----------------------------------------------------")
        print(f'Testando chave: {chave}')
        print('Mensagem traduzida: ' + cifra_de_cesar.traduzir_modo_apenas_letras(str(chave), mensagem))
        print('-----------------------------------------------------\n')
