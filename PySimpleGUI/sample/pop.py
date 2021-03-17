import PySimpleGUI as sg

def pop_event():
    sg.Popup('ポップアップの表示')

layout = [
    [sg.Button('pop表示')],
    ]

window = sg.Window('PySimpleGUI demo pop', layout)

while True:
    event, values = window.read()

    if event is None: 
        break
    
    if event == 'pop表示':
        pop_event()

    print(event, values)
window.close()