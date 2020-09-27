import Cifras.cifra_de_cesar as cifra_de_cesar
import Cifras.cifra_de_vigenere as cifra_de_vigenere
import dicionarios

def imprimir_apenas_letras(mensagem):
    lista_mensagens_apenas_letras = apenas_letras(mensagem)
    if lista_mensagens_apenas_letras:
        for num_chave, mensagem in enumerate(apenas_letras(mensagem)):
            print(dicionarios.retorna_mensagens_forca_bruta_cesar(num_chave + 1, mensagem))
    else:
        print(dicionarios.retorna_mensagem_com_bordas(dicionarios.retorna_erro_mensagem(), 127))

def imprimir_varios_caracteres(mensagem):
    lista_mensagens_varios_caracteres = varios_caracteres(mensagem)
    if lista_mensagens_varios_caracteres:
        for num_chave, mensagem in enumerate(varios_caracteres(mensagem)):
            print(dicionarios.retorna_mensagens_forca_bruta_cesar(num_chave + 1, mensagem))
    else:
        print(dicionarios.retorna_mensagem_com_bordas(dicionarios.retorna_erro_mensagem(), 127))


def apenas_letras(mensagem):  # Testa as 26 chaves possiveis da cifra de cesar em uma determinada mensagem.
    if not mensagem:
        return False
    lista_mensagens_possiveis = []
    for chave in range(1, 27):
        mensagem_traduzida = cifra_de_cesar.traduzir_modo_apenas_letras([str(chave)], mensagem)
        lista_mensagens_possiveis.append(mensagem_traduzida)
    return lista_mensagens_possiveis


def varios_caracteres(mensagem):
    if not mensagem:
        return False
    lista_mensagens_possiveis = []
    for chave in range(1, 669):
        mensagem_traduzida = cifra_de_cesar.traduzir_modo_varios_caracteres([str(chave)], mensagem)
        lista_mensagens_possiveis.append(mensagem_traduzida)
    return lista_mensagens_possiveis
