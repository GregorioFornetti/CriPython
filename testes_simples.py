import subst_simples
import cesar


def testar():  # Função que chamará todos os testes de cifras disponiveis.
    print('Iniciando os testes automatizados...')
    print('Aqui serão feitos alguns testes simples...')
    testa_cesar()


def testa_cesar():  # Função que testa a cifra de césar.
    separacoes('Cifra de César')


def separacoes(cifra):  # Cria uma separação no output gerado.
    titulo = 'Tentando: ' + cifra
    print()
    print('----' * 15)
    print('{:^45}'.format(titulo))
    print('----' * 15)
    print()

