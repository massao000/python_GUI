import PySimpleGUI as sg

layout = [
    [sg.Slider(range=(0.0,100.0), default_value =0.0, resolution=1.0, size=(10, None))],
    [sg.Slider(range=(0.0,100.0), default_value =0.0, resolution=1.0, orientation='h', size=(35, None))]
    ]

window = sg.Window('PySimpleGUI demo file', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event is None:
        break

    print(event, values)
window.close()