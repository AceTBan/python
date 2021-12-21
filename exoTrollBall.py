import random

equipe1 = input("indiquez le nom de l'equipe 1\n")
equipe2 = input("indiquez le nom de l'equipe 2\n")

dico1 = {equipe1 : 20 , equipe2 : 20}

while (dico1[equipe1] !=0 and dico1[equipe2] !=0):
    perdant_tour = random.randint(1,2)
    if perdant_tour == 1:
        dico1[equipe1] -=1
    else:
        dico1[equipe2] -=1
    print(dico1)
if dico1[equipe1] == 0:
    print("fin du match, equipe 2 gagnante")
else:
    print("fin du match, equipe 1 gagnante")
#
# import random
#
# equipe1, equipe2 = input("indiquez le nom des équipes (séparés par un espace)\n").split()
#
# scores = {equipe1: 5, equipe2: 5}
# i = 0
#
# while scores[equipe1] != 0 and scores[equipe2] != 0:
#     print("Tour numéro {} : \n{} : {} pts\n{} : {} pts".format(i, equipe1, scores[equipe1], equipe2, scores[equipe2]))
#
#     perdant = random.randint(1, 2)
#     if perdant == 1:
#         scores[equipe1] -= 1
#     else:
#         scores[equipe2] -= 1
#     i += 1
#     input("lancez le tour suivant (touche entrée)")
#
# if scores[equipe1] == 0:
#     print("le grand gagnant est :", equipe2)
# else:
#     print("le grand gagnant est:", equipe1)
#