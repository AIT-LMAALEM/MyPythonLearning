from tkinter import *

root=Tk()
root.title("Simple Calculator")
root.resizable(False,False)

e=Entry(root, width=44,borderwidth=4)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)


def b_click(number):
    e.insert(END,number)
    

def b_addf():
    
    number1=e.get()
    global num1
    num1 =int(number1)
    e.delete(0,END)

def b_clearf():
    e.delete(0,END)

def b_equalf():

    number2=e.get()
    num2=int(number2)
    e.delete(0,END)
    e.insert(0,num1+num2)

def b_multiplyf():
    pass
def b_subtractf():
    pass
def b_dividef():
    pass

    
    
b1=Button(root,text="1", padx=40, pady=20,command=lambda: b_click(1),bg="#2d2d2d",fg="#d8dfdf")
b2=Button(root,text="2", padx=40, pady=20,command=lambda: b_click(2),bg="#2d2d2d",fg="#d8dfdf")
b3=Button(root,text="3", padx=40, pady=20,command=lambda: b_click(3),bg="#2d2d2d",fg="#d8dfdf")
b4=Button(root,text="4", padx=40, pady=20,command=lambda: b_click(4),bg="#2d2d2d",fg="#d8dfdf")
b5=Button(root,text="5", padx=40, pady=20,command=lambda: b_click(5),bg="#2d2d2d",fg="#d8dfdf")
b6=Button(root,text="6", padx=40, pady=20,command=lambda: b_click(6),bg="#2d2d2d",fg="#d8dfdf")
b7=Button(root,text="7", padx=40, pady=20,command=lambda: b_click(7),bg="#2d2d2d",fg="#d8dfdf")
b8=Button(root,text="8", padx=40, pady=20,command=lambda: b_click(8),bg="#2d2d2d",fg="#d8dfdf")
b9=Button(root,text="9", padx=40, pady=20,command=lambda: b_click(9),bg="#2d2d2d",fg="#d8dfdf")
b0=Button(root,text="0", padx=40, pady=20,command=lambda: b_click(0),bg="#2d2d2d",fg="#d8dfdf")


b_clear=Button(root,text="Clear",padx=80,pady=30,command=b_clearf,bg="#2b7373",fg="#d8dfdf")
b_equal=Button(root,text="=",padx=40,pady=60,command=b_equalf,bg="#2b7373",fg="#d8dfdf")
b_add=Button(root,text="+",padx=40,pady=20,command=b_addf,bg="#864b2b",fg="#d8dfdf")
b_subtract=Button(root,text="-",padx=40,pady=20,command=b_subtractf,bg="#864b2b",fg="#d8dfdf")
b_multiply=Button(root,text="x",padx=40,pady=20,command=b_multiplyf,bg="#864b2b",fg="#d8dfdf")
b_divide=Button(root,text="/",padx=40,pady=20,command=b_dividef,bg="#864b2b",fg="#d8dfdf")

b1.grid(row=1,column=0)
b2.grid(row=1,column=1)
b3.grid(row=1,column=2)

b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)

b7.grid(row=3,column=0)
b8.grid(row=3,column=1)
b9.grid(row=3,column=2)

b0.grid(row=4,column=0)


b_clear.grid(row=6,column=1,columnspan=2)
b_equal.grid(row=5,column=0,rowspan=2)
b_add.grid(row=4,column=1)
b_subtract.grid(row=4,column=2)
b_multiply.grid(row=5,column=1)
b_divide.grid(row=5,column=2)





root.mainloop()