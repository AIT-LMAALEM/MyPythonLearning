#determinant d'une matrice d'ordre 2
A=[]
for i in range(2):
    ligne=[]
    for j in range(2):
        ligne.append(int(input(f"entrer A[{i+1}][{j+1}]:")))
    A.append(ligne)
det=(A[0][0]*A[1][1])-(A[1][0]*A[0][1])
print("la matrice A:")
for i in A:
    print(i)
print("le determinant de A:",det)