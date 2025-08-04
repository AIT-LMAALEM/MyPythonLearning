#programme qui supprime tous les nombres entiers d'un ensemble
K={11 , 1.5 , 4 , 3.14 , 16 , 1.42}
for i in list(K):
    if type(i)==int:
        K.remove(i)
print(K)