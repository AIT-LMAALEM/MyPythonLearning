from tkinter import *

root =Tk()
root.title("Toplevel")
root.config(bg="black")
root.geometry("600x400+300+100")
myLabel=Label(root,text="Window 1",font=(15)).pack()
def open2():
    top=Toplevel()
    top.geometry("600x400+300+100")
    Label(top,text="Window 2",font=(15)).pack()
    Button(top,text="Excit",command=top.quit).pack()

btn=Button(root,text="Open the seconde Window",command=open2,bg="white")
btn.pack()

root.mainloop()