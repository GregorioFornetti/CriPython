import PySimpleGUI as sg
import webbrowser
import dicionarios
# Dicionário utilizado para o funcionamento do botão "Acessar wiki". Chave = titulo - Valor = link da wiki github.
dic_links = {'Cifra de César':'https://github.com/GregorioFornetti/Programa-criptografia/wiki/Cifra-de-C%C3%A9sar',
             'Substituição simples':'https://github.com/GregorioFornetti/Programa-criptografia/wiki/Cifra-de-substitui%C3%A7%C3%A3o-simples',
             'Cifra de Vigenère':'https://github.com/GregorioFornetti/Programa-criptografia/wiki/Cifra-de-Vigen%C3%A8re',
             'UTF-8': 'https://github.com/GregorioFornetti/Cripythongrafia/wiki/UTF-8',
             'Base 64': 'https://github.com/GregorioFornetti/Cripythongrafia/wiki/Base64',
             'Bases numéricas': 'https://github.com/GregorioFornetti/Cripythongrafia/wiki/Bases-num%C3%A9ricas',
             'Força bruta César': 'https://github.com/GregorioFornetti/Cripythongrafia/wiki/For%C3%A7a-bruta-C%C3%A9sar',
             'Adivinhador César': 'https://github.com/GregorioFornetti/Cripythongrafia/wiki/Adivinhador-C%C3%A9sar',
             'Conversor bases numéricas': 'https://github.com/GregorioFornetti/Cripythongrafia/wiki/Conversor-bases-num%C3%A9ricas',
             'Encoding base64': 'https://github.com/GregorioFornetti/Cripythongrafia/wiki/Base64---Encoding-de-arquivos',
             'Decoding base64': 'https://github.com/GregorioFornetti/Cripythongrafia/wiki/Base64-Decoding-de-arquivos',
             'Wiki':'https://github.com/GregorioFornetti/Cripythongrafia/wiki',
             'Opcoes':'https://github.com/GregorioFornetti/Cripythongrafia/wiki/Op%C3%A7%C3%B5es-do-menu#4--op%C3%A7%C3%B5es'}


def voltar_para_tela_anterior(tela_anterior, tela_atual):  # Volta para a tela anterior se usuário escolheu botão "retornar".
    tela_anterior.UnHide()
    tela_atual.Close()


def verificar_eventos_gerais(nome_menu, evento, tela_atual):  # Verifica e executa eventos disponiveis nos menus das cifras.
    if evento == 'link':
        webbrowser.open(dic_links[nome_menu])
    elif evento == 'limpar':
        tela_atual.element('output').update('')


def retorna_layout_opçoes_em_radio(lista_opcoes, conexao='radio'):  
    # Cria um layout com opções selecionaveis (do tipo "radio", só pode escolher uma). As opções serão os elementos da lista fornecida.
    layout_opçoes = []
    dic_textos = dicionarios.retorna_opcoes_cifras()
    for opcao in lista_opcoes:
        if not layout_opçoes:  # Definir a primeira opção como "default".
            layout_opçoes.append(sg.Radio(dic_textos[opcao], conexao, key=opcao, default=True))
        else:
            layout_opçoes.append(sg.Radio(dic_textos[opcao], conexao, key=opcao, default=False))
    return layout_opçoes


def retorna_layout_botoes_utilitarios_padrao(dic_textos):
    return [sg.Button(dic_textos['Executar'], key='executar'), sg.Button(dic_textos['Abrir wiki'], key='link'),
            sg.Button(dic_textos['Limpar tela'], key='limpar'), sg.Button(dic_textos['Retornar'], key='retornar')]