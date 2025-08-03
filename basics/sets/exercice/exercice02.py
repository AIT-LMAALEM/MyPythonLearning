#méthodes et fonctions
#ajout
  # add()
E={"mhamed","imrane","rachid",True,5}
E.add("maroc")
print(E)
E.add(False)
print(E)

  # update()
E.update([2000,12,"helloe"])
E.update(("fst","ensam"))
E.update({'A','B','C'})
print(E)

#suppression
  #remove()
E.remove("fst")
E.remove("A")
E.remove("imrane")
print(E)

  #discard():la même comme remove ,la seul difference est que cette methoden'affiche pas d'erreur si l'element n'existe pas dans l'ensemble
E.discard(10000)
print(E)
 
  # pop():permet de supprimer un elements aleatoire de l'ensemble et de le retourner comme valeur de retour
x=E.pop()
print(x)

  #clear();permet de supprimer tout les elements de l'ensemble
E.clear()
E.add('hello')
print(E)


#operations
#len(),sum(),max(),min()
print(len(E))


#duplication

 #copy()
r={1,2,3,4}
t=r.copy()
r.add(7)
print(r)
print(t)
