from datetime import date

class compte:
    creationDate = date.today()
    banque = esteban
    sold = 0

    def __init__(self,prenom):
        self.prenom = prenom

    def credit(self,montant):
        self.sold += montant
        print("votre sold est de {}€",format(self.sold))

    def debit(self,montant):
        self.sold -= montant
        print("votre sold est de {}€",format(self.sold))

    def affichage(self):
        print("vous avez {}€ sur votre sold",format(self.sold))