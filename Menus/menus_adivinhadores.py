import PySimpleGUI as sg
import Menus
import Adivinhadores.forca_bruta_cesar as forca_bruta_cesar


def criar_layout_padrao_advinhador(titulo, nome_adivinhador):
    return [[sg.Text(titulo)],
            [sg.Text('Opções')],
            Menus.retorna_layout_opçoes(nome_adivinhador),
            [sg.Text('Mensagem encriptada:'), sg.Input(key='mensagem')],
            [sg.Output(key='output', size=(75,25))],
            [sg.Button('Executar', key='executar'), sg.Button('Abrir guia', key='link'),
             sg.Button('Limpar tela', key='limpar'), sg.Button('Retornar', key='retornar')]]


def menu_forca_bruta_cesar(tela_anterior):
    mensagem_inicial = '''
    Escolha uma opção de e escreva uma mensagem encriptada pela cifra de César.
    Testaremos todas as chaves possíveis!
    '''
    layout_advinha_cesar = criar_layout_padrao_advinhador(mensagem_inicial, 'Força bruta César')
    tela_advinha_cesar = sg.Window('Cripythongrafia: força bruta César', layout_advinha_cesar)
    while True:
        evento, valores = tela_advinha_cesar.read()
        if evento in ('retornar', None):
            Menus.voltar_para_tela_anterior(tela_anterior, tela_advinha_cesar)
            break
        Menus.verificar_eventos_gerais('Cifra de César', evento, tela_advinha_cesar)
        if evento == 'executar':
            if valores['apenas letras']:
                forca_bruta_cesar.apenas_letras(valores['mensagem'])
            else:
                forca_bruta_cesar.varios_caracteres(valores['mensagem'])
