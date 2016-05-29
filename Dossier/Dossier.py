import kivy
kivy.require('1.9.1')

from kivy.uix.gridlayout import GridLayout

class Dossier(GridLayout):
    def __init__(self, **kwargs):
        super(Dossier, self).__init__(**kwargs)
        self.cols = 1
        self.padding = 10
        self.spacing = 5
        print("jay")

if __name__ == "__main__":
    print("Run Main.py !")