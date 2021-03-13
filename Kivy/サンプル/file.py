import kivy      
kivy.require("1.9.1") 
import japanize_kivy # 日本語表示
from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.button import Button
from  kivy.uix.textinput import TextInput
from  kivy.uix.filechooser import FileChooser, FileChooserListLayout, FileChooserIconLayout
from kivy.uix.popup import Popup

from kivy.uix.boxlayout import BoxLayout

from kivy import Config
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '500')
Config.write()
# Window.size = (300, 480)
class Mein(App):
    title = 'kivy demo file'

    def build(self):
        self.layout = BoxLayout()

        button2 = Button(text='リスト型')
        button2.bind(on_press = self.pop_flie_list)
        self.layout.add_widget(button2)

        button2 = Button(text='ファイルアイコン')
        button2.bind(on_press = self.pop_file_icon)
        self.layout.add_widget(button2)

        return self.layout

    def pop_flie_list(self, tt):
        box_pop = BoxLayout(orientation="vertical")

        float_layout = FileChooser()

        float_layout_list = FileChooserListLayout()
        float_layout.add_widget(float_layout_list)
        box_pop.add_widget(float_layout)
        
        button3 = Button(text='閉じる', size_hint=(.3, .1))
        button3.bind(on_press = self.popup_close)
        box_pop.add_widget(button3)

        self.popup = Popup(title='ファイル', content=box_pop)
        self.popup.open()

    def pop_file_icon(self, tt):
        box_pop = BoxLayout(orientation="vertical")

        float_layout = FileChooser()

        float_layout_icon = FileChooserIconLayout()
        float_layout.add_widget(float_layout_icon)
        box_pop.add_widget(float_layout)
        
        button3 = Button(text='閉じる', size_hint=(.3, .1))
        button3.bind(on_press = self.popup_close)
        box_pop.add_widget(button3)

        self.popup = Popup(title='ファイル', content=box_pop)
        self.popup.open()

    def popup_close(self, instance):
        self.popup.dismiss()


Mein().run()
