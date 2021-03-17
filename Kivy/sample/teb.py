import kivy      
kivy.require("1.9.1") 
import japanize_kivy # 日本語表示
from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.tabbedpanel import TabbedPanelHeader 

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
        self.box4 = BoxLayout()
        self.tab = TabbedPanel(do_default_tab=False)
                    
        tab_text_head = TabbedPanelHeader(text='T1')
        tab_text_head.content = Label(text='タブ1') 

        tab_text_head2 = TabbedPanelHeader(text='T2')
        tab_text_head2.content = Label(text='タブ2')

        tab_text_head3 = TabbedPanelHeader(text='T3')
        tab_text_head3.content = Label(text='タブ3')

        self.tab.add_widget(tab_text_head)
        self.tab.add_widget(tab_text_head2)
        self.tab.add_widget(tab_text_head3)
        self.box4.add_widget(self.tab)

        return self.box4
    
Mein().run()
