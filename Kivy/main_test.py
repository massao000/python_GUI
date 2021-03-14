import kivy      
kivy.require("1.9.1") 
import japanize_kivy # 日本語表示
from kivy.app import App

from kivy import Config
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from  kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.slider import Slider
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.tabbedpanel import TabbedPanelHeader 
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView

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

        self.label = Label(text='▼表示テキストの入力▼', size_hint_x=None, width=160)
        self.layout.add_widget(self.label)

        box = BoxLayout()
        self.inp = TextInput(text='', size_hint_x=2)
        # self.inp.bind(on_text_validate=self.label_change) # , multiline=False
        box.add_widget(self.inp)
        # self.text = self.self.inp.text

        button = Button(text='実行')
        button.bind(on_press = self.label_change)
        box.add_widget(button)
        self.layout.add_widget(box)

        self.label2 = Label(text="ここの文字が変わります", size_hint_x=None, width=160) # , on_text_validate=self.label_change
        self.layout.add_widget(self.label2)


        self.box2 = BoxLayout()
        self.check_box = CheckBox(size_hint_x=None, width=100, active=True)
        self.box2.add_widget(self.check_box)

        self.check_box.bind(active = self.checkbox_on_off)

        self.check_label = Label(text='ON', size_hint_x=None, width=100)
        self.box2.add_widget(self.check_label)

        self.layout.add_widget(self.box2)
        

        button2 = Button(text='pop', size_hint_x=None, width=120)
        button2.bind(on_press = self.pop)
        self.layout.add_widget(button2)


        self.box3 = BoxLayout()
        button1 = Label(text='フォルダ選択')
        self.box3.add_widget(button1)

        self.inp2 = TextInput(text='', size_hint_x=2)
        self.box3.add_widget(self.inp2)

        button2 = Button(text='フォルダ選択')
        self.box3.add_widget(button2)
        self.layout.add_widget(self.box3)


        self.box4 = BoxLayout()
        self.box4.add_widget(Spinner(text='リスト', 
                                values=Mein.l,
                                size_hint=(None, 1),
                                size=(100, 40),
                                # pos=(200, 60)
                                ))
        self.layout.add_widget(self.box4)

        return self.layout
    
    def label_change(self, label):
        if self.inp.text != '':
            self.label2.text = self.inp.text
        else:
            self.label2.text = "ここの文字が変わります"

    def checkbox_on_off(self, checkbox, value):
        # print(value)
        if value:
            self.check_label.text = "ON"
        else:
            self.check_label.text = "OFF"
    
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
                        size_hint=(0.4, 0.3), # (None, None),
                        size=(400, 400))
        # self.popup.bind(
        #         on_press=self.popup_yes
        #     )
        # popup = Popup(title='Test popup', content=Label(text='Hello world'),
        #       auto_dismiss=False)
        self.popup.open()

    def popup_yes(self, instance):
        self.popup.dismiss()


Mein().run()