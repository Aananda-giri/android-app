
import random
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyRoot(BoxLayout):
    def __init__(self):
        super(MyRoot, self).__init()
    def generate_number(self):
        self.random_label.text = str(random.randint(0,10000))


class BasicApp(App):
    def build(self):
        label = Label(text="Hello World")
        return label
        return BoxLayout()
app=BasicApp()
app.run()
