import valores


def teste_chave_substSimples(chave):  # Verifica se a chave é valida.
    chave = chave.lower()
    if len(chave) != valores.TAMANHO_ALFABETO:  # A chave para ser valida tem que ter um tamanho de 26 caracteres.
        return False
    for char in chave:  # E a chave não pode ter caracteres repetidos.
        ascii_letra = ord(char)
        if chave.count(char) >= 2:
            return False
        if not(ascii_letra >= valores.MIN_MINUSCULA and ascii_letra <= valores.MAX_MINUSCULA):  # E nem caracteres especiais.
            return False
    return chave


def executar_modo_apenas_letras(chave, mensagem, modo_traducao=False):  # Função que traduz/encripta através da "substituição simples".
    pass


def traduz_subst_simples(chave):  # Função que irá adaptar a chave fornecida para a tradução.
    pass
