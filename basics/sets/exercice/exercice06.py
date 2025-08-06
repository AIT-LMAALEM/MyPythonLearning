#programme qui prend en entrée un ensemble de 4 équipes et afficher la liste complete des matchs possibles (aller et retour) entres ces équipes
# équipes=set()
# for  i in range(4):
#     équipes.add(input(f"entrer l'équipe n {i+1}:"))
# equipe_list=list(équipes)
# for i in range(len(équipes)):
#     for j in range(len(équipes)):
#         if i!=j:
#             print(f"[{equipe_list[i]},{equipe_list[j]}]")



#programme qui affiche toutes les paires d'élements dans un ensemble dont la somme est égale à une valeure donner
E=set()
for i in range(5):
    E.add(int(input(f"entrer le nombre {i+1}:")))
x=int(input("entrer un nombre qui n'existe pas dans E:"))
elements=[]
for element in E:
    for a_element in E:
        if element +a_element==x:
            elements.append([element,a_element])
print("les paires dont la somme est égale a",x,"est :")
for i in elements:
    print(i)


