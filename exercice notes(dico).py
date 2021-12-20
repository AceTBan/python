nbrNotes = int(input("Indiquez le nombre de notes à enregistrer\n"))

notes = {}
maxi = 0
mini = 20
matMax = ""
matMin = ""

for i in range(nbrNotes):
    mat = input("indiquez la matière\n")
    val = int(input("indiquez la note de cette matière\n"))
    enregistrement = {mat: val}
    notes.update(enregistrement)
    #notes[mat] = val

for i in notes:
    print(i, notes[i], sep=" : ")

# for i in notes:
#     if notes[i] > maxi:
#         maxi = notes[i]
#         matMax = i
#     if notes[i] < mini:
#         mini = notes[i]
#         matMin = i

print("la note maximale est: {} et c'est la matiere {}. La note minimale est {} et c'est la matiere {}".format(maxi, matMax, mini, matMin))
moyenne = sum(notes.values()) / nbrNotes
print("votre moyenne est de : {}/20".format(moyenne))
maxi = max(notes.values())
mini = min(notes.values())


matMax = list(notes.keys())[list(notes.values()).index(maxi)]
matMin = list(notes.keys())[list(notes.values()).index(mini)]

print(matMax,maxi, sep=" : ")
print(matMin,mini, sep=" : ")