import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class SR2GO(App):
    def build(self):
        return Builder.load_file('SR2GO.kv')

if __name__ == "__main__":
    SR2GO().run()