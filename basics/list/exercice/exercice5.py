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
somme=[]
for i,j in zip(A,B):
    ligne=[]
    for k,t in zip(i,j):
        ligne.append(k+t)
    somme.append(ligne)

