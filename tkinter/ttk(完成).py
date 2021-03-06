import tkinter as tk
import tkinter.ttk as ttk # 見た目が変わる
from tkinter import messagebox
import tkinter.filedialog
from tkinter import filedialog
import os


def pop_message():
    messagebox.showinfo('popup', 'ポップアップの表示')

def change_text(event):
    ch_text = textbox.get()
    textbox.delete(0, tk.END)
    change["text"] = ch_text

def changebox_click():
    if bln.get():
        # print('on')
        changebox_text["text"] = 'on'
    else:
        # print('No')
        changebox_text["text"] = 'off'

def open_file():
    fileType = [('','')]
    dirpath = os.path.abspath(os.path.dirname(__file__))
    filepath = filedialog.askopenfilename(filetypes=fileType,initialdir = dirpath)
    textbox2.insert(0, filepath)

def file_pop():
    file = textbox2.get()
    if file != '':
        messagebox.showinfo('ファイルパス表示', file)
    else:
        messagebox.showinfo('ファイルパス表示', 'ファイルパスがありません')
    


##### ウィンドウ #####
window = tk.Tk()
window.title('tkinter demo')
# window.geometry('480x480')

frame = ttk.Frame(window)
frame.grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)

note = ttk.Notebook(frame)
note.grid(column=0, row=0, padx=5, pady=5, sticky=tk.NSEW)

frame2 = ttk.Frame(frame)
frame2.grid(columnspan=2, column=0, row=8, padx=5, pady=5, sticky=tk.W+tk.E)


style = ttk.Style()
style.theme_use('classic')


##### テキストの変換 #####
label = ttk.Label(frame, text='▼表示テキストの入力▼')
label.grid(row=0, column=0)

textbox = ttk.Entry(frame)
textbox.grid(row=1, column=0)

button = ttk.Button(frame, text='実行')
button.grid(row=1, column=1, sticky=tk.W)
button.bind('<Button-1>', change_text)

change = ttk.Label(frame, text='ここの文字が変わります')
change.grid(row=2, column=0)


##### ポップアップの表示 #####
button_pop = ttk.Button(frame, text='pop', command=pop_message)
button_pop.grid(row=3, column=0)


##### ボックスボタン #####
bln = tk.BooleanVar()
bln.set('False')
changebox = tk.Checkbutton(frame, variable=bln, text='チェックボックス->', command=changebox_click)
changebox.grid(row=4, column=0)

changebox_text = ttk.Label(frame, text='off')
changebox_text.grid(row=4, column=1, sticky=tk.W)



##### ファイルを開く #####
file_text = ttk.Label(frame, text='ファイル選択')
file_text.grid(row=5, column=0)
button = ttk.Button(frame, text='ファイル選択', command=open_file)
button.grid(row=5, column=2)
# button.bind('<Button-1>', open_file)
textbox2 = ttk.Entry(frame)
textbox2.grid(row=5, column=1)

file_popup = ttk.Button(frame, text='ファイルパス', command=file_pop)
file_popup.grid(row=6, column=0)
# file_popup.bind('<Button-1>', file_pop)


##### コンボボックス #####
cobox = ttk.Combobox(frame)
cobox['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
cobox.set('コンボボックス')
cobox.grid(row=7, column=0)

##### リストボックス #####
lest_box = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
var_list = tk.StringVar(value=lest_box)
Listbox = tk.Listbox(frame, listvariable=var_list, height=5)
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=Listbox.yview)
Listbox["yscrollcommand"] = scrollbar.set
Listbox.grid(row=7, column=1)
scrollbar.grid(row=7, column=2, sticky=(tk.W, tk.N, tk.S))

##### タブの表示 ##### 
tab1 = tk.Frame(note)
tab2 = tk.Frame(note)

tab1_text = ttk.Label(tab1, text='タブ1')
tab1_text.grid(row=0, column=0)

tab2_text = ttk.Label(tab2, text='タブ2')
tab2_text.grid(row=0, column=0)

note.add(tab1, text="Tab1")
note.add(tab2, text="Tab2")
note.grid(row=7, column=3)

##### スクロールバー #####
# var = tk.DoubleVar()
scale = tk.Scale(frame2, orient="horizontal", length=300)
scale.grid(columnspan=2, row=10, column=1, sticky=tk.W+tk.E)

note.mainloop()

# 100行