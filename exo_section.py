# coding: utf-8

import eleves_primaire
from datetime import*

inscription = []
nom = []
prenom = []

saisie = False

while saisie == False:
    try:
        inscrits = int(input("Combien d'élève a ajouter ?\n"))
        saisie = True
    except ValueError:
        print("Vous devez entrer un nombre entier")
else:
    continuer = False

for i in range(inscrits):
    nom.append(input("indiquez le nom de l'lélève\n"))
    prenom.append(input("indiquez le prenom de l'élève\n"))

while True:
    perso = input("Avez-vous d'autre inscription ? y/n \n")
    if perso == "n":
        break
    else:
        inscrits

