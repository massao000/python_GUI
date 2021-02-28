import kivy      
kivy.require("1.9.1") 
import japanize_kivy # 日本語表示
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy import Config
from  kivy.uix.textinput  import  TextInput
from kivy.uix.label import Label

Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '500')
Config.set('graphics', 'resizable', False)

class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

class TestApp(App):
    title = 'kivy'
    def build(self):
        self.bu = Button(text='Hello World')
        return LoginScreen()

TestApp().run()
