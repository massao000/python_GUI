import tkinter as tk
import tkinter.ttk as ttk # 見た目が変わる

def change_text(event):
    ch_text = textbox.get()
    textbox.delete(0, tk.END)
    change["text"] = ch_text


##### ウィンドウ #####
window = tk.Tk()
window.title('tkinter demo')
# window.geometry('480x480')

frame = ttk.Frame(window)
frame.grid()

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

frame.mainloop()