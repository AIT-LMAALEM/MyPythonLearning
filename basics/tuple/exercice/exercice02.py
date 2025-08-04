#opération sur les tuples
t1=(1,2,3,4)
t2=(5,6,7,8)
print(t1+t2)
print(t1 +2*t2)
t1*=4  #multipier t1 4 fois
print(t1)
#comparer deux tuples :== != <= >= < >
#pour que duex tuples soient identiques il faut qu'l aient la même taille et contiennent deux a deux des élement égales
t1=(4,5,8,1)
t2=(0,5,3,6,1,6,2,0)
print(t2<=t1) #=>True   4>0

#affictation multiple 
t=("samir",18,"rabat")
nom,age,ville=t
print(age)


#methode et fonction
#création   tuple()
n=tuple(("hello","bonjour","salut"))
print(n)

# len(): donne le nombre d'element dans un tuple
print(len(n))

# sum(): la somme des elements dans un tuple
nombre=tuple(range(100))
print(sum(nombre))


# max() ,min()
# count(): methode permet de déterminer combien de fois l'élément apparaît dans le tuple
m=(1,1,3,2,3,3,3,5,3,5,-6)
print(m.count(3))



#methode index() nomtuple.index(element,debut,fin)
# debut par defaut est 0
# fin : par defaut la fin du tuple
lettre=tuple("abcdefgh")
print(lettre.index('c'))
print(lettre.index('h',2))
print(lettre.index('y'))

















































