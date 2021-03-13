import tkinter as tk
import tkinter.ttk as ttk # 見た目が変わる

window = tk.Tk()
window.title('tkinter demo')
# window.geometry('480x480')

frame = ttk.Frame(window)
frame.grid()

scale = tk.Scale(frame, orient="vertical", length=200)
scale.grid()

scale = tk.Scale(frame, orient="horizontal", length=200)
scale.grid()

frame.mainloop()
