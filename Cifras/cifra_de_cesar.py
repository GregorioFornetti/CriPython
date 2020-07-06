import Cifras.valores as valores


def retorna_chave_se_for_valida(chave):  # Função validadora da chave.
    if chave.isnumeric():
        return chave
    return False


def encriptar_modo_apenas_letras(chave, mensagem):
    chave = retorna_chave_se_for_valida(chave)
    return mensagem_nova_modo_apenas_letras(chave, mensagem)


def traduzir_modo_apenas_letras(chave, mensagem):
    chave = adaptar_chave_para_traduçao_apenas_letras(chave)
    return mensagem_nova_modo_apenas_letras(chave, mensagem)


def mensagem_nova_modo_apenas_letras(chave, mensagem):
    if not mensagem:
        return 'Mensagem inválida !'
    if chave:
        return cesar_troca_apenas_letras(chave, mensagem)
    else:
        return 'Chave Invalida !'


def adaptar_chave_para_traduçao_apenas_letras(chave):  # Adaptar a chave para a tradução, caso ela seja válida.
    chave = retorna_chave_se_for_valida(chave)
    if chave:
        chave = valores.TAMANHO_ALFABETO - (int(chave) % valores.TAMANHO_ALFABETO)
    return chave


def cesar_troca_apenas_letras(chave, mensagem):
    mensagem_nova = ''
    chave = int(chave) % valores.TAMANHO_ALFABETO  # Diminuir o valor da chave para o número de letras existentes no alfabeto.
    for letra in mensagem:
        ascii_letra = ord(letra)
        ascii_soma = ascii_letra + chave
        if ascii_letra >= valores.MIN_MINUSCULA and ascii_letra <= valores.MAX_MINUSCULA:
            if ascii_soma > valores.MAX_MINUSCULA:
                ascii_soma = 96 + (ascii_soma - valores.MAX_MINUSCULA)  # O codigo ascii passou de 'z', então deve voltar ao inicio.
            mensagem_nova += chr(ascii_soma)
            continue
        if ascii_letra >= valores.MIN_MAIUSCULA and ascii_letra <= valores.MAX_MAIUSCULA:  # Criptografia para letras maiusculas.
            if ascii_soma > valores.MAX_MAIUSCULA:
                ascii_soma = 64 + (ascii_soma - valores.MAX_MAIUSCULA)  # O codigo ascii passou de 'Z', então deve voltar ao inicio.
            mensagem_nova += chr(ascii_soma)
            continue
        mensagem_nova += letra  # Caso a mensagem tenha caracteres especiais ou caracteres com acentos, eles serão adicionados sem mudanças.
    return mensagem_nova


def encriptar_modo_varios_caracteres(chave, mensagem):
    if not mensagem:
        return "Mensagem Inválida !"
    chave = retorna_chave_se_for_valida(chave)
    if chave:
        nova_mensagem = ''
        chave = int(chave) % valores.TAMANHO_UNICODE
        for letra in mensagem:
            letra_UNICODE = ord(letra) + chave
            if letra_UNICODE > valores.FINAL_UNICODE:  # Chegou ao final da tabela, portanto é hora de voltar ao início.
                letra_UNICODE -= valores.TAMANHO_UNICODE
            if not chr(letra_UNICODE).isprintable():
                letra_UNICODE += valores.TAMANHO_ESPAÇO_VAZIO
            nova_mensagem += chr(letra_UNICODE)
        return nova_mensagem
    else:
        return "Chave Inválida !"


def traduzir_modo_varios_caracteres(chave, mensagem):
    if not mensagem:
        return "Mensagem Inválida !"
    chave_traduc = adaptar_chave_para_traduçao_varios_caracteres(chave)
    if chave_traduc:
        nova_mensagem = ''
        chave = int(chave) % valores.TAMANHO_UNICODE
        for letra in mensagem:
            letra_UNICODE = ord(letra) + chave_traduc
            if letra_UNICODE > valores.FINAL_UNICODE:  # Chegou ao final da tabela, portanto é hora de voltar ao início.
                letra_UNICODE -= valores.TAMANHO_UNICODE
            if not chr(ord(letra) - valores.TAMANHO_UNICODE).isprintable() and ord(letra) - chave < 161:
                letra_UNICODE -= valores.TAMANHO_ESPAÇO_VAZIO
            nova_mensagem += chr(letra_UNICODE)
        return nova_mensagem
    else:
        return "Chave Inválida !"


def mensagem_nova_modo_varios_caracteres(chave, mensagem):
    if not mensagem:
        return "Mensagem inválida !"
    if chave:
        return cesar_troca_varios_caracteres(chave, mensagem)
    else:
        return "Chave inválida !"


def cesar_troca_varios_caracteres_encript(chave, mensagem):
    nova_mensagem = ''
    chave = int(chave) % valores.TAMANHO_UNICODE
    for letra in mensagem:
        letra_UNICODE = ord(letra) + chave
        if letra_UNICODE > valores.FINAL_UNICODE:  # Chegou ao final da tabela, portanto é hora de voltar ao início.
            letra_UNICODE -= valores.TAMANHO_UNICODE
        if not chr(letra_UNICODE).isprintable():
            letra_UNICODE += valores.TAMANHO_ESPAÇO_VAZIO
        nova_mensagem += chr(letra_UNICODE)
    return nova_mensagem


def adaptar_chave_para_traduçao_varios_caracteres(chave):
    chave = retorna_chave_se_for_valida(chave)
    if chave:
        chave = valores.TAMANHO_UNICODE - (int(chave) % valores.TAMANHO_UNICODE)
    return chave
