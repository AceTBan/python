from ClassePrenium import *

inscrits = []

#Définition du type d'utilisateur
while True:
    choix = input("Etes vous un nouveau client ? (y/n)\n")

#nouveau utilisateur
    if choix == "y":
        choix = input("Souhaitez vous creer un compte prenium ? (y/n)\n")

#creation d'un compte prenium
        if choix == "y":
            nom = input("Saissiez votre NOM d'utilisateur:\n")
            mdp = input("Saissiez votre Mot De Passe:\n")
            vip = Prenium(nom, mdp)
            vip.CreerCompte(int(input("Combien souhaitez-vous déposer sur le compte?\n")))
            inscrits.append(vip)
#creation d'un compte classique
        elif choix == "n":
            nom = input("Saissiez votre NOM d'utilisateur:\n")
            mdp = input("Saissiez votre Mot De Passe:\n")
            utilisateur = User(nom, mdp)
            utilisateur.CreerCompte(int(input("Combien souhaitez-vous déposer sur le compte?\n")))
            inscrits.append(utilisateur)

# utilisateur déjà inscrit
# vérifier si le nom & le mdp est déjà présent dans la liste inscrits

    elif choix == "n":
        
        nom = input("Bonjours chère client veuiilez entrez votre nom d'utilisateur\n")
        mdp = input("Veuillez entrez le mot de passe\n")
        for i in inscrits:
            if i.nom == nom and i.mdp == mdp:

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
                    
        else:
            print("Entrée incorrecte, redémarrage du programme")
    elif choix == "quit":
        break
    else:
        print("Entrée incorrecte, redémarrage du programme")
    