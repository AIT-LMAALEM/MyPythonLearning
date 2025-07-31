#la ligne d'une matrice dont la somme de ses element est la plus grande
ligneA=int(input("entrer le nombres de lignes:"))
colonneA=int(input("entrer le nombres de colonnes:"))
A=[]
print("veuillez saisir les elements de la matrice A:")
for i in range(ligneA):
    ligne=[]
    for j in range(colonneA):
        ligne.append(int(input(f"A[{i+1}][{j+1}]:")))
    A.append(ligne)
sum_ligne=[]
for ligne in A:
    sum_ligne.append(sum(ligne))
print("la ligne dont la somme est le plus grande est:",A[sum_ligne.index(max(sum_ligne))])
