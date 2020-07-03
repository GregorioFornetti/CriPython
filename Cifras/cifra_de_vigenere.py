import Cifras.valores as valores


def testa_chave_vigenere(chave):  # Função que testa se a chave fornecida pelo usuário é válida.
    chave = chave.lower().replace(' ', '')  # Apagar todos os espaços da chave.
    if chave.isalpha():  # Depois de retirar todos os espaços, verificar se o usuário digitou apenas letras.
        return chave
    return False


def encriptar_modo_apenas_letras(chave, mensagem):  # Função que traduz/encripta a mensagem pela cifra de Vigenère.
    chave = testa_chave_vigenere(chave)
    return mensagem_nova_modo_apenas_letras(chave, mensagem)  


def traduzir_modo_apenas_letras(chave, mensagem):
    chave = adaptar_chave_para_traducao_apenas_letras(chave)
    return mensagem_nova_modo_apenas_letras(chave, mensagem)


def mensagem_nova_modo_apenas_letras(chave, mensagem):
    if not mensagem:
        return 'Mensagem inválida !'
    if chave:
        return vigenere_troca_apenas_letras(chave, mensagem)
    else:
        return 'Chave Invalida !'


def vigenere_troca_apenas_letras(chave, mensagem):
    tamanho_chave = len(chave)
    valor_atual_chave = 0
    mensagem_nova = ''
    for letra in mensagem:
        letra_cifrada = letra
        letra_ASCII = ord(letra)  # Valor ASCII da letra atual da mensagem.
        chave_ASCII = ord(chave[valor_atual_chave]) - valores.MIN_MINUSCULA  # Valor alfabético (0-25, A=0, B=1,...) da letra da chave atual. 
        if letra_ASCII >= valores.MIN_MINUSCULA and letra_ASCII <= valores.MAX_MINUSCULA:  # Casos de letras minusculas.
            letra_ASCII -= valores.MIN_MINUSCULA
            index_alfabeto = (letra_ASCII + chave_ASCII) % 26  # Juntar os valores da letra da chave e da mensagem. (OBS: não pode passar de 26, que é o mesmo que dar uma volta no alfabeto).
            letra_cifrada = valores.ALFABETO_MINUSCULO[index_alfabeto]  # Pegar a letra com o valor alfabético calculado pelo index_alfabeto.
            valor_atual_chave += 1  # Mover a letra da chave em uma casa.
        elif letra_ASCII >= valores.MIN_MAIUSCULA and letra_ASCII <= valores.MAX_MAIUSCULA:  # Casos de letras maiusculas.
            letra_ASCII -= valores.MIN_MAIUSCULA
            index_alfabeto = (letra_ASCII + chave_ASCII) % 26
            letra_cifrada = valores.ALFABETO_MAIUSCULO[index_alfabeto]
            valor_atual_chave += 1  # Mover a letra da chave em uma casa.
        mensagem_nova += letra_cifrada
        if valor_atual_chave >= tamanho_chave:  # Se a chave chegou ao final, voltar para o início.
            valor_atual_chave = 0
    return mensagem_nova


def adaptar_chave_para_traducao_apenas_letras(chave):  # Função que adapta a chave para a tradução.
    chave = testa_chave_vigenere(chave)
    if chave:
        chave_traduc = ''
        for letra in chave:
            letra_ASCII = ord(letra) - valores.MIN_MINUSCULA
            if letra_ASCII == 0:
                chave_traduc += valores.ALFABETO_MINUSCULO[0]
                continue
            letra_atual = 26 - letra_ASCII  # Para transformar a chave, basta subtrair 26 com o antigo valor da chave (isso fará com que a mensagem de uma "volta" e volte ao normal).
            chave_traduc += valores.ALFABETO_MINUSCULO[letra_atual]
        return chave_traduc
    else:
        return False


def adaptar_chave_para_traducao_varias_letras(chave):
    '''
    Função que cria a chave de tradução de vigenere para várias letras.
    A função recebe como parâmetro uma chave, que será adaptada para a tradução.
    '''
    chave_traduc = []
    for letra in chave:  # Adaptando a chave.
        # Cada letra da nova chave tem um código que completa o valor da chave antiga até chegar a dar uma volta.
        ASCII_atual = ord(letra)
        novo_valor = (valores.TAMANHO_ASCII - (ASCII_atual % valores.TAMANHO_ASCII))
        chave_traduc.append(novo_valor)
    return chave_traduc


def encriptar_modo_varios_caracteres(chave, mensagem):
    '''
    Função que encriptará a mensagem com a cifra de vigenere no modo várias letras.
    Recebe como parâmetros uma chave (string), mensagem(string) e modo_traducao(bool).
    '''
    if not mensagem:
        return 'Mensagem inválida !'
    chave_atual = 0
    if chave:
        tamanho_chave = len(chave)
        mensagem_nova = ''
        for letra in mensagem:
            chave_ASCII = ord(chave[chave_atual]) % valores.TAMANHO_ASCII
            letra_ASCII = ord(letra) + chave_ASCII
            if letra_ASCII > valores.FINAL_ASCII - valores.TAMANHO_ESPAÇO_VAZIO:  # Valor passou do valor final, então é hora de voltar para o início da tabela.
                letra_ASCII -= (valores.VOLTAR_PARA_INICIO - valores.TAMANHO_ESPAÇO_VAZIO)
            if letra_ASCII >= valores.INICIO_VAZIO:  # Passou da região vazia, então deve receber 34 ao seu valor final.
                letra_ASCII += valores.TAMANHO_ESPAÇO_VAZIO
            chave_atual += 1  # Atualizar index da chave.
            if chave_atual >= tamanho_chave:  # Voltar ao inicio da chave caso a chave passe de seu valor máximo.
                chave_atual = 0
            mensagem_nova += chr(letra_ASCII)
        return mensagem_nova
    else:
        return 'Chave inválida !'


def traduzir_modo_varios_caracteres(chave, mensagem):
    valor_atual = 0
    chave_traduc = adaptar_chave_para_traducao_varias_letras(chave)
    tamanho_chave = len(chave)
    mensagem_traduzida = ''
    for letra in mensagem:
        letra_msg_atual = ord(letra)
        letra_ASCII = letra_msg_atual + chave_traduc[valor_atual]
        verificar_volta = letra_msg_atual - ord(chave[valor_atual])
        if letra_msg_atual > valores.INICIO_VAZIO and verificar_volta - valores.TAMANHO_ESPAÇO_VAZIO < valores.INICIO_ASCII:
            # Antiga letra na mensagem recebeu 34 a mais para sua pontuação, então precisa corrigir agora para a tradução.
            letra_ASCII -= valores.TAMANHO_ESPAÇO_VAZIO
        if letra_msg_atual < valores.INICIO_VAZIO and verificar_volta > valores.INICIO_ASCII:
            letra_ASCII += valores.TAMANHO_ESPAÇO_VAZIO
        if letra_ASCII > valores.FINAL_ASCII:  # Chegou ao valor final da tabela, então é hora de voltar ao início da tabela.
            letra_ASCII -= valores.VOLTAR_PARA_INICIO
        valor_atual += 1  # Atualizar index da chave.
        if valor_atual >= tamanho_chave:  # Voltar ao inicio da chave caso a chave passe de seu valor máximo.
            valor_atual = 0
        mensagem_traduzida += chr(letra_ASCII)
    return mensagem_traduzida
