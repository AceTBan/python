valeur1 = 1
prenom = "Florent"


print(prenom)
print(valeur1)


#### EXO 1 #######

prenom= input("Quel est votre prénom? \n")
nom= input("quel est votre nom? \n")
date= int(input("Quel est votre année de naissance? \n"))
print("Bonjour", prenom, nom, "vous avez", 2021-date,"ans")

var1 = int(input("donne un nombre \n"))
var1 += int(input("un autre stp \n"))
var1 += int(input("encore un ! \n"))
print ("Abracadabra j'additionne et ça donne ce résultat:", var1)

var2 = int(input("donne un nombre \n"))
print ("Voila le résultat puissance 3!", var2**3)

#### Exo2 #####

var3= int(input("Donne un nombre \n"))
var4= bin(var3)
var5= hex(var3)
print("valeur en binaire", var4, "et la valeur en Hexadecimal", var5)

print("Pour ce qui est des String on a :")
print(dir("Chaine de caractères"))
print("Pour ce qui est des Integer on a :")
print(dir(5))

var6= input("Ecrit moi une histoire! \n")
print(len(var6))

a= int(input("1er nombre \n"))
b= int(input("2ème nombre \n"))
c= int(input("3ème nombre \n"))
d= int(input("4ème nombre \n"))
print("valeur min" ,min(a,b,c,d), "valeur max", max(a,b,c,d))

