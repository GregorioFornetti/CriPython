import PySimpleGUI as sg
import Cifras.cifra_de_cesar as cifra_de_cesar
import Cifras.subst_simples as subst_simples
import Menus


def retorna_layout_padrao_traduçao(titulo):
    layout = [[sg.Text(f"{f'Cripythongrafia: {titulo} (tradução)':^110}")],
             [sg.Text('Opções:')],
             Menus.retorna_layout_opçoes(titulo),
             [sg.Text('Mensagem encriptada:'), sg.InputText(key='mensagem')],
             [sg.Text('Chave:'), sg.InputText(key='chave')],
             [sg.Text('Mensagem traduzida:')],
             [sg.Output(size=(75,25), key='output')],
             [sg.Button('Traduzir', key='traduzir'), sg.Button('Abrir guia da cifra', key='link'),
              sg.Button('Limpar tela', key='limpar') ,sg.Button('Retornar', key='retornar')]]
    return layout


def retorna_layout_padrao_encriptaçao(titulo):
    layout = [[sg.Text(f"{f'Cripythongrafia: {titulo} (encriptação)':^110}")],
             [sg.Text('Opções:')],
             Menus.retorna_layout_opçoes(titulo),
             [sg.Text('Mensagem:'), sg.InputText(key='mensagem')],
             [sg.Text('Chave:'), sg.InputText(key='chave')],
             [sg.Text('Mensagem encriptada:')],
             [sg.Output(size=(75,25), key='output')],
             [sg.Button('Encriptar', key='encriptar'), sg.Button('Abrir guia da cifra', key='link'),
              sg.Button('Limpar tela', key='limpar'), sg.Button('Retornar', key='retornar')]]
    return layout


def executar_tela_cifra(titulo, tela_anterior, dicionario_funções_cifras, layout_cifra):
    tela_cifra = sg.Window(titulo, layout_cifra)
    while True:
        evento, valores = tela_cifra.read()
        if evento in ('retornar', None):
            Menus.voltar_para_tela_anterior(tela_anterior, tela_cifra)
            break
        Menus.verificar_eventos_gerais('Cifra de César', evento, tela_cifra)
        if evento == 'encriptar' or evento == 'traduzir':
            for opção, criptografar in dicionario_funções_cifras.items():
                if valores[opção]:  # Verificar a opção escolhida pelo usuário e executar a função referente a ela (armazenada no dicionário).
                    print(criptografar(valores['chave'], valores['mensagem']))


def menu_cifra_de_cesar_encriptação(tela_anterior):
    layout_cifra_de_cesar = retorna_layout_padrao_encriptaçao('Cifra de César')
    dicionario_funções_cesar_encript = {'apenas letras': cifra_de_cesar.encriptar_modo_apenas_letras,
                                        'vários caracteres': cifra_de_cesar.encriptar_modo_varios_caracteres}
    
    executar_tela_cifra('Cifra de César (encriptação)', tela_anterior, dicionario_funções_cesar_encript, layout_cifra_de_cesar)


def menu_cifra_de_cesar_tradução(tela_anterior):
    pass


def menu_subst_simples_encriptação(tela_anterior):
    pass


def manu_subst_simples_tradução(tela_anterior):
    pass


def menu_cifra_de_vigenere_encriptação(tela_anterior):
    pass


def menu_cifra_de_vigenere_tradução(tela_anterior):
    pass