from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

from kivy.uix.label import Label
class MyApp(App):
    """
    MyApp here
        :param App:
    """

    def build(self):
        """
        build here
            :param self:
        """

        layout = BoxLayout(size_hint=(1, None))
        layout.orientation = 'vertical'

        layout.bind(minimum_height=layout.setter('height'))
        for i in range(30):
            data = 'test' + str(i)
            btn = Label(text=data, height=30, size_hint=(1, None))
            layout.add_widget(btn)

        root = ScrollView(size_hint=(1, None), size=(
            Window.width, Window.height))

        root.add_widget(layout)

        return root


if __name__ == '__main__':
    MyApp().run()