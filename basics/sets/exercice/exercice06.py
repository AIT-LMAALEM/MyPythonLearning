#programme qui prend en entrée un ensemble de 4 équipes et afficher la liste complete des matchs possibles (aller et retour) entres ces équipes
équipes=set()
for  i in range(4):
    équipes.add(input(f"entrer l'équipe n {i+1}:"))
equipe_list=list(équipes)
for i in range(len(équipes)):
    for j in range(len(équipes)):
        if i!=j:
            print(f"[{equipe_list[i]},{equipe_list[j]}]")
