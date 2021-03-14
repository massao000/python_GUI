import PySimpleGUI as sg


sg.theme("dark blue")


tab1_layout = [
        [sg.Text('▼表示テキストの入力▼')],
        [sg.Input(key='in-text')],
        [sg.Text('ここの文字が変わります', size=(50,1), key='out-text')],
        [sg.Checkbox('チェックボックス->', key='test'), sg.Text('off', size=(3,1), key='Check')],
        [sg.Button('実行', button_color=('midnightblue', '#87cefa')), 
        sg.Button('pop', button_color=('midnightblue', '#87cefa'))],
        ]

tab2_layout =[
        [sg.Text('ファルダ選択', size=(15, 1)), sg.Input(size=(20, 1)), 
        sg.FileBrowse('ファイル選択', button_color=('midnightblue', '#87cefa'))],
        ]

layout = [
    [sg.TabGroup(
        [[sg.Tab('T1', tab1_layout), 
        sg.Tab('T2', tab2_layout)]]
    )]
    ]

window = sg.Window('PySimpleGUI demo', layout)

text_elem = window['Check']
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event is None:
        break
    if event == '実行':
        window['out-text'].update(values['in-text'])
    elif event == 'pop':
        sg.Popup('ポップアップの表示', button_color=('midnightblue', '#87cefa'))

    text_convert = ''
    if values['test']:
        text_convert = 'on'
        # window['Check'].update('on')
    else:
        text_convert = 'off'
    text_elem.update(text_convert)
    print(event, values)
window.close()
