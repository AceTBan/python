nb_notes = int(input("indiquez le nombre de notes\n"))
liste_notes = []
somme = 0
maxi = 0
mini = 20
for i in range(nb_notes):
    note = int(input("indiquez une note\n"))
    liste_notes.append(note)
    somme += note
moyenne = somme / nb_notes

for i in liste_notes:
    if i > maxi:
        maxi = i
    if i < mini:
        mini = i

print("la note maximale est:", max(liste_notes), "et la note minimale est:", min(liste_notes))
print("votre moyenne est de:", sum(liste_notes)/nb_notes)
print("la note maximale est:", maxi, "et la note minimale est:", mini)
print("votre moyenne est de:", moyenne)