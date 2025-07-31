#matrice creuse : si le nombre de zéros est plus grand que la moitié de ses éléments
taille=int(input("entrer la taille de la matrice:"))
A=[]
for i in range(taille):
    ligne=[]
    for j in range(taille):
        ligne.append(int(input(f"A[{i+1}][{j+1}]:")))
    A.append(ligne)
#on vérifier le nombre d'élément non null ou ligne
x=0
for ligne in A:
    for colonne in ligne:
        if colonne==0:
            x+=1
if x>(taille*taille)//2:
    print("la matrice est creuse")
else:
    print("la matrice n'est pas creuse")

