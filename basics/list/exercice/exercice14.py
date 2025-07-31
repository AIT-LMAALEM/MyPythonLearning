#programme qui affiche les éléments nobles d'une liste 
#un x est dit noble dans une liste si le nombre d'element supérieurs à x est égale à x
list1=[]
n=int(input("la taille de la list:"))
for i in range(n):
    list1.append(int(input(f"entrer l'élement {i+1}:")))
print(list1)

for i in range(len(list1)):
    x=0
    for j in range(len(list1)):
        if list1[j]>list1[i]:
            x+=1
    if list1[i]==x:
        print(list1[i]," est noble")
        