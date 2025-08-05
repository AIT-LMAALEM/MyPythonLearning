#programme qui supprime tous les nombres entiers d'un ensemble
# K={11 , 1.5 , 4 , 3.14 , 16 , 1.42}
# for i in list(K):
#     if type(i)==int:
#         K.remove(i)
# print(K)

#programme qui compte le nombre de voyelles dans un texte
voyelles={"a","e","i","o","u","y"}
texte=input("entrer un texte:").lower()
count=0
for x in texte:
    if x in voyelles:
        count+=1
print("le nombre de voyelles dans le texte est:",count)

