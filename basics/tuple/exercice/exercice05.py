#programme qui vérifie si les deux tuples ont au moins un élément en commun ou non
tup1=(0,2,4,6,8,10)
tup2=(0,1,3,5,7,9)
n=int(input("entrer un nombre entre 0 et 10:"))
if n in tup1 and tup2:
    print(n," existe dans tup1 et tup2")
else:
    print(n," n'existe pas dans tup1 et tup2")
print(tup1)
    