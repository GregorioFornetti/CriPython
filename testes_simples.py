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
    print('Chave = 1')
    mensagem_esperada = 'abcdefghijklmnopqrstuvwxyz'
    print('Mensagem = abcdefghijklmnopqrstuvwxyz')
    mensagem_esperada = 'bcdefghijklmnopqrstuvwxyza'
    print(f'Mensagem encriptada esperada: {mensagem_esperada}')
    mensagem_recebida = cesar.cifra_de_cesar('1', 'abcdefghijklmnopqrstuvwxyz')
    print(f'Mensagem encriptada recebida: {mensagem_recebida}')
    if mensagem_recebida == mensagem_esperada:
        print('Passou!')
    else:
        erros += 1
        print('Não passou!')


def separacoes(cifra):  # Cria uma separação no output gerado.
    titulo = 'Tentando: ' + cifra
    print()
    print('----' * 15)
    print('{:^45}'.format(titulo))
    print('----' * 15)
    print()

