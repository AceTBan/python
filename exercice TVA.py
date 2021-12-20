nb = int(input("indiquez le nombre d'article à scanner\n"))
i = 1
HT = 0
TVA = 0.2
#
# while i <= nb:
#     print("Indiquez le prix de l'article numero", i)
#     HT += int(input())
#     i += 1

for j in range(1, nb+1):
    print("Indiquez le prix de l'article numero", j)
    HT += int(input())

print("Votre total TTC est de", HT*(1+TVA), "€")