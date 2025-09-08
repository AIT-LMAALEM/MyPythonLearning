# Assigner des valeurs à nd.array
import numpy as np

vecteur= np.array([1,2,3])
print(vecteur)
vecteur[-1]=4
print(vecteur)

vecteur=np.array([1,2,3,4,5,6,7,8,9,10])
print(vecteur)
for i in range(10):
    vecteur[i]=10-i
print(vecteur)

matrice = np.array([[1,2,3],[1,2,3],[1,2,3]])
matrice[1,0] = 4
matrice[1,1] = 5
matrice[1,2] = 6
print(matrice)

matrice= np.array([[1,2],[3,1]])
for i in range(2):
    for j in range(2):
        if matrice[i][j] !=1:
             matrice[i][j]=0

print(matrice)

matrice[0] = np.array([2,2])
matrice[1] = np.array([3,3])
print(matrice)

matrice[1] = [4,4]
matrice[0] = [1,1]
print(matrice)

matrice2= np.array([[1,4,6],[4,2,3],[8,7,9],[1,3,5]])
matrice2[-1]= 0
matrice2[0]= 4
print(matrice2)

