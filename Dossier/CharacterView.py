import kivy
kivy.require('1.9.1')

from kivy.app import Builder
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label

class CharacterViewLabel(Label):
    def __init__(self):
        super(CharacterViewLabel, self).__init__()

class CharacterView(ScrollView):
    """Provides the UI to a Character"""
    def __init__(self, character, **kwargs):
        Builder.load_file("Dossier/CharacterView.kv")
        super(CharacterView, self).__init__(**kwargs)
        self.character = character
        self.grid = self.ids.grid
        self.grid.bind(minimum_height=self.grid.setter("height"))
