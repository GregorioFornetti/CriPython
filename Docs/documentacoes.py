import PySimpleGUI as sg

def documentacao_cifra_de_cesar(tela_d):
    try:
        doc = open('Docs/doc_cifra_de_cesar.txt', 'r')
        texto_doc = doc.read()
        layout_doc_cesar = [[sg.Text(texto_doc)],
                         [sg.Button('Retornar',key='retorno')]]
        tela_doc_cesar = sg.Window('Documentação cifra de cesar', layout_doc_cesar)
        while True:
            eventos, valores = tela_doc_cesar.read()
            if eventos in ('retorno', None):
                tela_d.UnHide()
                tela_doc_cesar.close()
                break
    except:
        return  # TODO


def documentacao_substituicao_simples(tela_d):
    return 5