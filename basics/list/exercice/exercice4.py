#programme qui lit une matrice A dim(4,6) puis il affiche A et la transpoée de A
matrice=[]
for i in range(3):
    ligne=[]
    for k in range(3):
        element=int(input(f"entrer A[{i+1}][{k+1}]:"))
        ligne.append(element)
    matrice.append(ligne)
print("la matrice A:")
for i in range(3):
    print(f"{matrice[i]}")

tran=[]
for k in range(3):
    ligne=[]
    for i in range(3):
        ligne.append(matrice[i][k])
    tran.append(ligne)

print("la transposée de A")
for i in range(3):
    print(f"{tran[i]}")

        