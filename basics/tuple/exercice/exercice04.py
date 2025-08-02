#un tuple imbriquée est un tuple qui a un autre tuple comme élément
#création
math=(("anwar","moha","samir","inas",("ait imran","samiri","rawan")),(13,15,11,10))
print(math[0])
print(math[0][0])
print(math[0][-1])
print(math[1])
print(math[1][-1])
print(math[0][4][0])

# tuple a 2D
amis=(("mhamed","anouar","ismaail","rayan"),(13,24,12,18))
for ligne in amis:
    for colonne in ligne:
        print(colonne)
