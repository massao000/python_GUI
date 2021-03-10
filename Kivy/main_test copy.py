import kivy      
kivy.require("1.9.1") 
import japanize_kivy # 日本語表示
from kivy.app import App

from kivy import Config
# from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from  kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.widget import Widget
from kivy.core.window import Window

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stacklayout import StackLayout

Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '500')
Config.write()
# Window.size = (300, 480)
class Mein(App):
    l = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
    title = 'kivy'

    def build(self):
        self.layout = GridLayout(cols=1, row_force_default=True, row_default_height=40)
        box = BoxLayout()

        self.label = Label(text='▼表示テキストの入力▼', size_hint_x=None, width=160)
        self.layout.add_widget(self.label)

        inp = TextInput(size_hint_x=2)
        box.add_widget(inp)

        button = Button(text='実行')
        button.bind(on_press = self.test)
        box.add_widget(button)
        self.layout.add_widget(box)

        self.label2 = Label(text='ここの文字が変わります', size_hint_x=None, width=160)
        self.layout.add_widget(self.label2)

        self.layout.add_widget(Spinner(text='リスト', 
                                values=Mein.l,
                                size_hint=(None, None),
                                size=(100, 44),
                                pos=(200, 60)
                                ))
        return self.layout
    
    def test(self, te):
        print('The spinner', self, 'have text', te)


    # def on_spinner_change(self, text):
    #     print('The spinner', self, 'have text', text)


Mein().run()
