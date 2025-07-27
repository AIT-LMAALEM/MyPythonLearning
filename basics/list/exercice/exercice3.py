# matrice
#programme qui permet de déclarer une liste de deux dimensions(3,6),puis il remplit la liste avec des 0
matrice=[]
for i in range(3):
    ligne=[]
    for j in range(6):
        ligne.append(0)
    matrice.append(ligne)
#pour chaque valeur de i ona une liste ligne qui est vide puis pour chaque valeur de j ligne reçoit des 0
print("la matrice est:")
print(f"{matrice[0]}\n{matrice[1]}\n{matrice[2]}")