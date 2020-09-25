import Cifras.cifra_de_cesar as cifra_de_cesar
import Cifras.cifra_de_vigenere as cifra_de_vigenere
import dicionarios


def apenas_letras(mensagem):  # Testa as 26 chaves possiveis da cifra de cesar em uma determinada mensagem.
    for chave in range(1, 27):
        mensagem_traduzida = cifra_de_cesar.traduzir_modo_apenas_letras([str(chave)], mensagem)
        print(dicionarios.retorna_mensagens_forca_bruta_cesar(chave, mensagem_traduzida))


def varios_caracteres(mensagem):
    for chave in range(1, 668):
        mensagem_traduzida = cifra_de_cesar.traduzir_modo_varios_caracteres([str(chave)], mensagem)
        print(dicionarios.retorna_mensagens_forca_bruta_cesar(chave, mensagem_traduzida))

