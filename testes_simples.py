import subst_simples
import cesar


def testar():  # Função que chamará todos os testes de cifras disponiveis.
    print('Iniciando os testes automatizados...')
    print('Aqui serão feitos alguns testes simples...')
    todos_erros = testa_cesar()


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


def separacoes(cifra):  # Cria uma separação no output gerado.
    titulo = 'Tentando: ' + cifra
    print()
    print('----' * 15)
    print('{:^45}'.format(titulo))
    print('----' * 15)
    print()


def imprimir_testes(chave, mensagem, mensagem_esperada, mensagem_recebida):  # Impressões automaticas.
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
