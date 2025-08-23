from tkinter import *

root = Tk()


#Exemple 1

def update(value1):
    Label(root,text=f"Your language is {value1}" ).pack()

Label(root,text="choose your language").pack()

lang=StringVar(value="arabic")
r1=Radiobutton(root,text="arabic",variable=lang,value="arabic").pack()
r2=Radiobutton(root,text="french",variable=lang,value="french").pack()
r3=Radiobutton(root,text="english",variable=lang,value="english").pack()

Button(root,text="update",command=lambda:update(lang.get())).pack()


#Exemple 2

Label(root,text="choose an option!").pack()
MODES=[
    (1,"Pepperoni"),
    (2,"cheese"),
    (3,"Mushroom"),
    (4,"onion"),
]
def  click(choice):
    Label(root,text=f"your option is {choice}").pack()

pizza=StringVar(value="cheese")
for num,type in MODES:
    Radiobutton(root,text=num,value=type,variable=pizza).pack()

Button(root,text="Click",command=lambda:click(pizza.get())).pack()



root.mainloop()


