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
    '''
    Função que encripta a cifra de césar no modo vários caracteres.
    Recebe como chave um número inteiro não negativo.
    Recebe como mensagem uma string com um texto para ser encriptado ou traduzido.
    Parâmetro opcional define se será para fazer a tradução ou não.
    '''
    if not mensagem:
        return 'Mensagem inválida !'
    chave = retorna_chave_se_for_valida(chave)
    if chave:
        nova_mensagem = ''
        chave = int(chave) % valores.TAMANHO_ASCII
        for letra in mensagem:
            letra_ASCII = ord(letra) + chave
            if letra_ASCII > valores.FINAL_ASCII - valores.TAMANHO_ESPAÇO_VAZIO:  # Chegou ao final da tabela, portanto é hora de voltar ao início.
                letra_ASCII -= (valores.VOLTAR_PARA_INICIO - valores.TAMANHO_ESPAÇO_VAZIO)
            if letra_ASCII >= valores.INICIO_VAZIO:  # O caractere atual já passou da "região vazia", portanto deve aumentar em 34 o seu código.
                letra_ASCII += valores.TAMANHO_ESPAÇO_VAZIO
            nova_mensagem += chr(letra_ASCII)
        return nova_mensagem
    else:
        return 'Chave inválida !'


def traduzir_modo_varios_caracteres(chave, mensagem):
    '''
    Função que traduzirá a cifra de césar no modo de todos os caracteres.
    Chave antiga recebe o valor da chave antiga (a chave que não passou pela transformação para a tradução).
    Chave traduc. recebe a chave adaptada para a tradução.
    Mensagem recebe o valor da mensagem encriptada, que precisa ser traduzida.
    '''
    if not mensagem:
        return 'Mensagem inválida !'
    chave_traduc = adaptar_chave_para_traduçao_varios_caracteres(chave)
    if chave:
        mensagem_traduzida = ''
        for letra in mensagem:
            letra_msg_atual = ord(letra)
            letra_ASCII = letra_msg_atual + chave_traduc
            verificar_volta = letra_msg_atual - int(chave)
            if letra_msg_atual > valores.INICIO_VAZIO and verificar_volta - valores.TAMANHO_ESPAÇO_VAZIO < valores.INICIO_ASCII:
                # Se a letra recebeu 2 vezes o número 34, é preciso voltar 34 na chave de tradução para não traduzir errado.
                letra_ASCII -= valores.TAMANHO_ESPAÇO_VAZIO
            if letra_msg_atual < valores.INICIO_VAZIO and verificar_volta > valores.INICIO_ASCII:
                # Se a letra não passou da "região não imprimível" é preciso somar mais 34 no caractere traduzido para sair certo.
                letra_ASCII += valores.TAMANHO_ESPAÇO_VAZIO    
            if letra_ASCII > valores.FINAL_ASCII:  # O valor da letra atual a ser traduzida passou do valor final, hora de voltar para o ínicio.
                letra_ASCII -= valores.VOLTAR_PARA_INICIO
            mensagem_traduzida += chr(letra_ASCII)
        return mensagem_traduzida
    else:
        return 'Chave inválida !'


def adaptar_chave_para_traduçao_varios_caracteres(chave):
    chave = retorna_chave_se_for_valida(chave)
    if chave:
        chave = valores.TAMANHO_ASCII - (int(chave) % valores.TAMANHO_ASCII)
    return chave
