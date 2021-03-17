import kivy      
kivy.require("1.9.1") 
import japanize_kivy # 日本語表示
from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.popup import Popup

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout

from kivy import Config
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '300')
Config.write()
# Window.size = (300, 480)
class Mein(App):
    title = 'kivy demo pop'

    def build(self):
        self.layout = FloatLayout(size=(300, 300))

        button2 = Button(text='pop', size_hint=(.3, .15), pos=(100, 100))
        button2.bind(on_press = self.pop)
        self.layout.add_widget(button2)

        return self.layout

    def pop(self, tt):
        self.layout_pop = GridLayout(cols=1, row_force_default=True, row_default_height=40)
        box_pop = BoxLayout()

        ss = Label(text='ポップアップの表示')
        self.layout_pop.add_widget(ss)
        button3 = Button(text='閉じる')
        button3.bind(on_press = self.popup_yes)
        self.layout_pop.add_widget(button3)

        self.popup = Popup(title='popup',
                        content=self.layout_pop,
                        size_hint=(0.6, 0.5),
                        size=(350, 350))

        self.popup.open()

    def popup_yes(self, instance):
        self.popup.dismiss()


Mein().run()
