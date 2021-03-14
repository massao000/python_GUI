import kivy      
kivy.require("1.9.1") 
import japanize_kivy # 日本語表示
from kivy import Config
from kivy.app import App
# from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
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

from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stacklayout import StackLayout

Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '500')
Config.write()

# Config.set('graphics', 'width', '500')
# Config.set('graphics', 'height', '500')
# Config.set('graphics', 'resizable', False)

class CustomSpinner(Spinner):
    pass

class CustomGridLayout(GridLayout):
    pass

class Mein(Widget):
    pass
    # def __init__(self, **kwargs):
    #     super(LoginScreen, self).__init__(**kwargs)
    #     self.cols = 2
        # self.add_widget(Label(text='User Name'))
        # self.username = TextInput(multiline=False)
        # self.add_widget(self.username)
        # self.add_widget(Label(text='password'))
        # self.password = TextInput(password=True, multiline=False)
        # self.add_widget(self.password)

        # self.check = CheckBox(active=True)
    # def on_spinner_change(self, text):
    #     print('The spinner', self, 'have text', text)
        

class TestApp(App):
    title = 'kivy'
    def build(self):
        # self.bu = Button(text='Hello World')
        return Mein()

TestApp().run()
