import PySimpleGUI as sg

tab3_layout = [[sg.Text('タブ1', size=(10,3))]]
tab4_layout = [[sg.Text('タブ2', size=(10,3))]]

layout = [
    [sg.TabGroup([
                [sg.Tab('T1', tab3_layout), 
                 sg.Tab('T2', tab4_layout)]])]
    ]

window = sg.Window('PySimpleGUI demo tab', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event is None:
        break

    print(event, values)
window.close()