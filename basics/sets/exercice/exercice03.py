#operation sur les ensembles

#Union :U: reprsente tous les elements contenus ou stockes dans les ensembles.le double ne seront inclus qu'une seul fois
# synthaxe 1: union()
#synthaxe 2: |
# E1 |=E2  
F={1,3,5,7,9}
E={0,2,4,6,8,10}
# print(F|E)
# print(F.union(E))
# F|=E
# print(F)


#intersection: represente tous les elements appartenant a la fois aux deux ensembles
# methode : intersection()  E=E1.intersection(E2,E3,E4...)
# operateur: &  E=E1 & E2 & E3 & ...
# E1 &=E2
R={"ahmed","ali",16,17,1,False}
S={"ali","hicham",5,17,0}
# print(S&R)
# print(S.intersection(R))
# R&=S 
# print(R)




#Difference:A\B represente les elements appartenat a un ensemble (gauche) qui n'appartiennent pas à un un autre (droit)
# differnece()   E=E1.difference(E2)
# -
#E1-=E2
e={1,4,3,6,8,9}
f={1,6,98,11,10,111}
# print(e-f)
# print(e.difference(f))
# print(f.difference(e))
# print(f-e)
# print(R-S)
# print(S-R)


# difference symetrique: represente les elements appartenant a l'un des deux ensembles, mais pas aux deux a la fois
# E=E1.symmetric_difference(E2)
#E1^=E2
# print(e^f)
# print(f^e)
# print(e.symmetric_difference(f))
# print(f.symmetric_difference(e))



# sous-ensemble: inclusion large B est sous ense de A si tout les elements de B sont aussi des elements de A, Best inclus dans A
# methode: issubset()   return : true ou false
# ope: <= 
# sous- ensemble propre: si tout les elements de B sont aussi des elements de A, mais A contient au moins un element qui n'est pas en B
# ope:<
a={1,2,3,4,5,6,7,8,9}
b={1,2,3,4,5,6}
if b<=a:
    print("b inclue dans a")
else:
    print("b n'est pas inclue dans a")











