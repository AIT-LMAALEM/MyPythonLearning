#la somme de deux matrices
print("*** programme qui lit deux matrices A et B  carée pui effectue l'addition ***")
ligne1=int(input("entrer le nombres de lignes:"))
colonne1=int(input("entrer le nombres de colonnes:"))
A=[]
B=[]
print("veuillez saisir les elements de la matrice A:")
for i in range(ligne1):
    ligne=[]
    for j in range(colonne1):
        ligne.append(int(input(f"A[{i+1}][{j+1}]:")))
    A.append(ligne)
print("veuillez saisir les elements de la matrice B:")
for i in range(ligne1):
    ligne=[]
    for j in range(colonne1):
        ligne.append(int(input(f"B[{i+1}][{j+1}]:")))
    B.append(ligne)
#list C=A+B
C=[]
for i in range(ligne1):
    ligne=[]
    for j in range(colonne1):
        ligne.append(A[i][j]+B[i][j])
    C.append(ligne)

print("la matrice A:")
for i in A:
    print(f"{i}")
print("la matrice B:")
for i in B:
    print(f"{i}")
print("la matrice A+B :")
for i in C:
    print(f"{i}")

#methode ~2
#en peut utiliser la fonction zip pour calculer la somme de deux matrice
# # Deux matrices d'exemple
# matrix_a = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]

# matrix_b = [
#     [7, 8, 9],
#     [10, 11, 12]
# ]

# # Résultat vide
# result = []

# # Parcourir les lignes
# for row_a, row_b in zip(matrix_a, matrix_b):
#     # Nouvelle ligne vide
#     new_row = []
#     # Parcourir les éléments de chaque ligne
#     for elem_a, elem_b in zip(row_a, row_b):
#         new_elem = elem_a + elem_b
#         new_row.append(new_elem)
#     # Ajouter la ligne calculée au résultat
#     result.append(new_row)

# # Affichage du résultat
# for row in result:
#     print(row)
