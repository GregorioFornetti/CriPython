import PySimpleGUI as sg
import cesar
import subst_simples
import testes_simples
import vigenere
import forca_bruta
sg.theme('DarkGrey5')


def main():
    # Lista de criptografias disponiveis:
    lista_criptografia = ['Cifra de César', 'Substituição simples', 'Cifra de Vigenère']

    # Interface principal do programa.
    # Layout da interface principal do programa.
    layout_principal =  [[sg.Text('Criptografias: Tela principal')],
                        [sg.Button('1- Criar mensagem criptografada.', key='1')],
                        [sg.Button('2- Traduzir mensagem criptografada.', key='2')],
                        [sg.Button('3- Ajuda.', key='3')],
                        [sg.Button('4- Testes automatizados', key='4')],
                        [sg.Button('5- Força bruta: Cifra de César.', key='5')],
                        [sg.Button('6- Finalizar programa', key='6')]]
    
    # Criar a interface principal do programa, utilizando o layout a cima.
    tela_principal = sg.Window('Criptografias: Tela principal',layout_principal)
    while True:  # Loop que verifica cada interação do usuário com o programa.
        eventos, valores = tela_principal.read()
        if eventos in ('6', None):
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
            menu_documentacao(tela_principal)
        if eventos == '4':
            # Esconder a tela principal e iniciar a interface "testes automatizados".
            tela_principal.Hide()
            menu_testes(tela_principal)
        if eventos == '5':
            # Esconder a tela principal e inicar a interface "força bruta".
            tela_principal.Hide()
            menu_forca_bruta(tela_principal)
        

def menu_encriptar(tela_p, lista_cript):
    # Interface "criar mensagem encriptada" do programa.
    lista_opcoes = cria_botoes()
    layout_encriptar =  [[sg.Text('Criptografia: encriptar.')],
                        [sg.Text('Tipo de criptografia:'), sg.Combo(lista_cript, key='cifra', enable_events=True)],
                        [sg.Text('Opções:')],
                        lista_opcoes,
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
            tela_encriptar.Close()
            tela_p.UnHide()
            break
        if eventos == '1':
            # Encriptar a mensagem.
            executa_criptografia(valores)
        atualiza_tela(tela_encriptar, valores)
        


def menu_traducao(tela_p, lista_cript):
    # Interface "traduzir mensagem encriptada" do programa.
    lista_opcoes = cria_botoes()
    layout_traduzir =   [[sg.Text('Criptografia: traduzir.')],
                        [sg.Text('Tipo de criptografia:'), sg.Combo(lista_cript, key='cifra', enable_events=True)],
                        [sg.Text('Opção:')],
                        lista_opcoes,
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
        atualiza_tela(tela_traduzir, valores)


def executa_criptografia(dic_criptografia):  # Função que irá levar o input do user para funções que fazem a criptografia.
    # Extrair todas informações fornecidas pelo usuário.
    cript_escolhida = dic_criptografia['cifra']
    mensagem = dic_criptografia['mensagem']
    chave = dic_criptografia['chave']
    msg_encriptada = 'Por favor, selecione uma cifra!'
    if cript_escolhida == 'Cifra de César':
        # Usuário escolheu encriptar pela cifra de cesar.
        msg_encriptada = cesar.cifra_de_cesar(chave, mensagem)
    if cript_escolhida == 'Substituição simples':
        # Usuário escolheu encriptar pela substituiçao simples.
        msg_encriptada = subst_simples.subst_simples(chave, mensagem)
    if cript_escolhida == 'Cifra de Vigenère':
        # Usuário escolheu encriptar pela cifra de vigenere.
        msg_encriptada = vigenere.vigenere(chave, mensagem)
    print(msg_encriptada)


def traduz_criptografia(dic_criptografia):  # Função que irá levar o input do usuario para as funções que traduzem a mensagem.
    # Extrair os inputs do usuário.
    cript_escolhida = dic_criptografia['cifra']
    mensagem = dic_criptografia['mensagem']
    chave = dic_criptografia['chave']
    traducao = 'Por favor, selecione uma cifra!'
    if cript_escolhida == 'Cifra de César':
        # Usuário escolheu traduzir a cifra de cesar.
        traducao = cesar.traduz_cesar(chave, mensagem)
    if cript_escolhida == 'Substituição simples':
        # Usuário escolheu traduzir a substituição simples.
        traducao = subst_simples.traduz_subst_simples(chave, mensagem)
    if cript_escolhida == 'Cifra de Vigenère':
        # Usuário escolheu traduzir a Cifra de Vigenère.
        traducao = vigenere.cria_chave_traducao(chave, mensagem)
    print(traducao)


def menu_documentacao(tela_p):
    # Layou do menu de ajuda.
    layout_documentacao = [[sg.Text('        Menu de ajuda         ')],
                          [sg.Text('Na opção 1 do menu principal, escolha uma cifra, uma mensagem')],
                          [sg.Text('e uma chave, e caso a chave seja valida, será imprimido uma mensagem encriptada')],
                          [sg.Text('Na opção 2 do menu principal, escolha uma cifra, uma mensagem encriptada')],
                          [sg.Text('e uma chave, e caso a chave seja valida, será imprimido uma mensagem traduzida')],
                          [sg.Text('Na opção 4, é possível ver alguns testes, que podem ajudar no entendimento')],
                          [sg.Text('das cifras disponiveis e suas funcionalidades.')],
                          [sg.Text('Acesse o site abaixo para ter mais informações:')],
                          [sg.Output()],
                          [sg.Button('Retornar',key='retorno')]]
    tela_doc = sg.Window('Menu ajuda', layout_documentacao)
    ja_mostrou = False
    while True:
        eventos, valores = tela_doc.read(timeout=1000)
        if not ja_mostrou:  # Mostrar o link apenas uma vez.
            print('https://github.com/GregorioFornetti/Programa-criptografia/wiki')
            ja_mostrou = True
        if eventos in ('retorno', None):
            # Usuário clicou em retornar ou fechar.
            tela_p.UnHide()
            tela_doc.close()
            break


def menu_testes(tela_p):
    layout_testes = [[sg.Text('Testes automatizados para verificar se o programa está funcionando corretamente.')],
                    [sg.Output(size=(120,40))],
                    [sg.Button('Retornar',key='retorno'), sg.Button('Testar',key='testar')]]

    tela_testes = sg.Window('Menu testes automatizados', layout_testes)
    while True:
        eventos, valores = tela_testes.read()
        if eventos in ('retorno', None):
            # Usuário saiu do menu ou clicou em "retornar".
            tela_p.UnHide()
            tela_testes.close()
            break
        if eventos in ('testar'):
            # O usuário clicou em "testar".
            testes_simples.testar()


def menu_forca_bruta(tela_p):
    layout_forca_bruta = [[sg.Text('             Força bruta: Cifra de César')],
                          [sg.Text('Escreva uma mensagem encriptada. Clique em testar e todas as chaves')],
                          [sg.Text('da cifra de césar serão testadas na força bruta.')],
                          [sg.Text('Mensagem encriptada:'), sg.Input(key='mensagem')],
                          [sg.Output(size=(100,35))],
                          [sg.Button('Testar', key='testar'), sg.Button('Retornar', key='retorno')]]
    tela_forca_bruta = sg.Window('Menu força bruta', layout_forca_bruta)
    while True:
        eventos, valores = tela_forca_bruta.read()
        if eventos in ('retorno', None):
            # Fechar a tela atual e abrir a tela principal.
            tela_p.UnHide()
            tela_forca_bruta.close()
            break
        if eventos == 'testar':
            # Efetuar teste.
            forca_bruta.forca_bruta_cesar(valores['mensagem'])


def cria_botoes():
    return  [sg.Radio('Cifra de César (apenas letras)     ', "Cesar", default=True, visible=False, key='Cifra de César1'),
            sg.Radio('Cifra de César (todos caracteres)', "Cesar", visible=False, key='Cifra de César2'),
            sg.Radio('Substituição simples', "Subst_simples", default=True, visible=False, key='Substituição simples1'),
            sg.Radio('Cifra de Vigenère (apenas letras)    ', "Vigenere", default=True, visible=False, key='Cifra de Vigenère1'),
            sg.Radio('Cifra de Vigenère (todos caracteres)', "Vigenere", visible=False, key='Cifra de Vigenère2')]


def atualiza_tela(tela, valores):
    cifra_selecionada = valores['cifra']
    valores_visiveis = ['mensagem', 'chave', 'cifra']
    for key in valores.keys():
        if key in valores_visiveis:
            continue
        elemento_atual = tela[key]
        if cifra_selecionada in key:
            elemento_atual.Update(visible=True)
        else:
            elemento_atual.Update(visible=False)
            



main()