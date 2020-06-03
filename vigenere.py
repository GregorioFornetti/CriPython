import valores


def testa_chave_vigenere(chave):  # Função que testa se a chave fornecida pelo usuário é válida.
    chave = chave.lower().replace(' ', '')  # Apagar todos os espaços da chave.
    if chave.isalpha():  # Depois de retirar todos os espaços, verificar se o usuário digitou apenas letras.
        return chave
    return False
    

def vigenere(chave, mensagem, modo_traducao=False):  # Função que traduz/encripta a mensagem pela cifra de Vigenère.
    if not mensagem:  # Se o usuário não escreveu uma mensagem, retornar uma mensagem de erro !
        return 'Mensagem inválida !'
    if modo_traducao:
        chave = cria_chave_traducao(chave)
    else:
        chave = testa_chave_vigenere(chave)
    tamanho_chave = len(chave)
    if chave:
        valor_atual_chave = 0
        mensagem_encriptada = ''
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
            mensagem_encriptada += letra_cifrada
            if valor_atual_chave >= tamanho_chave:  # Se a chave chegou ao final, voltar para o início.
                valor_atual_chave = 0
    else:  # Se a chave é inválida, retornar uma mensagem de erro.
        return 'Chave inválida !'
    return mensagem_encriptada         


def cria_chave_traducao(chave):  # Função que adapta a chave para a tradução.
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
        return 'Chave inválida !'




