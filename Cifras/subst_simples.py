
erro_mensagem = "Erro: Mensagem inexistente !"
erro_chave = 'Chave inválida !\nClique em "Abrir guia da cifra" e verifique quais chaves são válidas para o modo Substituição simples'

def encriptar_modo_apenas_letras(lista_chaves, mensagem):
    chave = adaptar_chave_modo_apenas_letras(lista_chaves)
    return mensagem_nova(chave, mensagem)


def encriptar_modo_varios_caracteres(lista_chaves, mensagem):
    chave = adaptar_chave_modo_varios_caracteres(lista_chaves)
    return mensagem_nova(chave, mensagem)


def traduzir_modo_apenas_letras(lista_chaves, mensagem):
    '''
    Para fazer a tradução, basta apenas trocar a ordem das chaves. Isso fará com que as letras 
    da mensagem encriptada sejam trocadas pelas letras mensagem comum.
    '''
    chave = adaptar_chave_modo_apenas_letras(lista_chaves[::-1])
    return mensagem_nova(chave, mensagem)


def traduzir_modo_varios_caracteres(lista_chaves, mensagem):
    chave = adaptar_chave_modo_varios_caracteres(lista_chaves[::-1])
    return mensagem_nova(chave, mensagem)


def mensagem_nova(chave, mensagem):
    if not mensagem:
        return erro_mensagem
    if chave:
        return criar_mensagem_com_caracteres_trocados(chave, mensagem)
    else:
        return erro_chave

def adaptar_chave_modo_varios_caracteres(lista_chaves):  # Criará um dicionário relacionando a chave_1 com a chave_2
    if lista_chaves[0] and lista_chaves[1]:
        if verifica_caracteres_duplicados_chave_normal(lista_chaves[0], lista_chaves[1]) and sorted(lista_chaves[0]) == sorted(lista_chaves[1]):
            # Chave valida: chave_1 e chave_2 possuem os mesmos caracteres (sem duplicações)
            return cria_dicionario_chave_normal(lista_chaves[0], lista_chaves[1])
        if verifica_caracteres_duplicados_chave_composta(lista_chaves[0], lista_chaves[1]) and len(lista_chaves[0]) == len(lista_chaves[1]):
            # Chave valida: chave_1 e chave_2 não possuem nenhum caractere em comum (sem duplicações)
            return cria_dicionario_chave_ida_e_volta(lista_chaves[0], lista_chaves[1])
    return False


def adaptar_chave_modo_apenas_letras(lista_chaves):  # Criar conversões para caixa baixa e alta.
    if lista_chaves[0].isalpha() and lista_chaves[1].isalpha():
        chave_1 = lista_chaves[0].lower()
        chave_2 = lista_chaves[1].lower()
        if verifica_caracteres_duplicados_chave_normal(chave_1, chave_2) and sorted(chave_1) == sorted(chave_2):
            # Chave valida: chave_1 e chave_2 possuem os mesmos caracteres (sem duplicações)
            chave_dics = cria_dicionario_chave_normal(chave_1, chave_2)
            chave_dics.update(cria_dicionario_chave_normal(chave_1.upper(), chave_2.upper()))
            return chave_dics
        if verifica_caracteres_duplicados_chave_composta(chave_1, chave_2) and len(chave_1) == len(chave_2):
            # Chave valida: chave_1 e chave_2 não possuem nenhum caractere em comum (sem duplicações)
            chave_dics = cria_dicionario_chave_ida_e_volta(chave_1, chave_2)
            chave_dics.update(cria_dicionario_chave_ida_e_volta(chave_1.upper(), chave_2.upper()))
            return chave_dics
    return False


def verifica_caracteres_duplicados_chave_composta(chave_1, chave_2):  
    # Juntará as duas chaves e verificará se essa nova chave composta não existe repetição.
    chave_composta = chave_1 + chave_2
    for letra in chave_composta:
        if chave_composta.count(letra) >= 2:
            return False
    return True


def verifica_caracteres_duplicados_chave_normal(chave_1, chave_2):
    # Verificará se existem repetições nas duas chaves fornecidas (não ocorre a junção).
    for chave in (chave_1, chave_2):
        for letra in chave:
            if chave.count(letra) >= 2:
                return False
    return True


def criar_mensagem_com_caracteres_trocados(chave_dics, mensagem):
    nova_mensagem = ''
    for letra in mensagem:
        try:
            nova_mensagem += chave_dics[letra]
        except:
            nova_mensagem += letra
    return nova_mensagem


def cria_dicionario_chave_ida_e_volta(chave_1, chave_2):
    '''
    OBS: É preciso criar duas chaves, pois ocorrerá erros quando um caractere trocado pela chave_2 não é trocado pela chave_1
    Ex com o erro:  chave_1 = a | chave_2 = b | mensagem = ab | mensagem_encriptada = bb | mensagem_traduzida = a
    Ex erro resolvido: chave_1 = a | chave_2 = b | mensagem = ab | mensagem_encriptada = ba | mensagem_traduzida = ab
    Com duas chaves, é possível realizar o processo inverso de procura caso seja necessário.
    '''
    dicionario_chave = dict()
    for index in range(len(chave_1)):
        dicionario_chave[chave_1[index]] = chave_2[index]
        dicionario_chave[chave_2[index]] = chave_1[index]
    return dicionario_chave


def cria_dicionario_chave_normal(chave_1, chave_2):
    dicionario_chave = dict()
    for index in range(len(chave_1)):
        dicionario_chave[chave_1[index]] = chave_2[index]
    return dicionario_chave


def retorna_chaves_se_for_valida(lista_chaves):  # Utilizado no menu opções...
    if adaptar_chave_modo_apenas_letras(lista_chaves) or adaptar_chave_modo_varios_caracteres(lista_chaves):
        return lista_chaves
    return False
