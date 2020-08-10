import Cifras.utilidades_cifras as utilidades
import banco_de_dados
import dicionarios


def encriptar_modo_apenas_letras(lista_chaves, mensagem):  # Função que traduz/encripta a mensagem pela cifra de Vigenère.
    chave = testa_chave_vigenere_apenas_letras(lista_chaves)
    return mensagem_nova_modo_apenas_letras(chave, mensagem)  


def testa_chave_vigenere_apenas_letras(lista_chaves):
    # Chave válida: texto com apenas letras sem acentos (espaçoes são ignorados).
    chave = lista_chaves[0].lower().replace(' ', '')
    for caractere in chave:
        if ord(caractere) < utilidades.MIN_MINUSCULA or ord(caractere) > utilidades.MAX_MINUSCULA:
            return False
    return chave


def traduzir_modo_apenas_letras(lista_chaves, mensagem):
    chave = adaptar_chave_para_traducao_apenas_letras(lista_chaves)
    return mensagem_nova_modo_apenas_letras(chave, mensagem)


def adaptar_chave_para_traducao_apenas_letras(lista_chaves):  # Função que adapta a chave para a tradução.
    chave = testa_chave_vigenere_apenas_letras(lista_chaves)
    if chave:
        chave_traduc = ''
        for letra in chave:
            letra_ASCII = ord(letra) - utilidades.MIN_MINUSCULA
            if letra_ASCII == 0:
                chave_traduc += utilidades.ALFABETO_MINUSCULO[0]
                continue
            letra_atual = 26 - letra_ASCII  # Para transformar a chave, basta subtrair 26 com o antigo valor da chave (isso fará com que a mensagem de uma "volta" e volte ao normal).
            chave_traduc += utilidades.ALFABETO_MINUSCULO[letra_atual]
        return chave_traduc
    else:
        return False


def mensagem_nova_modo_apenas_letras(chave, mensagem):
    if not mensagem:
        return dicionarios.retorna_erro_mensagem(banco_de_dados.retorna_idioma_configurado())
    if chave:
        return vigenere_troca_apenas_letras(chave, mensagem)
    else:
        return dicionarios.retorna_erro_chave(banco_de_dados.retorna_idioma_configurado())


def vigenere_troca_apenas_letras(chave, mensagem):
    tamanho_chave = len(chave)
    valor_atual_chave = 0
    mensagem_nova = ''
    for letra in mensagem:
        letra_cifrada = letra
        letra_ASCII = ord(letra)  # Valor ASCII da letra atual da mensagem.
        chave_ASCII = ord(chave[valor_atual_chave]) - utilidades.MIN_MINUSCULA  # Valor alfabético (0-25, A=0, B=1,...) da letra da chave atual. 
        if letra_ASCII >= utilidades.MIN_MINUSCULA and letra_ASCII <= utilidades.MAX_MINUSCULA:  # Casos de letras minusculas.
            letra_ASCII -= utilidades.MIN_MINUSCULA
            index_alfabeto = (letra_ASCII + chave_ASCII) % 26  # Juntar os utilidades da letra da chave e da mensagem. (OBS: não pode passar de 26, que é o mesmo que dar uma volta no alfabeto).
            letra_cifrada = utilidades.ALFABETO_MINUSCULO[index_alfabeto]  # Pegar a letra com o valor alfabético calculado pelo index_alfabeto.
            valor_atual_chave += 1  # Mover a letra da chave em uma casa.
        elif letra_ASCII >= utilidades.MIN_MAIUSCULA and letra_ASCII <= utilidades.MAX_MAIUSCULA:  # Casos de letras maiusculas.
            letra_ASCII -= utilidades.MIN_MAIUSCULA
            index_alfabeto = (letra_ASCII + chave_ASCII) % 26
            letra_cifrada = utilidades.ALFABETO_MAIUSCULO[index_alfabeto]
            valor_atual_chave += 1  # Mover a letra da chave em uma casa.
        mensagem_nova += letra_cifrada
        if valor_atual_chave >= tamanho_chave:  # Se a chave chegou ao final, voltar para o início.
            valor_atual_chave = 0
    return mensagem_nova


def encriptar_modo_varios_caracteres(lista_chaves, mensagem):
    dic_unicode = utilidades.criar_dicionario_caracteres_imprimiveis(utilidades.FINAL_UNICODE)
    chave = testa_chave_vigenere_varios_caracteres(lista_chaves)
    return mensagem_nova_modo_varios_caracteres(chave, mensagem, dic_unicode)


def testa_chave_vigenere_varios_caracteres(lista_chaves):
    for caractere in lista_chaves[0]:
        if ord(caractere) > 733:
            return False
    return lista_chaves[0]


def traduzir_modo_varios_caracteres(lista_chaves, mensagem):
    dic_unicode = utilidades.criar_dicionario_caracteres_imprimiveis(utilidades.FINAL_UNICODE)
    chave = adaptar_chave_para_traducao_varios_caracteres(lista_chaves, dic_unicode)
    return mensagem_nova_modo_varios_caracteres(chave, mensagem, dic_unicode)


def adaptar_chave_para_traducao_varios_caracteres(lista_chaves, dic_unicode):
    '''
    A chave de tradução será um texto com caracteres que tem um indice que faz com que as letras encriptadas,
    quando jogadas na func. troca caracteres, voltem ao normal. Para isso, é preciso que os caracteres da nova chave sejam 
    os valores que faltam para completar uma volta em relação ao valor da chave antigo.
    '''
    if testa_chave_vigenere_varios_caracteres(lista_chaves):
        tot_caracteres_imprimiveis = len(dic_unicode) // 2
        chave_traduc = ''
        for caractere in lista_chaves[0]:
            if caractere == ' ':  
                # Espaço, por ser o primeiro caractere do dicionario, não afeta na mensagem encriptada, portanto, pode mante-lo na chave nova.
                chave_traduc += ' '
            else:
                chave_traduc += dic_unicode[tot_caracteres_imprimiveis - dic_unicode[caractere]]
        return chave_traduc
    else:
        return False


def mensagem_nova_modo_varios_caracteres(chave, mensagem, dic_unicode):
    if not mensagem:
        return dicionarios.retorna_erro_mensagem(banco_de_dados.retorna_idioma_configurado())
    if chave:
        return vigenere_troca_varios_caracteres(chave, mensagem, dic_unicode)
    else:
        return dicionarios.retorna_erro_chave(banco_de_dados.retorna_idioma_configurado())


def vigenere_troca_varios_caracteres(chave, mensagem, dic_unicode):
    tot_caracteres_imprimiveis = len(dic_unicode) // 2
    indice_atual_chave = 0
    tamanho_chave = len(chave)
    nova_mensagem = ''
    for caractere in mensagem:
        try:
            valor_caractere_atual = dic_unicode[caractere] + dic_unicode[chave[indice_atual_chave]]
            if valor_caractere_atual >= tot_caracteres_imprimiveis:
                valor_caractere_atual -= tot_caracteres_imprimiveis
            indice_atual_chave += 1
            if indice_atual_chave == tamanho_chave:
                indice_atual_chave = 0
            nova_mensagem += dic_unicode[valor_caractere_atual]
        except:  # Caractere atual está acima do limite unicode declarado.
            nova_mensagem += caractere
    return nova_mensagem
