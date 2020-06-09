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
    '''
    Função que adaptará a chave para o seu modo de tradução.
    Recebe como parâmetro uma chave, que será adaptada para a tradução.
    Recebe um parâmetro opcional, referente a que modo a chave deve ser adaptada (apenas letras ou vários caractéres).
    '''
    if testa_chave_cesar(chave):
        if todos_caracteres:  # Adaptar a chave para a tradução do modo todos caracteres.
            chave = valores.TAMANHO_ASCII - (int(chave) % valores.TAMANHO_ASCII)
        else:  # Adaptar a chave para a tradução do modo simples (apenas letras).
            chave = valores.TAMANHO_ALFABETO - (int(chave) % valores.TAMANHO_ALFABETO)
        return chave
    else:
        return False


def cesar_todos_caracteres(chave, mensagem, modo_traducao=False):
    '''
    Função que encripta a cifra de césar no modo vários caracteres.
    Recebe como chave um número inteiro não negativo.
    Recebe como mensagem uma string com um texto para ser encriptado ou traduzido.
    Parâmetro opcional define se será para fazer a tradução ou não.
    '''
    if not mensagem:
        return 'Mensagem inválida !'
    if modo_traducao:  # Se for modo tradução, será encaminhado para outra função.
        chave_antiga = chave
        chave = traduz_cesar(chave, todos_caracteres=True) % valores.TAMANHO_ASCII
        return traduz_todos_caracteres(chave_antiga, chave, mensagem)
    else:  # Se for modo encriptar, continuar nessa função para encriptar a mensagem.
        chave = testa_chave_cesar(chave)
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


def traduz_todos_caracteres(chave_antiga, chave_traduc, mensagem):
    '''
    Função que traduzirá a cifra de césar no modo de todos os caracteres.
    Chave antiga recebe o valor da chave antiga (a chave que não passou pela transformação para a tradução).
    Chave traduc. recebe a chave adaptada para a tradução.
    Mensagem recebe o valor da mensagem encriptada, que precisa ser traduzida.
    '''
    mensagem_traduzida = ''
    for letra in mensagem:
        letra_msg_atual = ord(letra)
        letra_ASCII = letra_msg_atual + chave_traduc
        verificar_volta = letra_msg_atual - int(chave_antiga)
        if letra_msg_atual > valores.INICIO_VAZIO and verificar_volta - valores.TAMANHO_ESPAÇO_VAZIO < valores.INICIO_ASCII:
            # Se a letra recebeu 2 vezes o número 34, é preciso voltar 34 na chave de tradução para não traduzir errado.
            letra_ASCII -= valores.TAMANHO_ESPAÇO_VAZIO
        if letra_msg_atual < valores.INICIO_VAZIO and verificar_volta > valores.INICIO_ASCII:
            letra_ASCII += valores.TAMANHO_ESPAÇO_VAZIO    
        if letra_ASCII > valores.FINAL_ASCII:  # O valor da letra atual a ser traduzida passou do valor final, hora de voltar para o ínicio.
            letra_ASCII -= valores.VOLTAR_PARA_INICIO
        mensagem_traduzida += chr(letra_ASCII)
    return mensagem_traduzida
