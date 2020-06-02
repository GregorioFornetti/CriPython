import subst_simples
import cesar
import vigenere


def testar():  # Função que chamará todos os testes de cifras disponiveis.
    print('Iniciando os testes automatizados...')
    print('Aqui serão feitos alguns testes simples...')
    todos_erros = testa_cesar()
    todos_erros += testa_subst_simples()
    todos_erros += testa_vigenere()
    if todos_erros == 0:
        separacoes('Nenhum erro encontrado !')
    else:
        separacoes('Total de erros encontrados foi:' + str(todos_erros))


def testa_cesar():  # Função que testa a cifra de césar.
    erros = 0
    separacoes('Cifra de César')
    print('Teste 1:')
    erros += imprimir_testes('1',
                             'abcdefghijklmnopqrstuvwxyz',
                             'bcdefghijklmnopqrstuvwxyza',
                              cesar.cifra_de_cesar('1', 'abcdefghijklmnopqrstuvwxyz'))
    print('Teste 2:')
    erros += imprimir_testes('5',
                             'abcdefghijklmnopqrstuvwxyz',
                             'fghijklmnopqrstuvwxyzabcde',
                              cesar.cifra_de_cesar('5', 'abcdefghijklmnopqrstuvwxyz'))
    print('Teste 3:')
    erros += imprimir_testes('7',
                             'Bom dia, Boa tarde, Boa noite!',
                             'Ivt kph, Ivh ahykl, Ivh uvpal!',
                             cesar.cifra_de_cesar('7', 'Bom dia, Boa tarde, Boa noite!'))
    print('Teste 4:')
    erros += imprimir_testes('7 (tradução)',
                             'Ivt kph, Ivh ahykl, Ivh uvpal!',
                             'Bom dia, Boa tarde, Boa noite!',
                             cesar.traduz_cesar('7', 'Ivt kph, Ivh ahykl, Ivh uvpal!'))
    return erros


def testa_subst_simples():  # Função que testa a cifra de substituição simples.
    erros = 0
    separacoes('Substituição simples')
    print('Teste 1:')
    erros += imprimir_testes('fhizdlmnavgewptubxjrqocsky',
                             'Tudo bem com voce ?',
                             'Rqzt hdw itw otid ?',
                              subst_simples.subst_simples('fhizdlmnavgewptubxjrqocsky', 'Tudo bem com voce ?'))
    print('Teste 2:')
    erros += imprimir_testes('fhizdlmnavgewptubxjrqocsky (tradução)',
                             'Rqzt hdw itw otid ?',
                             'Tudo bem com voce ?',
                              subst_simples.traduz_subst_simples('fhizdlmnavgewptubxjrqocsky', 'Rqzt hdw itw otid ?'))
    print('Teste 3:')
    erros += imprimir_testes('neruzjxpgfabcowvdqyihtslmk',
                             'Por favor, me responda !',
                             'Vwq jntwq, cz qzyvwoun !',
                              subst_simples.subst_simples('neruzjxpgfabcowvdqyihtslmk', 'Por favor, me responda !'))
    print('Teste 4:')
    erros += imprimir_testes('neruzjxpgfabcowvdqyihtslmk (tradução)',
                             'Vwq jntwq, cz qzyvwoun !',
                             'Por favor, me responda !',
                             subst_simples.traduz_subst_simples('neruzjxpgfabcowvdqyihtslmk', 'Vwq jntwq, cz qzyvwoun !'))

    return erros


def testa_vigenere():  # Função que testa a cifra de Vigenère.
    erros = 0
    separacoes('Cifra de Vigenère')
    print('Teste 1:')
    erros += imprimir_testes('ataque',
                             'Vamos invadir a base deles amanhã !',
                             'Vtmem mnoatcv a uaiy heeei uqaghã !',
                             vigenere.vigenere('ataque', 'Vamos invadir a base deles amanhã !'))
    print('Teste 2:')
    erros += imprimir_testes('ataque (tradução)',
                             'Vtmem mnoatcv a uaiy heeei uqaghã !',
                             'Vamos invadir a base deles amanhã !',
                             vigenere.traduz_vigenere('ataque', 'Vtmem mnoatcv a uaiy heeei uqaghã !'))
    print('Teste 3:')
    erros += imprimir_testes('covid',
                             'Cuidado para não se contaminar !',
                             'Eidldfc kiuc bãj ah ecibdowiiu !',
                             vigenere.vigenere('covid', 'Cuidado para não se contaminar !'))
    print('Teste 4:')
    erros += imprimir_testes('covid (tradução)',
                             'Eidldfc kiuc bãj ah ecibdowiiu !',
                             'Cuidado para não se contaminar !',
                             vigenere.traduz_vigenere('covid', 'Eidldfc kiuc bãj ah ecibdowiiu !'))
    return erros




def separacoes(cifra):  # Cria uma separação no output gerado.
    print()
    print('----' * 15)
    print('{:^45}'.format(cifra))
    print('----' * 15)
    print()


def imprimir_testes(chave, mensagem, mensagem_esperada, mensagem_recebida):  # Impressões automaticas e testes.
    '''
    Função que recebe como parâmetros a chave que será usada para o teste, a mensagem que será encriptada/traduzida, a mensagem esperada
    que o programa deve retornar, e a mensagem recebida pelo próprio programa. Se a mensagem esperada for igual a mensagem recebida,
    quer dizer que o programa passou no teste.
    '''
    print(f'chave = {chave}')
    print(f'Mensagem = {mensagem}')
    print(f'Mensagem esperada: {mensagem_esperada}')
    print(f'Mensagem recebida: {mensagem_recebida}')
    if mensagem_esperada == mensagem_recebida:
        print('Passou!')
        return 0
    else:
        print('Não passou!')
        return 1
