import kivy      
kivy.require("1.9.1") 
import japanize_kivy # 日本語表示
from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.slider import Slider

from kivy.uix.gridlayout import GridLayout

from kivy import Config
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '500')
Config.write()
# Window.size = (300, 480)
class Mein(App):
    title = 'kivy demo Slider'

    def build(self):
        self.layout = GridLayout(cols=2)
        
        # self.float = FloatLayout(size=(300, 300))
        vertical = Slider(min=0, max=100, orientation='vertical')
        vertical.bind(value = self.v_value)
        self.layout.add_widget(vertical)

        self.vertical_Value = Label(text ='0')
        self.layout.add_widget(self.vertical_Value)

        horizontal = Slider(min=0, max=100)
        # horizontal = Slider(min=0, max=100, value=25, width=1)
        horizontal.bind(value = self.h_value)
        self.layout.add_widget(horizontal)

        self.horizontal_Value = Label(text ='0')
        self.layout.add_widget(self.horizontal_Value)
        
        return self.layout

    def h_value(self, instance, brightness): 
        self.horizontal_Value.text = str(int(brightness))

    def v_value(self, instance, brightness): 
        self.vertical_Value.text = str(int(brightness))

Mein().run()
