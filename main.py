import PySimpleGUI as sg
import cesar
import subst_simples
import Docs.documentacoes


def main():
    # Lista de criptografias disponiveis:
    lista_criptografia = ['Cifra de cesar', 'Substituiçao simples']

    # Interface principal do programa.
    # Layout da interface principal do programa.
    layout_principal = [[sg.Text('Criptografias: Tela principal')],
                        [sg.Button('1- Criar mensagem criptografada.', key='1')],
                        [sg.Button('2- Traduzir mensagem criptografada.', key='2')],
                        [sg.Button('3- Documentação.', key='3')],
                        [sg.Button('4- Testes automatizados', key='4')],
                        [sg.Button('5- Finalizar programa', key='5')]]
    
    # Criar a interface principal do programa, utilizando o layout a cima.
    tela_principal = sg.Window('Criptografias: Tela principal',layout_principal)
    while True:  # Loop que verifica cada interação do usuário com o programa.
        eventos, valores = tela_principal.read()
        if eventos in ('5', None):
            # Fechar o programa
            tela_principal.close()
            break
        if eventos == '1':
            # Esconder a tela principal e iniciar a interface "encriptar".
            tela_principal.Hide()
            menu_encriptar(tela_principal, lista_criptografia)
        if eventos == '2':
            # Esconder a tela principal e iniciar a interface "traduzir".
            tela_principal.Hide()
            menu_traducao(tela_principal, lista_criptografia)
        if eventos == '3':
            # Esconder a tela principal e iniciar a interface "documentação".
            tela_principal.Hide()
            menu_documentacao(tela_principal, lista_criptografia)


def menu_encriptar(tela_p, lista_cript):
    # Interface "criar mensagem encriptada" do programa.
    layout_encriptar =  [[sg.Text('Criptografia: encriptar.')],
                        [sg.Text('Tipo de criptografia:'), sg.Combo(lista_cript, key='cifra')],
                        [sg.Text('Mensagem:'), sg.InputText(key='mensagem')],
                        [sg.Text('Chave:'), sg.InputText(key='chave')],
                        [sg.Text('Mensagem encriptada:')],
                        [sg.Output(size=(70,20))],
                        [sg.Button('Encriptar', key='1'), sg.Button('Retornar', key='2')]]

    tela_encriptar = sg.Window('Criptografias: encriptar', layout_encriptar)
    while True:
        eventos, valores = tela_encriptar.read()
        if eventos in ('2', None):
            # Fechar tela atual e voltar para a tela principal.
            tela_encriptar.close()
            tela_p.UnHide()
            break
        if eventos == '1':
            # Encriptar a mensagem.
            executa_criptografia(valores)


def menu_traducao(tela_p, lista_cript):
    # Interface "traduzir mensagem encriptada" do programa.
    layout_traduzir =   [[sg.Text('Criptografia: traduzir.')],
                        [sg.Text('Tipo de criptografia:'), sg.Combo(lista_cript, key='cifra')],
                        [sg.Text('Mensagem:'), sg.InputText(key='mensagem')],
                        [sg.Text('Chave:'), sg.InputText(key='chave')],
                        [sg.Text('Mensagem traduzida:')],
                        [sg.Output(size=(70,20))],
                        [sg.Button('Traduzir', key='1'), sg.Button('Retornar', key='2')]]

    tela_traduzir = sg.Window('Criptografias: traduzir', layout_traduzir)
    while True:
        eventos, valores = tela_traduzir.read()
        if eventos in ('2', None):
            # Fechar tela atual e voltar para a tela principal.
            tela_p.UnHide()
            tela_traduzir.close()
            break
        if eventos == '1':
            # Traduzir mensagem encriptada.
            traduz_criptografia(valores)


def executa_criptografia(dic_criptografia):  # Função que irá levar o input do user para funções que fazem a criptografia.
    # Extrair todas informações fornecidas pelo usuário.
    cript_escolhida = dic_criptografia['cifra']
    mensagem = dic_criptografia['mensagem']
    chave = dic_criptografia['chave']
    if cript_escolhida == 'Cifra de cesar':
        # Usuário escolheu encriptar pela cifra de cesar.
        cesar.cifra_de_cesar(chave, mensagem)
    if cript_escolhida == 'Substituiçao simples':
        # Usuário escolheu encriptar pela substituiçao simples
        subst_simples.subst_simples(chave, mensagem)


def traduz_criptografia(dic_criptografia):  # Função que irá levar o input do usuario para as funções que traduzem a mensagem.
    # Extrair os inputs do usuário.
    cript_escolhida = dic_criptografia['cifra']
    mensagem = dic_criptografia['mensagem']
    chave = dic_criptografia['chave']
    if cript_escolhida == 'Cifra de cesar':
        # Usuário escolheu traduzir a cifra de cesar.
        cesar.traduz_cesar(chave, mensagem)
    if cript_escolhida == 'Substituiçao simples':
        # Usuário escolheu traduzir a substituição simples.
        subst_simples.traduz_subst_simples(chave, mensagem)


def menu_documentacao(tela_p, lista_cript):
    # Interface do "Menu da documentação".
    layout_documentacao = [[sg.Text('Menu de documentação: escolha a cifra que você deseja obter mais informações.')]]
    for cifra in lista_cript:  # Adicionando todos os botões ao layout (todas cifras disponíveis).
        layout_documentacao.append([sg.Button(cifra,key=cifra)])
    layout_documentacao.append([sg.Text('OBS: visite o o repositório desse programa para uma documentação melhor: https://github.com/GregorioFornetti/Programa-criptografia/wiki')])
    layout_documentacao.append([sg.Button('Retornar', key='retorno')])  # Adicionar o botão de retornar.
    tela_documentacao = sg.Window('Menu Documentação', layout_documentacao)
    while True:
        eventos, valores = tela_documentacao.read()
        if eventos in ('retorno', None):
            # Usuário fechou a aba ou clicou em "retornar".
            tela_p.UnHide()
            tela_documentacao.close()
            break
        if eventos == lista_cript[0]:
            # Usuário escolheu abrir a documentação da "cifra de cesar".
            tela_documentacao.Hide()
            Docs.documentacoes.documentacao_cifra_de_cesar(tela_documentacao)
        if eventos == lista_cript[1]:
            # Usuário escolheu abrir a documentção da "substituição simples".
            tela_documentacao.Hide()

    
main()