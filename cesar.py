import valores


def testa_chave_cesar(chave):  # Função validadora da chave.
    if chave.isnumeric():  # Se a chave for numérica(ou seja, ser um numero inteiro positivo) ela é valida.
        return True
    return False

def cifra_de_cesar(chave, mensagem):  # Função que traduz e encripta com cifra de cesar.
    chave_valida = testa_chave_cesar(chave)
    if not mensagem:
        return 'Mensagem invalida !'
    if chave_valida:
        mensagem_nova = ''
        chave = int(chave) % valores.TAMANHO_ALFABETO  # Diminuir o valor da chave para o número de letras existentes no alfabeto.
        for letra in mensagem:
            ascii_letra = ord(letra)
            ascii_soma = ascii_letra + chave
            if ascii_letra >= valores.MIN_MINUSCULA and ascii_letra <= valores.MAX_MINUSCULA:  # Criptografia para letras minusculas.
                if ascii_soma > valores.MAX_MINUSCULA:
                    ascii_soma = 96 + (ascii_soma - valores.MAX_MINUSCULA)  # O codigo ascii passou de 'z', então deve voltar ao inicio.
                mensagem_nova += chr(ascii_soma)
                continue
            if ascii_letra >= valores.MIN_MAIUSCULA and ascii_letra <= valores.MAX_MAIUSCULA:  # Criptografia para letras maiusculas.
                if ascii_soma > valores.MAX_MAIUSCULA:
                    ascii_soma = 64 + (ascii_soma - valores.MAX_MAIUSCULA)  # O codigo ascii passou de 'Z', então deve voltar ao inicio.
                mensagem_nova += chr(ascii_soma)
                continue
            # Se chegou até aqui, quer dizer que não é letra, então simplesmente adicionar esse caracter.
            mensagem_nova += letra
        return mensagem_nova
    else:
        return 'Chave Invalida !'


def traduz_cesar(chave, mensagem):
    if testa_chave_cesar(chave):
        # Tratamento da chave para a tradução.
        chave = valores.TAMANHO_ALFABETO - (int(chave) % valores.TAMANHO_ALFABETO)
        return cifra_de_cesar(str(chave), mensagem)
    else:
        return 'Chave Invalida !'


            