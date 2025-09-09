import numpy as np 
import os
# Multiplication Table


def clear_screen():
    os.system("cls" if os.name=="nt" else "clear")

while True:
    
    num =int(input("enter a number :"))
    clear_screen()
    ligne = np.arange(1,num+1)[None,:]
    colonne= np.arange(1,num+1)[:,None]

    print(f" Multiplication Table:\n {ligne * colonne}")
   