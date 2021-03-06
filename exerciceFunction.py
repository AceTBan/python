# # def calcul_age(annee):
# #     return 2022 - annee
# #
# #
# # continuer = True
# # while continuer:
# #     year = input("indiquez votre année de naissance\n")
# #     try:
# #         year = int(year)
# #     except ValueError:
# #         print("veuillez indiquer l'année en chiffres")
# #     else:
# #         continuer = False
# #
# # print(f"vous avez {calcul_age(year)} ans")
#
# def multiplier(nbr1, nbr2):
#     return nbr1*nbr2
#
# nb1,nb2 = input("indiquez deux nombres séparés par des espaces\n").split(" ")
#
# nb1 = int(nb1)
# nb2 = int(nb2)
#
# # autre facon de transformer nb1 et nb2 en int
# # nb1,nb2 = [int(x) for x in input("indiquez deux nombres séparés par un espace\n").split(" ")]
#
# print("{} x {} = {}".format(nb1,nb2,multiplier(nb1,nb2)))

import re

def verif_mail(adresse):
    rex = re.compile("[A-Za-z0-9]{4}@[A-Za-z0-9]{6}\.[A-Z|a-z]{3}")
    if rex.fullmatch(adresse):
        return True
    else:
        return False

def verif_mail_long(adresse):
    # On test si le 5eme caractère est un @ et si le 12eme est un .
    # Si ce n'est pas le cas on return False
    if adresse[4] != "@" or adresse[11] != ".":
        return False
    # On parcours toute notre chaine et on test chaque caractère, sauf le 5eme et le 12eme
    # Si le caractère n'est pas alphanumérique (donc un str chiffre ou lettre) on return False
    for ind, val in enumerate(adresse):
        if (ind < 4) or (ind >= 5 and ind <= 10) or ind > 11:
            if not val.isalnum():
                return False
    # Si on n'a jamais return False c'est que la chaine est correcte, on return donc True
    return True

mail = input("indiquez votre adresse mail\n")

if verif_mail_long(mail):
    print("OK")
else:
    print("KO")

# print("OK" if verif_mail(mail) else "KO")