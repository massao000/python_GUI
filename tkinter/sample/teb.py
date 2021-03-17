import tkinter as tk
import tkinter.ttk as ttk # 見た目が変わる

##### ウィンドウ #####
window = tk.Tk()
window.title('tkinter demo tab')

note = ttk.Notebook(window, height=100, width=200)

tab1 = tk.Frame(note)
tab2 = tk.Frame(note)
tab3 = tk.Frame(note)

tab1_text = tk.Label(tab1, text='タブ1')
tab1_text.grid(row=0, column=0)

tab2_text = tk.Label(tab2, text='タブ2')
tab2_text.grid(row=0, column=0)

tab3_text = tk.Label(tab3, text='タブ3')
tab3_text.grid(row=0, column=0)

note.add(tab1, text="Tab1")
note.add(tab2, text="Tab2")
note.add(tab3, text="Tab3")

note.grid(row=0, column=0)
window.mainloop()
