from ClassePrenium import *

while True:
#Définition du type d'utilisateur
    choix = input("Etes vous un nouveau client ? (y/n)\n")

#nouveau utilisateur
    if choix == "y":
        choix = input("Souhaitez vous creer un compte prenium ? (y/n)\n")

#creation d'un compte prenium
        if choix == "y":
            nom = input("Saissiez votre NOM:\n")
            mdp = input("Saissiez votre Mot De Passe:\n")
            vip = Prenium()
            vip.CreerCompte(int(input("Combien souhaitez-vous déposer sur le compte?\n")))

#creation d'un compte classique
        elif choix == "n":
            nom = input("Saissiez votre NOM:\n")
            mdp = input("Saissiez votre Mot De Passe:\n")
            utilisateur = User(nom, mdp)
            utilisateur.CreerCompte(int(input("Combien souhaitez-vous déposer sur le compte?\n")))

        else:
            print("Entrée incorrecte, redémarrage du programme")
    elif choix == "quit":
        break
    else:
        print("Entrée incorrecte, redémarrage du programme")

# utilisateur déjà inscrit

    while True:
        choix = int(input("Que voulez vous faire ?\n\t"
                        "1: Visualiser votre solde\n\t"
                        "2: Créditer votre compte\n\t"
                        "3: Débiter votre compte\n\t"
                        "4: Afficher les crédits éffectués\n\t"
                        "5: Quitter\n\t"))
        if choix == 1:
            User.CompteBanquaire.Afficher()
        elif choix == 2:
            montant = int(input("De combien souhaitez vous être créditer ?\n"))
            User.CompteBanquaire.Crediter(montant)
        elif choix == 3:
            mont= int(input("De combien souhaitez vous être débiter ?\n"))
            User.CompteBanquaire.Debiter(montant)
        elif choix == 4:
            User.CompteBanquaire.AfficherCredits()
        else:
            print("Au revoir")
            break
        