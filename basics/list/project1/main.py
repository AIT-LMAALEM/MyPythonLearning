tic=[["-","-","-"],["-","-","-"],["-","-","-"]]
num=[[1,2,3],[4,5,6],[7,8,9]]
def graph():
    for i in range(3):
         print("-----------------")
         for j in range(3):
             print("|",tic[i][j],"|",end=" ")
         print("       ",end=" ")
         for j in range(3):
             print("|",num[i][j],"|",end=" ")
         print()

def x():
    global tic
    print("c'est le tour de joueur X")
    n=int(input("veuillez sélectionner un espace vide sur la grille entre 1 et 9:"))
    ligne=(n-1)//3
    colonne=(n-1)%3
    tic[ligne][colonne]=choix
    graph()

def o():
    global tic
    print("c'est le tour de joueur O")
    n=int(input("veuillez sélectionner un espace vide sur la grille entre 1 et 9:"))
    ligne=(n-1)//3
    colonne=(n-1)%3
    tic.remove(tic[ligne][colonne])
    tic[ligne][colonne]=choix
    graph()


players=["X","O"]
turn=0
choix=input("veuillez choisir soit une croix(X), soit un round(O):").upper()
print("vous avez choisi :",choix)




