import Cifras.cifra_de_cesar as cifra_de_cesar
import Cifras.cifra_de_vigenere as cifra_de_vigenere


def apenas_letras(mensagem):  # Testa as 26 chaves possiveis da cifra de cesar em uma determinada mensagem.
    for chave in range(1, 27):
        mensagem_traduzida = cifra_de_cesar.traduzir_modo_apenas_letras([str(chave)], mensagem)
        imprimir_traduc_atual(chave, mensagem_traduzida)


def varios_caracteres(mensagem):
    for chave in range(1, 668):
        mensagem_traduzida = cifra_de_cesar.traduzir_modo_varios_caracteres([str(chave)], mensagem)
        imprimir_traduc_atual(chave, mensagem_traduzida)


def imprimir_traduc_atual(chave, mensagem_traduzida):
    print("\n-----------------------------------------------------")
    print(f'Testando chave: {chave}')
    print('Mensagem traduzida: ' + mensagem_traduzida)
    print('-----------------------------------------------------\n')
