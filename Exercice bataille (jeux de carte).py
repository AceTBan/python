

import random

deck = []
j1 = []
j2 = []





def distribution(j2,j1,deck):
    for i in range(2,14):
        deck.append(i)
        deck.append(i)
        deck.append(i)
        deck.append(i)

    random.shuffle(deck)
    for j in range(0,52,2):
        carte1 = deck[j]
        j1.append(carte1)
        carte2 = deck[j+1]
        j2.append(carte2)
        return j1,j2


def tour(j1,j2):
    carte1=j1[0]
    carte2=j2[0]
    if carte1<carte2:
        j2.pop(0)
        j1.append(carte1)
        j1.pop(0)
        j1.append(carte2)
        affichage(j1,j2,carte1,carte2)
        print("j1 gagne")

    elif carte1>carte2:
        j1.pop(0)
        j2.append(carte1)
        j2.pop(0)
        j2.append(carte2)
        affichage(j1,j2,carte1,carte2)
        print("j2 gagne")

    elif carte1==carte2:
        print("exeko")
        exeko_j1 = []
        exeko_j2 = []
        exeko_j1.append(carte1)
        exeko_j2.append(carte2)
        j1.pop(0)
        j2.pop(0)
        affichage(j1,j2,carte1,carte2)
        while carte1==carte2:
            exeko_j1.append(j1[0])
            exeko_j2.append(j2[0])
            j1.pop(0)
            j2.pop(0)
            exeko_j1.append(j1[0])
            exeko_j2.append(j2[0])
            carte1=j1[0]
            carte2=j2[0]
            j1.pop(0)
            j2.pop(0)

            if carte1>carte2:
                j1+exeko_j1
                j1+exeko_j2
                affichage(j1,j2,carte1,carte2)
                print("j1 gagne")

            elif carte1<carte2:
                j2 + exeko_j1
                j2 + exeko_j2
                affichage(j1,j2,carte1,carte2)
                print("j1 gagne")





def affichage(j1,j2,carte1,carte2):
    if carte1==14:
        carte1 ="as"
    if carte2==14:
        carte2="as"
    if carte1==13:
        carte1="roi"
    if carte2==13:
        carte2="roi"
    if carte1==12:
        carte1="dame"
    if carte2==12:
        carte2="dame"
    if carte1==11:
        carte1="valet"
    if carte2==11:
        carte2="valet"
    print("j1:",carte1,"j2",carte2)






while j1 or j2:
    if not j1:
        print ("j1 perd")
        break
    if not j2:
        print ("j2 perd")
    else:
        tour(j1,j2)
        print("commencer?")
        continuer=input()