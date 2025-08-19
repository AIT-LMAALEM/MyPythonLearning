from tkinter import *
win=Tk()
win.geometry("516x520")
win.resizable(False,False)
win.config(bg="black")
def click():
    win2=Tk()
    win2.geometry("600x600")
    lbl=Label(win2,text="user name")
    lbl.place(x=100,y=200)

def enter(e):
    bt1.config(bg="#7999AE")
def leave(e):
    bt1.config(bg="white")

bt1=Button(win,text="login",bg="white",fg="black",font=("arial",12,"bold"),activebackground="black",activeforeground="white",relief="flat",bd=0,command=click)
bt1.place(x=200,y=200,width=100,height=50)
bt1.bind("<Enter>",enter)
bt1.bind("<Leave>",leave)







win.mainloop()