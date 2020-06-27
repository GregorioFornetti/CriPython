import PySimpleGUI as sg
import forca_bruta
import testes_simples
import Cifras.cifra_de_cesar
import Cifras.cifra_de_vigenere
import Cifras.subst_simples
sg.theme('DarkGrey5')
lista_criptografias_disponiveis = ['Cifra de César', 'Substituição simples', 'Cifra de Vigenère']
dic_opçoes_disponiveis = {'Cifra de César': ['apenas letras', 'vários caracteres'],
                            'Substituição simples':['apenas letras'],
                            'Cifra de Vigenère':['apenas letras', 'vários caracteres']}


def main():
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
        evento, valores = tela_principal.read()
        if evento in ('6', None):
            # Fechar o programa
            tela_principal.close()
            break
        if evento == '1':
            # Esconder a tela principal e iniciar a interface "encriptar".
            tela_principal.Hide()
            menu_encriptar(tela_principal)
        if evento == '2':
            # Esconder a tela principal e iniciar a interface "traduzir".
            tela_principal.Hide()
            menu_traducao(tela_principal)
        if evento == '3':
            # Esconder a tela principal e iniciar a interface "documentação".
            tela_principal.Hide()
            menu_documentacao(tela_principal)
        if evento == '4':
            # Esconder a tela principal e iniciar a interface "testes automatizados".
            tela_principal.Hide()
            menu_testes(tela_principal)
        if evento == '5':
            # Esconder a tela principal e inicar a interface "força bruta".
            tela_principal.Hide()
            menu_forca_bruta(tela_principal)


def cria_layout_traduçao_e_encriptaçao(titulo):
    layout = [[sg.Text(titulo)]]
    for n, criptografia in enumerate(lista_criptografias_disponiveis):
        layout.append([sg.Button(f'{n + 1} - {criptografia}', key=criptografia)])
    layout.append([sg.Button('Retornar', key='retornar')])
    return layout


def retorna_layout_opçoes(criptografia):
    layout_opçoes = []
    for opçao in dic_opçoes_disponiveis[criptografia]:
        if not layout_opçoes:  # Definir a primeira opção como "default".
            layout_opçoes.append(sg.Radio(opçao, criptografia, key=opçao, default=True))
        else:
            layout_opçoes.append(sg.Radio(opçao, criptografia, key=opçao, default=False))
    return layout_opçoes


def retorna_layout_padrao_traduçao(titulo, criptografia):
    layout = [[sg.Text(titulo)],
             [sg.Text('Opções:')],
             retorna_layout_opçoes(criptografia),
             [sg.Text('Mensagem encriptada:'), sg.InputText(key='mensagem')],
             [sg.Text('Chave:'), sg.InputText(key='chave')],
             [sg.Text('Mensagem traduzida:')],
             [sg.Output(size=(80,30))],
             [sg.Button('Traduzir', key='traduzir'), sg.Button('Retornar', key='retornar')]]
    return layout


def retorna_layout_padrao_encriptaçao(titulo, criptografia):
    layout = [[sg.Text(titulo)],
             [sg.Text('Opções:')],
             retorna_layout_opçoes(criptografia),
             [sg.Text('Mensagem:'), sg.InputText(key='mensagem')],
             [sg.Text('Chave:'), sg.InputText(key='chave')],
             [sg.Text('Mensagem encriptada:')],
             [sg.Output(size=(80,30))],
             [sg.Button('Encriptar', key='traduzir'), sg.Button('Retornar', key='retornar')]]
    return layout


def menu_encriptar(tela_anterior):
    layout_encriptar = cria_layout_traduçao_e_encriptaçao('Pythografia: encriptar')
    tela_encriptar = sg.Window('Criptografias: encriptar', layout_encriptar)
    while True:
        evento, valores = tela_encriptar.read()
        if voltou_para_tela_anterior(evento, tela_anterior, tela_encriptar):
            break
        if evento == 'Cifra de César':
            menu_cesar_encriptar(tela_encriptar)
        elif evento == 'Substituição simples':
            menu_subst_simples_encriptar(tela_encriptar)
        else:
            menu_vigenere_encriptar(tela_encriptar)


def menu_traducao(tela_anterior):
    layout_traduzir = cria_layout_traduçao_e_encriptaçao('PythonGrafia: traduzir')
    tela_traduzir = sg.Window('Criptografias: traduzir', layout_traduzir)
    while True:
        evento, valores = tela_traduzir.read()
        if voltou_para_tela_anterior(evento, tela_anterior, tela_traduzir):
            break
        if evento == 'Cifra de César':
            menu_cesar_traduzir(tela_traduzir)
        elif evento == 'Substituição simples':
            menu_subst_simples_traduzir(tela_traduzir)
        else:
            menu_vigenere_traduzir(tela_traduzir)


def menu_cesar_encriptar(tela_anterior):
    layout_cesar_encript = retorna_layout_padrao_encriptaçao('PythonGrafia: Cifra de César (encriptação)', 'Cifra de César')
    tela_cesar_encript = sg.Window('PythonGrafia: Cifra de César', layout_cesar_encript)
    while True:
        evento, valores = tela_cesar_encript.read()
        if voltou_para_tela_anterior(evento, tela_anterior, tela_cesar_encript):
            break
        if valores['apenas letras']:
            print(Cifras.cifra_de_cesar.encriptar_modo_apenas_letras(valores['chave'], valores['mensagem']))
        else:
            print(Cifras.cifra_de_cesar.encriptar_modo_varios_caracteres(valores['chave'], valores['mensagem']))


def menu_cesar_traduzir(tela_anterior):
    layout_cesar_traduc = retorna_layout_padrao_traduçao('PythonGrafia: Cifra de César (tradução)', 'Cifra de César')
    tela_cesar_traduc = sg.Window('PythonGrafia: Cifra de César', layout_cesar_traduc)

    while True:
        evento, valores = tela_cesar_traduc.read()
        if voltou_para_tela_anterior(evento, tela_anterior, tela_cesar_traduc):
            break
        if valores['apenas letras']:
            print(Cifras.cifra_de_cesar.traduzir_modo_apenas_letras(valores['chave'], valores['mensagem']))
        else:
            print(Cifras.cifra_de_cesar.traduzir_modo_varios_caracteres(valores['chave'], valores['mensagem']))


def menu_subst_simples_encriptar(tela_anterior):
    # Criando o layout da substituição simples.
    layout_subst_encript = retorna_layout_padrao_encriptaçao('PythonGrafia: Substituição simples (encriptação)', 'Substituição simples')
    del layout_subst_encript[4]
    layout_subst_encript.insert(4, [sg.Text('Letras mensagem comum:    '), sg.Input(key='letras_comum')])
    layout_subst_encript.insert(5, [sg.Text('Letras mensagem encriptada:'), sg.Input(key='letras_encript')])
    tela_subst_encript = sg.Window('PythonGrafia: Substituição simples', layout_subst_encript)

    while True:
        evento, valores = tela_subst_encript.read()
        if voltou_para_tela_anterior(evento, tela_anterior, tela_subst_encript):
            break


def menu_subst_simples_traduzir(tela_anterior):
    layout_subst_traduc = retorna_layout_padrao_traduçao('PythonGrafia: Substituição simples (tradução)', 'Substituição simples')
    tela_subst_traduc = sg.Window('PythonGrafia: substituição simples', layout_subst_traduc)
    while True:
        evento, valores = tela_subst_traduc.read()
        if voltou_para_tela_anterior(evento, tela_anterior, tela_subst_traduc):
            break


def menu_vigenere_encriptar(tela_anterior):
    layout_vigenere_encript = retorna_layout_padrao_encriptaçao('PythonGrafia: Cifra de Vigenère (encriptação)', 'Cifra de Vigenère')
    tela_vigenere_encript = sg.Window('PythonGrafia: Cifra de Vigenère', layout_vigenere_encript)
    while True:
        evento, valores = tela_vigenere_encript.read()
        if voltou_para_tela_anterior(evento, tela_anterior, tela_vigenere_encript):
            break
        if valores['apenas letras']:
            print(Cifras.cifra_de_vigenere.encriptar_modo_apenas_letras(valores['chave'], valores['mensagem']))
        else:
            print(Cifras.cifra_de_vigenere.encriptar_modo_varios_caracteres(valores['chave'], valores['mensagem']))


def menu_vigenere_traduzir(tela_anterior):
    layout_vigenere_traduc = retorna_layout_padrao_traduçao('PythonGrafia: Cifra de Vigenère (tradução)', 'Cifra de Vigenère')
    tela_vigenere_traduc = sg.Window('PythonGrafia: Cifra de Vigenère', layout_vigenere_traduc)
    while True:
        evento, valores = tela_vigenere_traduc.read()
        if voltou_para_tela_anterior(evento, tela_anterior, tela_vigenere_traduc):
            break
        if valores['apenas letras']:
            print(Cifras.cifra_de_vigenere.traduzir_modo_apenas_letras(valores['chave'], valores['mensagem']))
        else:
            print(Cifras.cifra_de_vigenere.traduzir_modo_varios_caracteres(valores['chave'], valores['mensagem']))


def menu_documentacao(tela_anterior):
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
                          [sg.Button('Retornar',key='retornar')]]
    tela_doc = sg.Window('Menu ajuda', layout_documentacao)
    ja_mostrou = False
    while True:
        evento, valores = tela_doc.read(timeout=1000)
        if not ja_mostrou:  # Mostrar o link apenas uma vez.
            print('https://github.com/GregorioFornetti/Programa-criptografia/wiki')
            ja_mostrou = True
        if voltou_para_tela_anterior(evento, tela_anterior, tela_doc):
            break


def menu_testes(tela_anterior):
    layout_testes = [[sg.Text('Testes automatizados para verificar se o programa está funcionando corretamente.')],
                    [sg.Output(size=(120,40))],
                    [sg.Button('Retornar',key='retorno'), sg.Button('Testar',key='testar')]]

    tela_testes = sg.Window('Menu testes automatizados', layout_testes)
    while True:
        evento, valores = tela_testes.read()
        if voltou_para_tela_anterior(evento, tela_anterior, tela_testes):
            break
        if evento in ('testar'):
            # O usuário clicou em "testar".
            testes_simples.testar()


def menu_forca_bruta(tela_anterior):
    layout_forca_bruta = [[sg.Text('             Força bruta: Cifra de César')],
                          [sg.Text('Escreva uma mensagem encriptada. Clique em testar e todas as chaves')],
                          [sg.Text('da cifra de césar serão testadas na força bruta.')],
                          [sg.Text('Mensagem encriptada:'), sg.Input(key='mensagem')],
                          [sg.Output(size=(100,35))],
                          [sg.Button('Testar', key='testar'), sg.Button('Retornar', key='retornar')]]
    tela_forca_bruta = sg.Window('Menu força bruta', layout_forca_bruta)
    while True:
        evento, valores = tela_forca_bruta.read()
        if voltou_para_tela_anterior(evento, tela_anterior, tela_forca_bruta):
            break
        if evento == 'testar':
            # Efetuar teste.
            forca_bruta.forca_bruta_cesar(valores['mensagem'])


def voltou_para_tela_anterior(evento, tela_anterior, tela_atual):  # Volta para a tela anterior se usuário escolheu botão "retornar".
    if evento in ('retornar', None):
        tela_anterior.UnHide()
        tela_atual.Close()
        return True
    return False


main()