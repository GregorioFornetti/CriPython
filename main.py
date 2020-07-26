import PySimpleGUI as sg
import webbrowser
import Cifras.cifra_de_cesar as cifra_de_cesar
import Cifras.cifra_de_vigenere as cifra_de_vigenere
import Cifras.subst_simples as subst_simples
import Menus.menus_utilitarios as menus_utilitarios
import Menus.menus_cifras as menus_cifras

sg.theme('DarkGrey5')
lista_criptografias_disponiveis = ['Cifra de César', 'Substituição simples', 'Cifra de Vigenère']
lista_utilitarios_disponiveis = ['Força bruta César', 'Adivinhador César']
dic_opçoes_disponiveis = {'Cifra de César': ['apenas letras', 'vários caracteres'],
                          'Substituição simples':['apenas letras', 'vários caracteres'],
                          'Cifra de Vigenère':['apenas letras', 'vários caracteres']}
dic_links = {'Cifra de César':'https://github.com/GregorioFornetti/Programa-criptografia/wiki/Cifra-de-C%C3%A9sar',
            'Substituição simples':'https://github.com/GregorioFornetti/Programa-criptografia/wiki/Cifra-de-substitui%C3%A7%C3%A3o-simples',
            'Cifra de Vigenère':'https://github.com/GregorioFornetti/Programa-criptografia/wiki/Cifra-de-Vigen%C3%A8re',
            'Wiki':'https://github.com/GregorioFornetti/Cripythongrafia/wiki',
            'Testes':'https://github.com/GregorioFornetti/Cripythongrafia/wiki/Op%C3%A7%C3%B5es-do-menu#4--testes-automatizados'}

def main():
    # Layout da interface principal do programa.
    layout_principal =  [[sg.Text('       Cripythongrafia: Tela principal')],
                        [sg.Button('1- Criar mensagem criptografada', key='1')],
                        [sg.Button('2- Traduzir mensagem criptografada', key='2')],
                        [sg.Button('3- Utilitários', key='3')],
                        [sg.Button('5- Ajuda', key='5')],
                        [sg.Button('6- Finalizar programa', key='6')]]
    # Criar a interface principal do programa, utilizando o layout a cima.
    tela_principal = sg.Window('Cripythongrafia: Tela principal',layout_principal)
    while True:  # Loop que verifica as interações do usuários com o menu principal.
        evento, valores = tela_principal.read()
        if evento in ('6', None):
            # Fechar o programa
            tela_principal.close()
            break
        if evento == '1':
            # Iniciar interface "encriptar".
            tela_principal.Hide()
            menu_encriptar(tela_principal)
        if evento == '2':
            # Iniciar a interface "traduzir".
            tela_principal.Hide()
            menu_traducao(tela_principal)
        if evento == '3':
            # Inicar interface "utilitários"
            tela_principal.Hide()
            menu_utilitarios(tela_principal)
        if evento == '5':
            # Abrir wiki ajuda
            webbrowser.open(dic_links['Wiki'])


def retorna_layout_botoes_enumerados(titulo, lista_opcoes):
    layout = [[sg.Text(titulo)]]
    for n, opcao in enumerate(lista_opcoes):
        layout.append([sg.Button(f'{n + 1} - {opcao}', key=opcao)])
    layout.append([sg.Button('Retornar', key='retornar')])
    return layout


def retorna_layout_opcoes(criptografia):
    layout_opçoes = []
    for opçao in dic_opçoes_disponiveis[criptografia]:
        if not layout_opçoes:  # Definir a primeira opção como "default".
            layout_opçoes.append(sg.Radio(opçao, criptografia, key=opçao, default=True))
        else:
            layout_opçoes.append(sg.Radio(opçao, criptografia, key=opçao, default=False))
    return layout_opçoes


def executar_menu(titulo, dicionario_funcoes, tela_anterior, layout):
    tela_atual = sg.Window(titulo, layout)
    while True:
        evento, valores = tela_atual.read()
        if evento in ('retornar', None):
            voltar_para_tela_anterior(tela_anterior, tela_atual)
            break
        tela_atual.Hide()
        for opcao, funcao in dicionario_funcoes.items():
            if evento == opcao:
                funcao(tela_atual)


def menu_encriptar(tela_anterior):
    titulo = 'Cripythongrafia: Encriptação'
    layout_encriptar = retorna_layout_botoes_enumerados(titulo, lista_criptografias_disponiveis)
    dic_funcoes_menus_cifras_encript = {
        'Cifra de César':menus_cifras.menu_cifra_de_cesar_encriptação,
        'Substituição simples':menus_cifras.menu_subst_simples_encriptação,
        'Cifra de Vigenère':menus_cifras.menu_cifra_de_vigenere_encriptação
    }

    executar_menu(titulo, dic_funcoes_menus_cifras_encript, tela_anterior, layout_encriptar)


def menu_traducao(tela_anterior):
    titulo = "Cripythongrafia: Tradução"
    layout_traducao = retorna_layout_botoes_enumerados(titulo, lista_criptografias_disponiveis)
    dic_funcoes_menus_cifras_traduc = {
        'Cifra de César':menus_cifras.menu_cifra_de_cesar_tradução,
        'Substituição simples':menus_cifras.menu_subst_simples_tradução,
        'Cifra de Vigenère':menus_cifras.menu_cifra_de_vigenere_tradução
    }

    executar_menu(titulo, dic_funcoes_menus_cifras_traduc, tela_anterior, layout_traducao)

def menu_utilitarios(tela_anterior):
    titulo = "Cripythongrafia: Utilitários"
    layout_utilitarios = retorna_layout_botoes_enumerados(titulo, lista_utilitarios_disponiveis)
    dic_funcoes_utilitarios = {
        'Força bruta César':menus_utilitarios.menu_forca_bruta_cesar,
        'Adivinhador César':menus_utilitarios.menu_adivinhador_cesar
    }

    executar_menu(titulo, dic_funcoes_utilitarios, tela_anterior, layout_utilitarios)


def voltar_para_tela_anterior(tela_anterior, tela_atual):  # Volta para a tela anterior se usuário escolheu botão "retornar".
    tela_anterior.UnHide()
    tela_atual.Close()


def verificar_eventos_gerais(nome_opcao, evento, tela_atual):  # Verifica e executa eventos disponiveis nos menus das cifras.
    if evento == 'link':
        webbrowser.open(dic_links[nome_opcao])
    elif evento == 'limpar':
        tela_atual.element('output').update('')


main()