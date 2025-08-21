from tkinter import *


root =Tk()
myLabel1=Label(root,text="hello world!")
myLabel1.grid(row=0,column=0)
myLabel2=Label(root,text="My name is mhamed").grid(row=0,column=1)

def Add():
    mylabel=Label(root,text="Look! I clicked Add!")
    mylabel.grid()

def Delete():
    mylabel=Label(root,text="Look! I clicked Delete")
    mylabel.grid()
def enter():
    mylabel=Label(root,text=f"hello {ent.get()}")
    mylabel.grid(row=3,column=1)


mybt1=Button(root,text="Add",padx=25,pady=10,command=Add).grid(row=1, column=0)
mybt2=Button(root,text="Delete",padx=25,pady=10,command=Delete).grid(row=2, column=0)

ent=Entry(root,font=(11),width=20)
ent.grid(row=3,column=0)
ent.insert(0,"username")
mybt3=Button(root,text="Enter",padx=25,pady=10,command=enter).grid(row=4, column=0)




root.mainloop()