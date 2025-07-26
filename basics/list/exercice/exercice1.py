#programme qui demende à l'utilisateur de saisir 10 réel stockés dans une liste puis le programme calcule et affiche 
#la somme,le produit et la moyenne des éléments de la liste

nombres=[]
for i in range(10):
    print("entrer l'element ",i+1," de la liste:")
    nombres.append(float(input()))
p=1
for i in nombres:
    p*=i

print("la somme des elements de la liste :",sum(nombres))
print("la moyenne des elements de la liste :",sum(nombres)/len(nombres))
print("le produit des element de la liste",p)
