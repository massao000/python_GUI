import tkinter as tk
import tkinter.ttk as ttk # 見た目が変わる
from tkinter import filedialog
import os



def open_file():
    fileType = [('','')]
    dirpath = os.path.abspath(os.path.dirname(__file__))
    filepath = filedialog.askopenfilename(filetypes=fileType,initialdir = dirpath)

##### ウィンドウ #####
window = tk.Tk()
window.title('tkinter demo')
# window.geometry('480x480')

frame = ttk.Frame(window)
frame.grid()


button = ttk.Button(frame, text='ファイル選択', command=open_file)
button.grid(row=0, column=0)

frame.mainloop()
