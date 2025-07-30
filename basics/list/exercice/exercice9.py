#programme qui affiche le min et le max de chaque ligne et colonne
ligneA=int(input("entrer le nombres de lignes:"))
colonneA=int(input("entrer le nombres de colonnes:"))
A=[]
print("veuillez saisir les elements de la matrice A:")
for i in range(ligneA):
    ligne=[]
    for j in range(colonneA):
        ligne.append(int(input(f"A[{i+1}][{j+1}]:")))
    A.append(ligne)
print("la matrice A:")
for i in A:
    print(i)
for i,ligne in enumerate(A,start=1):
    print(f"min(ligne[{i}])={min(ligne)}")
    print(f"max(line[{i}])={max(ligne)}\n")
# pour trouver le min et le max de chaque colonne en peut faire la transposée de A puis en calcule le min et le max
B=[]
for i in range(colonneA):
    ligne=[]
    for j in range(ligneA):
        ligne.append(A[j][i])
    B.append(ligne)
for i,colonne in enumerate(B,start=1):
    print(f"min(colonne[{i}])={min(colonne)}")
    print(f"max(colonne[{i}])={max(colonne)}\n")



