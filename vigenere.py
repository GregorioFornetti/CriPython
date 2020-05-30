import valores


def testa_chave_vigenere(chave):  # Função que testa se a chave fornecida pelo usuário é válida.
    chave = chave.lower().replace(' ', '')  # Apagar todos os espaços da chave.
    if chave.isalpha():  # Depois de retirar todos os espaços, verificar se o usuário digitou apenas letras.
        return chave
    return False
    

def vigenere(chave, mensagem):
    if not mensagem:
        return 'Mensagem inválida !'
    chave = testa_chave_vigenere(chave)
    tamanho_chave = len(chave)
    if chave:
        valor_atual_chave = 0
        mensagem_encriptada = ''
        for letra in mensagem:
            letra_cifrada = letra
            letra_ASCII = ord(letra)
            chave_ASCII = ord(chave[valor_atual_chave]) - valores.MIN_MINUSCULA
            if letra_ASCII >= valores.MIN_MINUSCULA and letra_ASCII <= valores.MAX_MINUSCULA:
                letra_ASCII -= valores.MIN_MINUSCULA
                index_alfabeto = (letra_ASCII + chave_ASCII) % 26
                letra_cifrada = valores.ALFABETO_MINUSCULO[index_alfabeto]
            elif letra_ASCII >= valores.MIN_MAIUSCULA and letra_ASCII <= valores.MAX_MAIUSCULA:
                letra_ASCII -= valores.MIN_MAIUSCULA
                index_alfabeto = (letra_ASCII + chave_ASCII) % 26
                letra_cifrada = valores.ALFABETO_MAIUSCULO[index_alfabeto]
            mensagem_encriptada += letra_cifrada
            valor_atual_chave += 1
            if valor_atual_chave >= tamanho_chave:
                valor_atual_chave = 0
    else:
        return 'Chave inválida !'
    return mensagem_encriptada         


def traduz_vigenere(chave, mensagem):
    if not mensagem:
        return 'Mensagem inválida !'
    chave = testa_chave_vigenere(chave)
    tamanho_chave = len(chave)
    if chave:
        valor_atual_chave = 0
        mensagem_traduzida = ''
        for letra in mensagem:
            letra_cifrada = letra
            letra_ASCII = ord(letra)
            chave_ASCII = ord(chave[valor_atual_chave]) - valores.MIN_MINUSCULA
            if letra_ASCII >= valores.MIN_MINUSCULA and letra_ASCII <= valores.MAX_MINUSCULA:
                letra_ASCII -= valores.MIN_MINUSCULA
                index_alfabeto = (letra_ASCII - chave_ASCII + 26) % 26
                letra_cifrada = valores.ALFABETO_MINUSCULO[index_alfabeto]
            elif letra_ASCII >= valores.MIN_MAIUSCULA and letra_ASCII <= valores.MAX_MAIUSCULA:
                letra_ASCII -= valores.MIN_MAIUSCULA
                index_alfabeto = (letra_ASCII - chave_ASCII + 26) % 26
                letra_cifrada = valores.ALFABETO_MAIUSCULO[index_alfabeto]
            mensagem_traduzida += letra_cifrada
            valor_atual_chave += 1
            if valor_atual_chave >= tamanho_chave:
                valor_atual_chave = 0
    else:
        return 'Chave inválida !'
    return mensagem_traduzida





