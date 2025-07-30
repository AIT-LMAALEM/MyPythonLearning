#le programme echange les elements du triangle inférieur avec le triangle superieur de la matrice
A=[]
taille=int(input("entrer la taille de la matrice A:"))
print("veuillez saisir les elements de la matrice A:")
for i in range(taille):
    ligne=[]
    for j in range(taille):
        ligne.append(int(input(f"A[{i+1}][{j+1}]:")))
    A.append(ligne)
print("la matrice :")
for i in A:
    print(i)
#l'echange 
for i in range(taille):
    for j in range(taille):
       if i>j:
            A[i][j],A[j][i]=A[j][i],A[i][j]
print("échange....")
print("la nouvelle matrice :")
for i in A:
    print(i)
