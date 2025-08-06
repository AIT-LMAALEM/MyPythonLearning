#programme qui detérmine si un mot est un hétérogramme ou non
# N.B:un hétérogramme est un mots dans laquelle lettre de l'alphabet n'apparaît plus d'une fois
mots=input("entrer un mots:")
E=set(mots)
for i in E:
    for j in E:
        if i!=j:
            print(mots," est un hétérogramme")
        else:
            print(mots," n'est pas un hétérogramme")
