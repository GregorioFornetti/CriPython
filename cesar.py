import valores


def testa_chave_cesar(chave):  # Função validadora da chave.
    if chave.isnumeric():  # Se a chave for numérica(ou seja, ser um numero inteiro positivo) ela é valida.
        return chave
    return False

def cifra_de_cesar(chave, mensagem, modo_traducao=False):  # Função que traduz e encripta com cifra de cesar.
    if modo_traducao:
        chave = traduz_cesar(chave)
    else:
        chave = testa_chave_cesar(chave)
    if not mensagem:
        return 'Mensagem invalida !'
    if chave:
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


def traduz_cesar(chave, todos_caracteres=False):
    if testa_chave_cesar(chave):
        # Tratamento da chave para a tradução.
        if todos_caracteres:
            chave = valores.TAMANHO_ASCII - (int(chave) % valores.TAMANHO_ASCII)
            print(chave)
        else:    
            chave = valores.TAMANHO_ALFABETO - (int(chave) % valores.TAMANHO_ALFABETO)
        return chave
    else:
        return False


def cesar_todos_caracteres(chave, mensagem, modo_traducao=False):
    if not mensagem:
        return 'Mensagem inválida !'
    if modo_traducao:
        chave = traduz_cesar(chave, todos_caracteres=True)
    else:
        chave = testa_chave_cesar(chave)
    if chave:
        nova_mensagem = ''
        chave = int(chave) % valores.TAMANHO_ASCII
        for letra in mensagem:
            letra_ASCII = ord(letra) + chave
            if modo_traducao and letra_ASCII >= 127:
                letra_ASCII -= 34
            if letra_ASCII > valores.FINAL_ASCII - 34:
                letra_ASCII -= (224 - 34)
            if letra_ASCII >= 127:  # Caractere não imprimivel (del), desconsidera-lo da lista ASCII.
                letra_ASCII += 34
            nova_mensagem += chr(letra_ASCII)
        return nova_mensagem
    else:
        return 'Chave inválida !'


for i in range(256, 501):
    print(i)
    print(chr(i))