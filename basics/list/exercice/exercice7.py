#programme qui calcule la somme de la diagonale principale d'une matrice
A=[]
taille=int(input("entrer la taille de la matrice A:"))
print("veuillez saisir les elements de la matrice A:")
for i in range(taille):
    ligne=[]
    for j in range(taille):
        ligne.append(int(input(f"A[{i+1}][{j+1}]:")))
    A.append(ligne)
#afficher la matrice A
print("la matrice A:")
for i in A:
    print(i)
#calcule la somme des element de la diagonale
sum=0
for i in range(taille):
    for j in range(taille):
        if i ==j:
          sum+=A[i][i]
print("la somme de la diagonale principale:",sum)