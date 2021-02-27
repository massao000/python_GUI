import PySimpleGUI as sg


sg.theme("dark blue")

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# tab1_layout = [
#         [sg.Text('▼表示テキストの入力▼')],
#         [sg.Input(key='in-text')],
#         [sg.Text('ここの文字が変わります', size=(50,1), key='out-text')],
#         [sg.Checkbox('チェックボックス->', key='test', change_submits=True), sg.Text('off', size=(3,1), key='Check')],
#         [sg.Button('実行', button_color=('midnightblue', '#87cefa')), 
#         sg.Button('pop', button_color=('midnightblue', '#87cefa'))],
#         ] 

# tab2_layout =[
#         [sg.Text('ファルダ選択', size=(13, 1)), sg.Input(size=(20, 1)), 
#         sg.FileBrowse('ファイル選択', key='file', button_color=('midnightblue', '#87cefa'))],
#         [sg.Button('表示', key='hyouji', button_color=('midnightblue', '#87cefa'))],
#         [sg.Combo((number_list), default_value='ナンバーズ', size=(10, 1)),
#         sg.Listbox(number_list, size=(10, 5)), 
#         sg.Slider(range=(0.0,100.0), default_value =0.0, resolution=1.0, orientation='h', size=(35, None))]
#         ]

tab3_layout = [[sg.Text('タブ1', size=(10,3))]]
tab4_layout = [[sg.Text('タブ2', size=(10,3))]]
layout = [
    [sg.Text('▼表示テキストの入力▼')],
    [sg.Input(key='in-text'), sg.Button('実行', button_color=('midnightblue', '#87cefa'))],
    [sg.Text('ここの文字が変わります', size=(50,1), key='out-text')],
    [sg.Checkbox('チェックボックス->', key='test', change_submits=True), sg.Text('off', size=(3,1), key='Check')],
    [ sg.Button('pop', button_color=('midnightblue', '#87cefa'))],
    [sg.Text('ファルダ選択', size=(13, 1)),
        sg.Input(size=(20, 1)), 
        sg.FileBrowse('ファイル選択', key='file', button_color=('midnightblue', '#87cefa'))],

    [sg.Button('ファイルパス表示', key='hyouji', button_color=('midnightblue', '#87cefa'))],
    [sg.Combo((number_list), default_value='コンボボックス', size=(15, 1)),
    sg.Listbox(number_list, size=(10, 5)), sg.TabGroup([
                                             [sg.Tab('T1', tab3_layout), 
                                              sg.Tab('T2', tab4_layout)]])
                                              ],
    [sg.Slider(range=(0.0,100.0), default_value =0.0, resolution=1.0, orientation='h', size=(35, None))],
    
    []
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
    else:
        text_convert = 'off'
    text_elem.update(text_convert)

    if event == 'hyouji':
        if values["file"] != '':
            sg.Popup(values['file'])
        else:
            sg.Popup('ファイルが選択されていない')





    print(event, values)
window.close()
