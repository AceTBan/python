from banque import *

utilisateur = input ('choisissez un prenom pour votre compte:')
monCompte = compte(utilisateur)

while True:
    choix = int(input('appuyez sur 1 pour créditer votre compte \n appuyez sur 2 pour débiter votre compte \n appuyez sur 3 pour voir votre sold')
    if choix == 1:
        somme = int(input('de combien voulez vous créditez votre compte ?'))
        credit(somme)
    if choix == 2:
        retire == int(input('de combien voulez vous ?'))
        debit(retire)
    if choix == 3:
        affichage()
    else:
        print('a bientot')
        break