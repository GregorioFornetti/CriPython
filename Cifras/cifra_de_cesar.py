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
    dic_unicode = criar_dicionario_caracteres_imprimiveis(733)
    chave = retorna_chave_se_for_valida(chave)
    return mensagem_nova_modo_varios_caracteres(chave, mensagem, dic_unicode)


def traduzir_modo_varios_caracteres(chave, mensagem):
    dic_unicode = criar_dicionario_caracteres_imprimiveis(733)
    chave = adaptar_chave_para_traduçao_varios_caracteres(chave, dic_unicode)
    return mensagem_nova_modo_varios_caracteres(chave, mensagem, dic_unicode)


def criar_dicionario_caracteres_imprimiveis(limite):
    valor_atual = 0
    dicionario_unicode = {}
    for valor_unicode in range(32, limite + 1):
        if chr(valor_unicode).isprintable():
            dicionario_unicode[chr(valor_unicode)] = valor_atual
            dicionario_unicode[valor_atual] = chr(valor_unicode)
            valor_atual += 1
    return dicionario_unicode


def mensagem_nova_modo_varios_caracteres(chave, mensagem, dic_unicode):
    if not mensagem:
        return "Mensagem inválida !"
    if chave:
        return cesar_troca_varios_caracteres(chave, mensagem, dic_unicode)
    else:
        return "Chave inválida !"


def cesar_troca_varios_caracteres(chave, mensagem, dic_unicode):
    tot_caracteres_imprimiveis = len(dic_unicode) // 2
    chave = int(chave) % tot_caracteres_imprimiveis
    nova_mensagem = ''
    for letra in mensagem:
        valor_unicode_nova_letra = dic_unicode[letra] + chave
        if valor_unicode_nova_letra >= tot_caracteres_imprimiveis:
            valor_unicode_nova_letra -= tot_caracteres_imprimiveis
        nova_mensagem += dic_unicode[valor_unicode_nova_letra]
    return nova_mensagem


def adaptar_chave_para_traduçao_varios_caracteres(chave, dic_unicode):
    tot_valores_imprimiveis = len(dic_unicode) // 2
    chave = retorna_chave_se_for_valida(chave)
    if chave:
        chave = tot_valores_imprimiveis - (int(chave) % tot_valores_imprimiveis)
    return chave
