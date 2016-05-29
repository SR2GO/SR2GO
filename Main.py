#!/usr/bin/python
# -*- coding: utf-8 -*-
import kivy
kivy.require('1.9.1')

from kivy.app import App, Builder
from kivy.garden.navigationdrawer import NavigationDrawer
from kivy.uix.label import Label
from kivy.uix.image import Image

from Dossier.Dossier import Dossier

class CustomNavigationDrawer(NavigationDrawer):
    def __init__(self):
        super(CustomNavigationDrawer, self).__init__()
        self.main = self.ids.main
        self.title = self.ids.title
        self.widget = None

    def set_main(self,widget,title):
        self.title.text=title
        if self.main and self.widget:
            self.main.remove_widget(self.widget)
        self.widget = widget
        self.main.add_widget(widget)

class SR2GO(App):
    def __init__(self):
        super(SR2GO, self).__init__()
        self.nav = None
        self.dossier = Dossier(self)

    def build(self):
        Builder.load_file("SR2GO.kv")
        self.nav = CustomNavigationDrawer()
        self.nav.set_main(Image(source="images/sample.png"), "SR 20 GO")  #Splashscreen
        return self.nav

    def load(self, widget, name):
        self.nav.set_main(widget,name)

    def open_arsenal(self):
        self.load(Label(text="Arsenal"), "Arsenal")
        self.nav.toggle_state()

    def open_dossier(self):
        self.load(self.dossier, "Dossier")
        self.nav.toggle_state()

    def open_npc(self):
        self.load(Label(text="NPC Database"), "NPC Database")
        self.nav.toggle_state()

    def open_run(self):
        self.load(Label(text="Run Database"), "Run Database")
        self.nav.toggle_state()

if __name__ == "__main__":
    SR2GO().run()