import PySimpleGUI as sg

layout = [[sg.Frame('opa', key='aaaa', visible=True,layout=[[sg.Button('oi')]])]]
tela = sg.Window('sla', layout)
while True:
    evento, valores = tela.read(timeout=10000)
    print(valores)
    print(evento)
