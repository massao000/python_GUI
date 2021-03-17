import PySimpleGUI as sg

def text():
    window['out-text'].update(values['in-text'])


layout = [
    [sg.Text('▼表示テキストの入力▼')],
    [sg.Input(key='in-text'), sg.Button('変換')],
    [sg.Text('ここの文字が変わります', size=(50,1), key='out-text')]
    ]

window = sg.Window('PySimpleGUI demo inp_text', layout)

while True:
    event, values = window.read()

    if event is None:
        break

    if event == '変換':
        text()

    print(event, values)
window.close()