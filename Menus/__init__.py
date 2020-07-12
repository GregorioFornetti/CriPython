import PySimpleGUI as sg
import webbrowser

dic_link_cifras = {'Cifra de César':'https://github.com/GregorioFornetti/Programa-criptografia/wiki/Cifra-de-C%C3%A9sar',
                   'Substituição simples':'https://github.com/GregorioFornetti/Programa-criptografia/wiki/Cifra-de-substitui%C3%A7%C3%A3o-simples',
                   'Cifra de Vigenère':'https://github.com/GregorioFornetti/Programa-criptografia/wiki/Cifra-de-Vigen%C3%A8re',
                    'Força bruta César': 'https://github.com/GregorioFornetti/Cripythongrafia/wiki/For%C3%A7a-bruta-C%C3%A9sar',
                   'Adivinhador César': 'https://github.com/GregorioFornetti/Cripythongrafia/wiki/Adivinhador-C%C3%A9sar'}
dic_opcoes = {'Cifra de César': ['apenas letras', 'vários caracteres'],
              'Substituição simples': ['apenas letras', 'vários caracteres'],
              'Cifra de Vigenère': ['apenas letras', 'vários caracteres'],
              'Força bruta César': ['apenas letras', 'vários caracteres'],
              'Adivinhador César': ['apenas letras', 'vários caracteres']}

def voltar_para_tela_anterior(tela_anterior, tela_atual):  # Volta para a tela anterior se usuário escolheu botão "retornar".
    tela_anterior.UnHide()
    tela_atual.Close()


def verificar_eventos_gerais(nome_cifra, evento, tela_atual):  # Verifica e executa eventos disponiveis nos menus das cifras.
    if evento == 'link':
        webbrowser.open(dic_link_cifras[nome_cifra])
    elif evento == 'limpar':
        tela_atual.element('output').update('')


def retorna_layout_opçoes(nome_implementacao):
    layout_opçoes = []
    for opçao in dic_opcoes[nome_implementacao]:
        if not layout_opçoes:  # Definir a primeira opção como "default".
            layout_opçoes.append(sg.Radio(opçao, nome_implementacao, key=opçao, default=True))
        else:
            layout_opçoes.append(sg.Radio(opçao, nome_implementacao, key=opçao, default=False))
    return layout_opçoes
