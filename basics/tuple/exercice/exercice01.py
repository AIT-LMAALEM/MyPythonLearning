# le tuple est une séquence de données ordonnées (,) ,de 0 à n-1
# la taille d'une tuple ne peut pas être modifier une fois qu'il est créé(a une taille fixe)
# ne nous pouvons pas ajouter,modifier ou supprimer des éléments d'un tuple après sa création
# un tuple peut contenir différent types d'éléments(string,booléen,int,float,..)
# le tuple peut contenir des doublons

#création
amis=("adel","yassine","samia","samir")
tupleA=(10,20,True,30,False,2.23,"hello",5+10)
tupleB="maroc","egypt","algerie","souria"
tupleC=tuple((1,2,3,4,5))
tupleD=tuple("mohamade") #=>('m','o','h','a','m','a','d','e')


#créer un tuple contenant les nombre de 5 à 100
nombre=tuple(range(5,101))
nombre_pair=tuple(range(0,100,2))
print(nombre_pair)

# affichage d'un élèment
math=("analyse","algebre","probabilité","geometrie","statistique")
print(math[0])
print(math[-1])

n=int(input("entrer un nombre entier non null:"))
print(tuple(range(1,n+1)))
print(tuple(range(0,n+1,2)))
print(tuple(range(1,n+1,2)))


















