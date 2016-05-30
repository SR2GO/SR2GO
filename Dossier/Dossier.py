import kivy
kivy.require('1.9.1')

from kivy.app import Builder
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from Dossier.Character import Character
from Dossier.CharacterView import CharacterView

class DossierButton(Button):
    def __init__(self, text = None, char = None):
        super(DossierButton, self).__init__()
        self.Char = char or None
        self.text = text or "DossierButton"

class Dossier(ScrollView):
    def __init__(self, app):
        Builder.load_file("Dossier/Dossier.kv")
        super(Dossier, self).__init__()
        self.App = app
        self.grid = self.ids.grid
        self.grid.bind(minimum_height=self.grid.setter("height"))
        for i in self.load_chars():
            btn = DossierButton(text = i.Name, char = i)
            btn.bind(on_press=self.btn_press)
            self.ids.grid.add_widget(btn)

    def btn_press(self, instance):
        char = instance.Char
        cv = CharacterView(char)
        self.App.load(cv, char.Name)

    def load_chars(self):
        return [Character(str(n)) for n in range(100)]

if __name__ == "__main__":
    print("Run Main.py !")