
# importe la fonction aleatoire
import random
# creation de trois listes (deck qui contient les cartes du jeu - j1 les cartes du joueur n1 & j2 du joueur n2)
deck = []
j1 = []
j2 = []




# fonction "distribution" qui va permettre de melanger les cartes et les distribuer aleatoirement au joueur
def distribution(j2,j1,deck):
    for i in range(2,15):
        deck.append(i)
        deck.append(i)
        deck.append(i)
        deck.append(i)
    # fois 4 parce que (coeur, pique, trefle, coeur)
    random.shuffle(deck)
    for j in range(0,52,2):
        carte1 = deck[j]
        j1.append(carte1)
        carte2 = deck[j+1]
        j2.append(carte2)
    return j1,j2

# fonction "tour" permet le bon fonctionnement du jeu
def tour(j1,j2):
    carte1=j1[0]
    carte2=j2[0]
    if carte1<carte2:                   # celui qui "pop" la carte l'"append" a l'autre
        j1.pop(0)
        j2.append(carte1)
        j2.pop(0)
        j2.append(carte2)
        affichage(j1,j2,carte1,carte2)
        print("joey gagne le tour de jeu")

    elif carte1>carte2:
        j2.pop(0)
        j1.append(carte2)
        j1.pop(0)
        j1.append(carte1)
        affichage(j1,j2,carte1,carte2)
        print("kaiba gagne la manche ")

    elif carte1==carte2:
        print("exeko")
        exeko_j1 = []
        exeko_j2 = []
        exeko_j1.append(carte1)
        exeko_j2.append(carte2)
        j2.pop(0)
        j1.pop(0)
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

            if carte1<carte2:
                j2 + exeko_j1
                j2 + exeko_j2
                affichage(j1,j2,carte1,carte2)
                print("joey gagne la bataille")

            elif carte1>carte2:
                j1+exeko_j1
                j1+exeko_j2
                affichage(j1,j2,carte1,carte2)
                print("kaiba gagne la bataille")




# fonction "affichage" permet d'afficher les figures (as, roi, dame, valet)
def affichage(j1,j2,carte1,carte2):
    if carte1==14:
        carte1="as"
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
    print("kaiba draw an",carte1,"&","joey draw an",carte2)




distribution(j1,j2,deck)
# boucle de jeu (si un joueur n'a plus de carte il perd la partie sinon continue)
while j1 or j2:
    if not j1:
        print ("kaiba perd alors qu'il a 3 dragon blanc aux yeux bleu O_O' ")
        break
    if not j2:
        print ("joey perd mais il a un dragon noir aux yeux rouge hyper styler alors ca va ^^")
    else:
        tour(j1,j2)