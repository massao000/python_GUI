import kivy      
kivy.require("1.9.1") 
import japanize_kivy # 日本語表示
from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from  kivy.uix.textinput import TextInput

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy import Config
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '150')
Config.write()
# Window.size = (300, 480)
class Mein(App):
    title = 'kivy demo inp_text'

    def build(self):
        self.layout = GridLayout(cols=1, row_force_default=True, row_default_height=40)

        self.label = Label(text='▼表示テキストの入力▼', font_size=(25), size_hint_x=None, width=300)
        self.layout.add_widget(self.label)

        box = BoxLayout()
        self.inp = TextInput(text='', size_hint_x=2)
        box.add_widget(self.inp)

        button = Button(text='実行')
        button.bind(on_press = self.label_change)
        box.add_widget(button)
        self.layout.add_widget(box)

        self.label2 = Label(text="ここの文字が変わります", font_size=(25)) # , size_hint_x=None, width=160
        self.layout.add_widget(self.label2)

        return self.layout
    
    def label_change(self, label):
        if self.inp.text != '':
            self.label2.text = self.inp.text
        else:
            self.label2.text = "ここの文字が変わります"

Mein().run()
