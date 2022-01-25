from ClassePrenium import *


user = Compte(nom)

while True:
    choix = int(input("Que voulez vous faire ?\n\t"
                      "1: visualiser votre solde\n\t"
                      "2: créditer votre compte\n\t"
                      "3: débiter votre compte\n\t"
                      "4: Afficher vos les crédits éffectués\n"
                      "5: quitter"))
    if choix == 1:
        user.Afficher()
    elif choix == 2:
        montant = int(input("de combien souhaitez vous créditer ?\n"))
        user.Crediter(montant)
    elif choix == 3:
        mont= int(input("de combien souhaitez vous débiter ?\n"))
        user.Debiter(mont)
    elif choix == 4:
        user.AfficherCredits()
    else:
        print("Au revoir")
        break





while True:
#Définition du type d'utilisateur
    choix = input("Etes vous un nouveau client ? (y/n)\n")

    #nouveau utilisateur
    if choix == "y":
        choix = input("souhaitez vous creer un compte prenium ? (y/n)\n")

#creation d'un compte prenium
        if choix == "y":

#creation d'un compte classique
        elif choix == "n":

        else:
            print("Entrée incorrecte, redémarrage du programme")
    elif choix == "quit":
        break
    else:
        print("Entrée incorrecte, redémarrage du programme")
