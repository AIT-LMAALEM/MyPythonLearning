from tkinter import *
from tkinter import messagebox

win=Tk()
win.title("messege Boxes")
def click():
    messagebox.showinfo("messege box","Hello World!")
Button(win,text="Click",command=click).pack()

def click2():
    messagebox.showerror("messege box","Error!")
Button(win,text="Click2",command=click2).pack()

def click3():
    messagebox.showwarning("messege box","Warning!")
Button(win,text="Click3",command=click3).pack()

def click4():
    respense= messagebox.askquestion("messege box","Are you Boy or Girl?")
    
Button(win,text="Click4",command=click4).pack()

def click5():
    respense=messagebox.askyesno("messege box","Are you boy?")
    if respense==1:
        Label(win,text="you choose Ok").pack()
        
    else:
        Label(win,text="you choose No!").pack()
        
Button(win,text="Click5",command=click5).pack()

def click6():
    respense=messagebox.askokcancel("messege box","do you want to eat?")
Button(win,text="Click6",command=click6).pack()




win.mainloop()