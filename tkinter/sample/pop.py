import tkinter as tk
import tkinter.ttk as ttk # 見た目が変わる
from tkinter import messagebox


def pop_message():
    messagebox.showinfo('popup', 'ポップアップの表示')

##### ウィンドウ #####
window = tk.Tk()
window.title('tkinter demo')

frame = ttk.Frame(window)
frame.grid()


button_pop = ttk.Button(frame, text='pop表示', command=pop_message)
button_pop.grid(row=0, column=0)

frame.mainloop()