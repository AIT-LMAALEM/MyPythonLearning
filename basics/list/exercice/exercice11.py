#programme qui affiche la matrice identité 
taille=int(input("entrer la taille de la matrice:"))
ide=[]
for i in range(taille):
    ligne=[]
    for j in range(taille):
        if i==j:
            ligne.append(1)
        else:
            ligne.append(0)
    ide.append(ligne)
print("la matrice identité de taille ",taille,"est:")
for lignes in ide:
    print(lignes)

