from kivy.app import App
import japanize_kivy # 日本語表示
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.label import Label

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stacklayout import StackLayout

from kivy import Config
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '500')
Config.write()

Builder.load_string('''
<Tabelle>:
    GridLayout:
        cols:1
        row_force_default:True
        row_default_height:40
        Label:
            text:'▼表示テキストの入力▼'
            size_hint_x:None
            width:160
<RV>:
    viewclass: 'Label'
    RecycleBoxLayout:
        default_size: None, dp(56)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
''')

class Tabelle(Label):
    pass

class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{'text': str(x)} for x in range(5)]


class TestApp(App):
    def build(self):
        pass


if __name__ == '__main__':
    TestApp().run()