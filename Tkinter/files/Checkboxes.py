from tkinter import *

root= Tk()
root.title("CheckBoxe")
root.config(bg="black")

var1=StringVar()
var2=StringVar()
var3=StringVar()
def check():
    Label(root,text=f" {var1.get()} {var2.get()} {var3.get()}").pack()

check1=Checkbutton(
                   root,
                   text="Python",
                   variable=var1,
                   bg="black",fg="white",
                   onvalue="Python",offvalue="",
                   activebackground="black",activeforeground="white",
                   selectcolor="gray"
                   ).pack()
check2=Checkbutton(
                   root,
                   text="Java",
                   variable=var2,
                   bg="black",fg="white",
                   onvalue="Java",offvalue="",
                   activebackground="black",activeforeground="white",
                   selectcolor="gray"
                   ).pack()
check3=Checkbutton(
                   root,
                   text="C++",
                   variable=var3,
                   bg="black",fg="white",
                   onvalue="C++",offvalue="",
                   activebackground="black",activeforeground="white",
                   selectcolor="gray"
                   ).pack()
Button(root,text="Show Selection ",command=check).pack()

# check1.select()
# check1.deselect()





root.mainloop()