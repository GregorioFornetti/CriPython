dic_link_cifras = {'Cifra de César':'https://github.com/GregorioFornetti/Programa-criptografia/wiki/Cifra-de-C%C3%A9sar',
                   'Substituição simples':'https://github.com/GregorioFornetti/Programa-criptografia/wiki/Cifra-de-substitui%C3%A7%C3%A3o-simples',
                   'Cifra de Vigenère':'https://github.com/GregorioFornetti/Programa-criptografia/wiki/Cifra-de-Vigen%C3%A8re'}


def voltar_para_tela_anterior(tela_anterior, tela_atual):  # Volta para a tela anterior se usuário escolheu botão "retornar".
    tela_anterior.UnHide()
    tela_atual.Close()


def verificar_eventos_gerais(nome_cifra, evento, tela_atual):  # Verifica e executa eventos disponiveis nos menus das cifras.
    if evento == 'link':
        webbrowser.open(dic_link_cifras[nome_cifra])
    elif evento == 'limpar':
        tela_atual.element('output').update('')