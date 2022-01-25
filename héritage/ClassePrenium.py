from ClasseUser import *

class Prenium:
    def __init__(self, nom, mdp):
        super().__init__(nom, mdp)
        self.Emprunt=0

    def Emprunter(self,montant):
        self.CompteBanquaire.Crediter(montant)
