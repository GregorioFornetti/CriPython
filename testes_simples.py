import Cifras.cifra_de_cesar as cifra_de_cesar
import Cifras.cifra_de_vigenere as cifra_de_vigenere
import Cifras.subst_simples as subst_simples

soma_erros = 0

def testar():  # Função que chamará todos os testes de cifras disponiveis.
    print('Iniciando os testes automatizados...')
    print('Aqui serão feitos alguns testes simples...')
    print('Utilize esses testes para entender melhor sobre o funcionamento das cifras disponíveis.')
    testa_cesar_apenas_letras()
    testa_cesar_varios_caracteres()
    testa_subst_simples_apenas_letras()
    testa_subst_simples_varios_caracteres()
    testa_vigenere_apenas_letras()
    testa_vigenere_varios_caracteres()
    if soma_erros == 0:
        separacoes('Nenhum erro encontrado !')
    else:
        separacoes('Total de erros encontrados foi:' + str(soma_erros))


def testa_cesar_apenas_letras():  # Função que testa a cifra de césar.
    separacoes('Cifra de César(apenas letras)')
    testes = {}
    # Primeiro teste:
    testes['chave'] = '1'
    testes['mensagem'] = 'abcdefghijklmnopqrstuvwxyz'
    testes['mensagem esperada'] = 'bcdefghijklmnopqrstuvwxyza'
    testes['mensagem computada'] = cifra_de_cesar.encriptar_modo_apenas_letras(testes['chave'], testes['mensagem'])
    verificar_e_imprimir_testes(1, testes)
    # Segundo teste:
    testes['chave'] = '5'
    testes['mensagem'] = 'abcdefghijklmnopqrstuvwxyz'
    testes['mensagem esperada'] = 'fghijklmnopqrstuvwxyzabcde'
    testes['mensagem computada'] = cifra_de_cesar.encriptar_modo_apenas_letras(testes['chave'], testes['mensagem'])
    verificar_e_imprimir_testes(2, testes)
    # Terceiro teste:
    testes['chave'] = '7'
    testes['mensagem'] = 'Bom dia, Boa tarde, Boa noite!'
    testes['mensagem esperada'] = 'Ivt kph, Ivh ahykl, Ivh uvpal!'
    testes['mensagem computada'] = cifra_de_cesar.encriptar_modo_apenas_letras(testes['chave'], testes['mensagem'])
    verificar_e_imprimir_testes(3, testes)
    # Quarto teste:
    testes['chave'] = '7'
    testes['mensagem'] = 'Ivt kph, Ivh ahykl, Ivh uvpal!'
    testes['mensagem esperada'] = 'Bom dia, Boa tarde, Boa noite!'
    testes['mensagem computada'] = cifra_de_cesar.traduzir_modo_apenas_letras(testes['chave'], testes['mensagem'])
    verificar_e_imprimir_testes(4, testes, modo_traduc=True)


def testa_cesar_varios_caracteres():
    separacoes('Cifra de César(vários caracteres)')
    testes = {}
    # Primeiro teste:
    testes['chave'] = '123'
    testes['mensagem'] = 'Olá ! Será que troca letras com acentos também ? E espaços ? Vamos testar agora !'
    testes['mensagem esperada'] = 'íĊŜ¾¿¾ñăĐŜ¾ďēă¾ĒĐčāÿ¾ĊăĒĐÿđ¾āčċ¾ÿāăČĒčđ¾ĒÿċĀŤċ¾Ý¾ã¾ăđĎÿŢčđ¾Ý¾ôÿċčđ¾ĒăđĒÿĐ¾ÿąčĐÿ¾¿'
    testes['mensagem computada'] = cifra_de_cesar.encriptar_modo_varios_caracteres(testes['chave'], testes['mensagem'])
    verificar_e_imprimir_testes(1, testes)
    # Segundo teste:
    testes['chave'] = '123'
    testes['mensagem'] = 'íĊŜ¾¿¾ñăĐŜ¾ďēă¾ĒĐčāÿ¾ĊăĒĐÿđ¾āčċ¾ÿāăČĒčđ¾ĒÿċĀŤċ¾Ý¾ã¾ăđĎÿŢčđ¾Ý¾ôÿċčđ¾ĒăđĒÿĐ¾ÿąčĐÿ¾¿'
    testes['mensagem esperada'] = 'Olá ! Será que troca letras com acentos também ? E espaços ? Vamos testar agora !'
    testes['mensagem computada'] = cifra_de_cesar.traduzir_modo_varios_caracteres(testes['chave'], testes['mensagem'])
    verificar_e_imprimir_testes(2, testes, modo_traduc=True)
    # Terceiro teste:
    testes['chave'] = '321'
    testes['mensagem'] = 'Legal ! Parece que está tudo funcionando corretamente, vamos ver como o texto fica movendo mais ainda !!!'
    testes['mensagem esperada'] = 'ưǉǋǅǐƄƅƄƴǅǖǉǇǉƄǕǙǉƄǉǗǘȢƄǘǙǈǓƄǊǙǒǇǍǓǒǅǒǈǓƄǇǓǖǖǉǘǅǑǉǒǘǉƐƄǚǅǑǓǗƄǚǉǖƄǇǓǑǓƄǓƄǘǉǜǘǓƄǊǍǇǅƄǑǓǚǉǒǈǓƄǑǅǍǗƄǅǍǒǈǅƄƅƅƅ'
    testes['mensagem computada'] = cifra_de_cesar.encriptar_modo_varios_caracteres(testes['chave'], testes['mensagem'])
    verificar_e_imprimir_testes(3, testes)
    # Quarto teste:
    testes['chave'] = '321'
    testes['mensagem'] = 'ưǉǋǅǐƄƅƄƴǅǖǉǇǉƄǕǙǉƄǉǗǘȢƄǘǙǈǓƄǊǙǒǇǍǓǒǅǒǈǓƄǇǓǖǖǉǘǅǑǉǒǘǉƐƄǚǅǑǓǗƄǚǉǖƄǇǓǑǓƄǓƄǘǉǜǘǓƄǊǍǇǅƄǑǓǚǉǒǈǓƄǑǅǍǗƄǅǍǒǈǅƄƅƅƅ'
    testes['mensagem esperada'] = 'Legal ! Parece que está tudo funcionando corretamente, vamos ver como o texto fica movendo mais ainda !!!'
    testes['mensagem computada'] = cifra_de_cesar.traduzir_modo_varios_caracteres(testes['chave'], testes['mensagem'])
    verificar_e_imprimir_testes(4, testes, modo_traduc=True)


def testa_subst_simples_apenas_letras():  # Função que testa a cifra de substituição simples.
    separacoes('Substituição simples(apenas letras)')
    testes = {}
    # Primeiro teste:
    testes['letras mensagem comum'] = 'abcdefghijklmnopqrstuvwxyz'
    testes['letras mensagem encriptada'] = 'fhizdlmnavgewptubxjrqocsky'
    testes['mensagem'] = 'Tudo bem com voce ?'
    testes['mensagem esperada'] = 'Rqzt hdw itw otid ?'
    testes['mensagem computada'] = subst_simples.executar_modo_apenas_letras(testes['letras mensagem comum'],
                                                                             testes['letras mensagem encriptada'], testes['mensagem'])
    verificar_e_imprimir_testes(1, testes)
    # Segundo teste:
    testes['letras mensagem comum'] = 'abcdefghijklmnopqrstuvwxyz'
    testes['letras mensagem encriptada'] = 'fhizdlmnavgewptubxjrqocsky'
    testes['mensagem'] = 'Rqzt hdw itw otid ?'
    testes['mensagem esperada'] = 'Tudo bem com voce ?'
    testes['mensagem computada'] = subst_simples.executar_modo_apenas_letras(testes['letras mensagem encriptada'],
                                                                             testes['letras mensagem comum'], testes['mensagem'])
    verificar_e_imprimir_testes(2, testes, modo_traduc=True)
    # Terceiro teste:
    testes['letras mensagem comum'] = 'abcdefghijklmnopqrstuvwxyz'
    testes['letras mensagem encriptada'] = 'neruzjxpgfabcowvdqyihtslmk'
    testes['mensagem'] = 'Por favor, me responda !'
    testes['mensagem esperada'] = 'Vwq jntwq, cz qzyvwoun !'
    testes['mensagem computada'] = subst_simples.executar_modo_apenas_letras(testes['letras mensagem comum'],
                                                                             testes['letras mensagem encriptada'], testes['mensagem'])
    verificar_e_imprimir_testes(3, testes)
    # Quarto teste:
    testes['letras mensagem comum'] = 'abcdefghijklmnopqrstuvwxyz'
    testes['letras mensagem encriptada'] = 'neruzjxpgfabcowvdqyihtslmk'
    testes['mensagem'] = 'Vwq jntwq, cz qzyvwoun !'
    testes['mensagem esperada'] = 'Por favor, me responda !' 
    testes['mensagem computada'] = subst_simples.executar_modo_apenas_letras(testes['letras mensagem encriptada'],
                                                                             testes['letras mensagem comum'], testes['mensagem'])
    verificar_e_imprimir_testes(4, testes, modo_traduc=True)


def testa_subst_simples_varios_caracteres():
    separacoes('Substituição simples(vários caracteres)')
    testes = {}
    # Primeiro teste:
    testes['letras mensagem comum'] = 'abcdefghijklmnopqrstuvwxyz'
    testes['letras mensagem encriptada'] = 'fhizdlmnavgewptubxjrqocsky'
    testes['mensagem'] = 'Ué ? Esse exemplo não é igual ao da cifra de substituição simples no modo apenas letras ? Não, as maiusculas não serão trocadas se você não pedir!'
    testes['mensagem esperada'] = 'Ué ? Ejjd dsdwuet pãt é amqfe ft zf ialxf zd jqhjrarqaçãt jawuedj pt wtzt fudpfj edrxfj ? Nãt, fj wfaqjiqefj pãt jdxãt rxtifzfj jd otiê pãt udzax!'
    testes['mensagem computada'] = subst_simples.executar_modo_varios_caracteres(testes['letras mensagem comum'],
                                                                                 testes['letras mensagem encriptada'], testes['mensagem'])
    verificar_e_imprimir_testes(1, testes)
    # Segundo teste:
    testes['letras mensagem comum'] = 'abcdefghijklmnopqrstuvwxyz'
    testes['letras mensagem encriptada'] = 'fhizdlmnavgewptubxjrqocsky'
    testes['mensagem'] = 'Ué ? Ejjd dsdwuet pãt é amqfe ft zf ialxf zd jqhjrarqaçãt jawuedj pt wtzt fudpfj edrxfj ? Nãt, fj wfaqjiqefj pãt jdxãt rxtifzfj jd otiê pãt udzax!'
    testes['mensagem esperada'] = 'Ué ? Esse exemplo não é igual ao da cifra de substituição simples no modo apenas letras ? Não, as maiusculas não serão trocadas se você não pedir!'
    testes['mensagem computada'] = subst_simples.executar_modo_varios_caracteres(testes['letras mensagem encriptada'],
                                                                                 testes['letras mensagem comum'], testes['mensagem'])
    verificar_e_imprimir_testes(2, testes, modo_traduc=True)
    # Terceiro teste:
    testes['letras mensagem comum'] = 'abcdefghijklmnopqrstuvwxyz !?.,'
    testes['letras mensagem encriptada'] = 'qwertyuiopasdfghjklzxcvbnm@#$%*'
    testes['mensagem'] = 'Vamos trocar outros caracteres agora ! Testando, 1, 2, 3 ... Funcionou ?'
    testes['mensagem esperada'] = 'Vqdgl@zkgeqk@gxzkgl@eqkqeztktl@qugkq@#@Ttlzqfrg*@1*@2*@3@%%%@Fxfeogfgx@$'
    testes['mensagem computada'] = subst_simples.executar_modo_varios_caracteres(testes['letras mensagem comum'],
                                                                                 testes['letras mensagem encriptada'], testes['mensagem'])
    verificar_e_imprimir_testes(3, testes)
    # Quarto teste:
    testes['letras mensagem comum'] = 'abcdefghijklmnopqrstuvwxyz !?.,'
    testes['letras mensagem encriptada'] = 'qwertyuiopasdfghjklzxcvbnm@#$%*'
    testes['mensagem'] = 'Vqdgl@zkgeqk@gxzkgl@eqkqeztktl@qugkq@#@Ttlzqfrg*@1*@2*@3@%%%@Fxfeogfgx@$'
    testes['mensagem esperada'] = 'Vamos trocar outros caracteres agora ! Testando, 1, 2, 3 ... Funcionou ?'
    testes['mensagem computada'] = subst_simples.executar_modo_varios_caracteres(testes['letras mensagem encriptada'],
                                                                                 testes['letras mensagem comum'], testes['mensagem'])
    verificar_e_imprimir_testes(4, testes, modo_traduc=True)


def testa_vigenere_apenas_letras():  # Função que testa a cifra de Vigenère.
    separacoes('Cifra de Vigenère(apenas letras)')
    testes = {}
    # Primeiro teste:
    testes['chave'] = 'ataque'
    testes['mensagem'] = 'Vamos invadir a base deles amanhã !'
    testes['mensagem esperada'] = 'Vtmem mnoatcv a uaiy heeei uqaghã !'
    testes['mensagem computada'] = cifra_de_vigenere.encriptar_modo_apenas_letras(testes['chave'], testes['mensagem'])
    verificar_e_imprimir_testes(1, testes)
    # Segundo teste:
    testes['chave'] = 'ataque'
    testes['mensagem'] = 'Vtmem mnoatcv a uaiy heeei uqaghã !'
    testes['mensagem esperada'] = 'Vamos invadir a base deles amanhã !'
    testes['mensagem computada'] = cifra_de_vigenere.traduzir_modo_apenas_letras(testes['chave'], testes['mensagem'])
    verificar_e_imprimir_testes(2, testes, modo_traduc=True)
    # Terceiro teste:
    testes['chave'] = 'covid'
    testes['mensagem'] = 'Cuidado para não se contaminar !'
    testes['mensagem esperada'] = 'Eidldfc kiuc bãj ah ecibdowiiu !'
    testes['mensagem computada'] = cifra_de_vigenere.encriptar_modo_apenas_letras(testes['chave'], testes['mensagem'])
    verificar_e_imprimir_testes(3, testes)
    # Quarto teste:
    testes['chave'] = 'covid'
    testes['mensagem'] = 'Eidldfc kiuc bãj ah ecibdowiiu !'
    testes['mensagem esperada'] = 'Cuidado para não se contaminar !'
    testes['mensagem computada'] = cifra_de_vigenere.traduzir_modo_apenas_letras(testes['chave'], testes['mensagem'])
    verificar_e_imprimir_testes(4, testes, modo_traduc=True)


def testa_vigenere_varios_caracteres():
    separacoes('Cifra de Vigenère (vários caracteres)')
    testes = {}
    # Primeiro teste:
    testes['chave'] = 'testando'
    testes['mensagem'] = 'Vamos ver como que essa cifra está funcionando ! Será que está trocando tudo ?'
    testes['mensagem esperada'] = 'ìèĂąö°üöĈ§øąðÿ¦Ăċìµûöăç±ùðûĈä°ëĄĊŨµüøþéúąõöĄçÿ¦²¶ÚúĈŤ°÷Ćû§úĉ÷ű¦ąĈöø÷ñôõ±Ċüùą£Ï'
    testes['mensagem computada'] = cifra_de_vigenere.encriptar_modo_varios_caracteres(testes['chave'], testes['mensagem'])
    verificar_e_imprimir_testes(1, testes)
    # Segundo teste:
    testes['chave'] = 'testando'
    testes['mensagem'] = 'ìèĂąö°üöĈ§øąðÿ¦Ăċìµûöăç±ùðûĈä°ëĄĊŨµüøþéúąõöĄçÿ¦²¶ÚúĈŤ°÷Ćû§úĉ÷ű¦ąĈöø÷ñôõ±Ċüùą£Ï'
    testes['mensagem esperada'] = 'Vamos ver como que essa cifra está funcionando ! Será que está trocando tudo ?'
    testes['mensagem computada'] = cifra_de_vigenere.traduzir_modo_varios_caracteres(testes['chave'], testes['mensagem'])
    verificar_e_imprimir_testes(2, testes, modo_traduc=True)
    # Terceiro teste:
    testes['chave'] = 'cháves diférentes!'
    testes['mensagem'] = 'Vamos testar agora com uma chave diferente, com espaços e acentos.'
    testes['mensagem esperada'] = 'ÛëŰćúµ¶ëþüŬĆ§ñýöć¤¥íŲą§Ċ¯ç«ëųõýõ¶ëþ©êüŨĆûúL¦î÷Ÿ´ìăĆèż²øªŨ¸èø§ôÿ÷žÂ'
    testes['mensagem computada'] = cifra_de_vigenere.encriptar_modo_varios_caracteres(testes['chave'], testes['mensagem'])
    verificar_e_imprimir_testes(3, testes)
    # Quarto teste:
    testes['chave'] = 'cháves diférentes!'
    testes['mensagem'] = 'ÛëŰćúµ¶ëþüŬĆ§ñýöć¤¥íŲą§Ċ¯ç«ëųõýõ¶ëþ©êüŨĆûúL¦î÷Ÿ´ìăĆèż²øªŨ¸èø§ôÿ÷žÂ'
    testes['mensagem esperada'] = 'Vamos testar agora com uma chave diferente, com espaços e acentos.'
    testes['mensagem computada'] = cifra_de_vigenere.traduzir_modo_varios_caracteres(testes['chave'], testes['mensagem'])
    verificar_e_imprimir_testes(4, testes, modo_traduc=True)


def separacoes(cifra):  # Cria uma separação no output gerado.
    print()
    print('-' * 210)
    print('{:^190}'.format(cifra))
    print('-' * 210)
    print()


def verificar_e_imprimir_testes(n_teste, dic_testes, modo_traduc=False):  # Impressões automaticas e testes.
    '''
    Função que verificará e imprimirá os testes feitos pelo programa.
    Param. dic_testes: é um dicionário que contém a chave e a mensagem que devem ser testadas (indexes: chave, mensagem),
    e também apresenta o resultado esperado a ser recebido pelo programa(index: mensagem esperada)
    Param. n_teste: é o número do teste realizado.
    '''
    global soma_erros
    print(f'Teste {n_teste}:')
    if modo_traduc:
        print('Modo tradução')
    else:
        print('Modo encriptação')
    for chave, valor in dic_testes.items():
        print(f'{chave} = {valor}')
    
    if dic_testes["mensagem esperada"] == dic_testes["mensagem computada"]:
        # O algoritmo do programa foi bem sucedido e acertou o valor esperado.
        print('Passou!\n')
    else:
        # Ocorreu algum erro e o algoritmo não acertou o valor esperado.
        print('Não passou!\n')
        soma_erros += 1
