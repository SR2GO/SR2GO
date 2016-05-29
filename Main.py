#!/usr/bin/python
# -*- coding: utf-8 -*-
import kivy
kivy.require('1.9.1')

from kivy.app import App, Builder
from kivy.garden.navigationdrawer import NavigationDrawer
from kivy.uix.label import Label

class CustomNavigationDrawer(NavigationDrawer):
    def __init__(self):
        super(CustomNavigationDrawer, self).__init__()

class SR2GO(App):
    def __init__(self):
        super(SR2GO, self).__init__()
        self.main = None
        self.nav = None

    def build(self):
        Builder.load_file("SR2GO.kv")
        self.nav = CustomNavigationDrawer()
        self.main = Label(text="Label")
        return self.nav

    def open_arsenal(self):
        pass

    def open_dossier(self):
        pass

    def open_npc(self):
        pass

    def open_run(self):
        pass

if __name__ == "__main__":
    SR2GO().run()