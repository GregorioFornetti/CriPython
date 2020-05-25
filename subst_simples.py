import valores


def teste_chave_substSimples(chave):  # Verifica se a chave é valida.
    chave = chave.lower()
    if len(chave) != valores.TAMANHO_ALFABETO:  # A chave para ser valida tem que ter um tamanho de 26 caracteres.
        return False
    for char in chave:  # E a chave não pode ter caracteres repetidos.
        ascii_letra = ord(char)
        if chave.count(char) >= 2:
            return False
        if not(ascii_letra >= valores.MIN_MINUSCULA and ascii_letra <= valores.MAX_MINUSCULA):
            return False
    return True


def subst_simples(chave, mensagem):  # Função que traduz/encripta através da "substituição simples".
    chave_valida = teste_chave_substSimples(chave)
    if not mensagem:
        return 'Mensagem Invalida !'
    mensagem_nova = ''
    if chave_valida:
        for letra in mensagem:
            ascii_letra = ord(letra)  # Pega o valor ASCII da letra atual da mensagem.
            if ascii_letra >= valores.MIN_MAIUSCULA and ascii_letra <= valores.MAX_MAIUSCULA:  # A letra atual é maiuscula.
                mensagem_nova += chave[ascii_letra - valores.MIN_MAIUSCULA].upper()  # Adicionar a nova letra encriptada ou traduzida para a mensagem final.
                continue
            if ascii_letra >= valores.MIN_MINUSCULA and ascii_letra <= valores.MAX_MINUSCULA:  # A letra atual é minuscula.
                mensagem_nova += chave[ascii_letra - valores.MIN_MINUSCULA].lower()  # Adicionar a nova letra encriptada ou traduzida para a mensagem final.
                continue
            mensagem_nova += letra  # Se chegou até aqui, quer dizer que foi lido algo diferente que uma letra(ex:"!",".",","...).
        return mensagem_nova
    else:
        return 'Chave Invalida !'


def traduz_subst_simples(chave, mensagem):  # Função que irá adaptar a chave fornecida para a tradução.
    if teste_chave_substSimples(chave):
        letra_troca = valores.MIN_MINUSCULA
        chave = chave.lower()
        nova_chave = ''
        lista_chave = []
        for i in range(valores.TAMANHO_ALFABETO):
            lista_chave.append('a')  # Preencher a lista (que será a nova chave) com um valor qualquer (placeholder).
        for letra in chave:  # Loop que irá verificar cada letra da chave antiga.
            posicao_alfabeto = ord(letra) % valores.MIN_MINUSCULA  # Tal equação irá retornar uma posição do alfabeto da letra atual (a = 0, b = 1, etc).
            lista_chave[posicao_alfabeto] = chr(letra_troca)  # Colocar a letra atual na posição correta da chave de tradução.
            letra_troca += 1  # Ir para a próxima letra da chave.
        for valor in lista_chave:  # Repassar todos valores da lista para uma string.
            nova_chave += valor
        return subst_simples(nova_chave, mensagem)  # Traduzir a mensagem com a chave nova.
    else:
        return 'Chave invalida !'
