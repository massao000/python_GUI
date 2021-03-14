import PySimpleGUI as sg

layout = [
    # [sg.Checkbox(i) for i in range(3)],
    # [sg.Radio(i, "RADIO1", default=True) for i in range(3)],
    [sg.Text('チェックボックス')],
    [sg.Checkbox(1), sg.Checkbox(2), sg.Checkbox('3')],
    [sg.Text('ラジオボタン')],
    [sg.Radio(1, "RADIO1", default=True), sg.Radio(2, "RADIO1"), sg.Radio('3', "RADIO1")],
    [sg.Button('button'), sg.Button('exti', key='exti')]
    ]

window = sg.Window('PySimpleGUI demo button', layout)

while True:
    event, values = window.read()

    if event == 'exti' or event is None:
        break

    print(event, values)
window.close()