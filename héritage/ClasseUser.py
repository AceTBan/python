from ClasseCompte import *


class User:
    def __init__(self, nom, mdp):
        self.nom = nom
        self.mdp = mdp

    def CreerCompte(self, montant):
        self.CompteBanquaire = Compte(self.nom)
        self.CompteBanquaire.Crediter(montant)

    def AfficherInformations(self):
        self.CompteBanquaire.Afficher()


# utilisateur = User("ACE", "yuiop")
# utilisateur.CreerCompte(159)
# utilisateur.AfficherInformations()
