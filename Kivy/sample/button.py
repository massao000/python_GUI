import kivy      
kivy.require("1.9.1") 
import japanize_kivy # 日本語表示
from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout

from kivy import Config
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '250')
Config.write()
# Window.size = (300, 480)
class Mein(App):
    title = 'kivy demo button'

    def build(self):
        self.layout = GridLayout(cols=1, row_force_default=True, row_default_height=40)
        
        self.label_check = Label(text='チェックボックス', size_hint_x=None, width=160)
        self.layout.add_widget(self.label_check)
        
        self.box = BoxLayout()
        self.check_box = CheckBox(size_hint_x=None, width=100, active=True)
        self.box.add_widget(self.check_box)
        self.check_box = CheckBox(size_hint_x=None, width=100)
        self.box.add_widget(self.check_box)
        self.check_box = CheckBox(size_hint_x=None, width=100, active=True)
        self.box.add_widget(self.check_box)
        self.layout.add_widget(self.box)

        self.label_radio = Label(text='ラジオボタン', size_hint_x=None, width=160)
        self.layout.add_widget(self.label_radio)

        self.box2 = BoxLayout()
        self.radio_box = CheckBox(group='radio',size_hint_x=None, width=100, active=True)
        self.box2.add_widget(self.radio_box)
        self.radio_box = CheckBox(group='radio',size_hint_x=None, width=100)
        self.box2.add_widget(self.radio_box)
        self.radio_box = CheckBox(group='radio',size_hint_x=None, width=100)
        self.box2.add_widget(self.radio_box)
        self.layout.add_widget(self.box2)
        
        float_layout = FloatLayout(size=(300, 300))
        button = Button(text='実行', size_hint=(.3, 1), pos=(20, 20))
        # button.bind(on_press = self.label_change)
        float_layout.add_widget(button)
        self.layout.add_widget(float_layout)

        return self.layout

    def click(self, test):
        # 処理を書く
        pass
        
    
Mein().run()
