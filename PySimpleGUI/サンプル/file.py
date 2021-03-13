import PySimpleGUI as sg

layout = [
    [sg.FileBrowse('ファイル選択', key='file')]
    ]

window = sg.Window('PySimpleGUI demo file', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event is None:
        break

    print(event, values)
window.close()