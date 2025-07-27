nombres=[]
for i in range(10):
    print("entrer l'element ",i+1," de la liste:",end=" ")
    nombres.append(int(input()))

#le min et le max dans une liste
print("le minimum de la liste:",min(nombres))
print("le maximum de la liste :",max(nombres))


# le deuxieme plus grand element de la liste
#methode1
x=max(nombres)
nombres.remove(max(nombres))
print("2éme plus grande element est:",max(nombres))
nombres.append(x)
print(nombres)

#methode~2
nombres.sort(reverse=True)  # tri par order decroissant
print(nombres[1])


#les nombre pair de la liste
npair=[]
for i in nombres:
    if i%2==0:
        npair.append(i)
print(npair)



#vérifier l'existence du nombre n dans la liste 
n=int(input("entrer la valeur de n:"))
if n in nombres:
    print("le nombre ",n,"existe dans la liste")
else:
    print("le nombre ",n,"n'existe pas dans la liste")



#determine et afficher les éléments uniques de la liste
unique=[]
for i in range(10):
    if nombres.count(nombres[i])==1:
        unique.append(nombres[i])
print(unique)





        


