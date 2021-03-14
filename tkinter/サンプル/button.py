import tkinter as tk
import tkinter.ttk as ttk # 見た目が変わる
from tkinter import messagebox
import tkinter.filedialog
from tkinter import filedialog
import os  


##### ウィンドウ #####
window = tk.Tk()
window.title('tkinter demo button')
# window.geometry('480x480')

frame = ttk.Frame(window)
frame.grid()

label_check = ttk.Label(frame, text='チェックボックス')
label_check.grid(row=0, column=1, sticky=tk.W)

bln = tk.BooleanVar()
# bln.set(False)
changebox = tk.Checkbutton(frame, variable=bln, text='1')
changebox.grid(row=1, column=0)

bln = tk.BooleanVar()
changebox = tk.Checkbutton(frame, variable=bln, text='2')
changebox.grid(row=1, column=1)

bln = tk.BooleanVar()
changebox = tk.Checkbutton(frame, variable=bln, text='3')
changebox.grid(row=1, column=2)

# chk_txt = [1, 2, 3]

# chk_bln = {}

# for i in range(len(chk_txt)):
#     chk_bln[i] = tkinter.BooleanVar()
#     chk = tkinter.Checkbutton(frame, variable=chk_bln[i], text=chk_txt[i]) 
#     chk.grid(row=0, column=0 + i)

label_check = ttk.Label(frame, text='ラジオボタン')
label_check.grid(row=2, column=1, sticky=tk.W)

radio = tk.IntVar()
radio.set(0)
changebox = tk.Radiobutton(frame, value=0, variable=radio, text='1')
changebox.grid(row=3, column=0)
changebox = tk.Radiobutton(frame, value=1, variable=radio, text='2')
changebox.grid(row=3, column=1)
changebox = tk.Radiobutton(frame, value=2, variable=radio, text='3')
changebox.grid(row=3, column=2)

button = ttk.Button(frame, text='ボタン')
button.grid(row=4, column=1, sticky=tk.W)
# button.bind('<Button-1>', change_text)

frame.mainloop()

# 100行