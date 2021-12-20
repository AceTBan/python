jour = int(input("indiquez votre jour de naissance (le chiffre)"))
mois = int(input("indiquez le chiffre de votre mois de naissance (3 pour mars par exemple"))
annee = int(input("indique votre annee de naissance"))

if annee > 2021-18:
    print("vous n'etes pas majeur")
elif mois > 12:
    print("vous n'etes pas majeur")
elif mois == 12 and jour > 16:
    print("vous n'etes pas majeur")
else:
    print("vous etes majeur")

if (annee > 2021-18) or (annee > 2021-18 and mois == 12 and jour > 16):
    print("vous n'etes pas majeur")
else:
    if annee == 2021-18 and jour == 16 and mois == 12:
        print("bon anniversaire")
    print("vous etes majeur")