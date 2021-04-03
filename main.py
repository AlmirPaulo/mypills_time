    # name = ObjectProperty(None)
    # email = ObjectProperty(None)

    # def press_btn(self):
    #     name = self.var1.text
    #     email = self.var2.text

    #     print(f'User: {name} Email: {email}')

    #     self.var1.text = ''
    #     self.var2.text = ''


import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class OMPBox(Widget):
    def test(self):
        return None

class OhMyPills(App):
    def build(self):
        return OMPBox()

if __name__ == '__main__':
   OhMyPills().run()
