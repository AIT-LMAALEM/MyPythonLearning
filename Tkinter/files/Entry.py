from tkinter import *

win =Tk()
win.geometry("1024x720")
win.config(bg="gray")
n=1
def click():
    global n
    if n==1:
        ent2.config(show="")
        bt.config(text="hide")
        n=2
    else:
        ent2.config(show="*")
        bt.config(text="show")
        n=1

def enter1(e):
    bt.config(bg="#0F95EF")
def leave1(e):
    bt.config(bg="white")

def delete():
    ent2.delete(0,END)

var=StringVar()
def get1():
    x=var.get()
    print(x)


ent1= Entry(win,bg="white",fg="black",relief="flat",highlightthickness=1,highlightbackground="cyan",highlightcolor="green")
ent1.place(x=50,y=100,width=200,height=30)
ent2= Entry(win,bg="white",fg="black",relief="flat",show="*",selectbackground="red",selectforeground="green")
ent2.place(x=50,y=150,width=200,height=30)

bt=Button(win,text="show",bg="orange",fg="black",command=click)
bt.place(x=260,y=150)
bt.bind("<Enter>",enter1)
bt.bind("<Leave>",leave1)

bt2=Button(win,text="delete",bg="orange",fg="black",command=delete)
bt2.place(x=260,y=180)

bt3=Button(win,text="get",bg="orange",fg="black",command=get1)
bt3.place(x=260,y=210)


win.mainloop()