#produit matricielle
#condition il faut que le nombres de colonnes de la matrice A doit étre egale au nombres de lignes de la matrice B
A=[]
ligneA=int(input("entrer le nombres de ligne de A:"))
colonneA=int(input("entrer le nombres de colonnes de A:"))
print("veuillez saisir les elements de la matrice A:")
for i in range(ligneA):
    ligne=[]
    for j in range(colonneA):
        ligne.append(int(input(f"A[{i+1}][{j+1}]:")))
    A.append(ligne)
B=[]
ligneB=int(input("entrer le nombres de ligne de B:"))
colonneB=int(input("entrer le nombres de colonnes de B:"))
print("veuillez saisir les elements de la matrice A:")
for i in range(ligneB):
    ligne1=[]
    for j in range(colonneB):
        ligne1.append(int(input(f"B[{i+1}][{j+1}]:")))
    B.append(ligne1)
print("la matrice A:")
for i in A:
    print(i)
print("la matrice B:")
for j in B:
    print(j)
if colonneA!=ligneB:
    print("Le produit matriciel est impossible!")
else:
    C=[]
    for i in range(ligneA):
        ligne=[]
        for j in range(colonneB):
            sum=0
            for k in range(colonneA): #ou ligne B
                sum+=A[i][k]*B[k][j]
            ligne.append(sum)
        C.append(ligne)
    print("le produit A*B")
    for i in C:
        print(i)
