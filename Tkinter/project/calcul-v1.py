from tkinter import *

root=Tk()
root.title("Simple Calculator")
root.resizable(False,False)

e=Entry(root, width=44,borderwidth=4)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)


def b_click(number):
    e.insert(END,number)
    

def b_addf():
    e.insert(END,"+")
    # number1=e.get()
    # global num1
    # num1 =int(number1)
    # e.delete(0,END)

def b_clearf():
    e.delete(0,END)

def b_equalf():
    
    oper=e.get()
    num=oper.split("+")
    e.delete(0,END)
    sum=0
    for i in range(len(num)):
        sum+=int(num[i])
    e.insert(0,sum)
    #METHOD 1
    # number2=e.get()
    # num2=int(number2)
    # e.delete(0,END)
    # e.insert(0,num1+num2)

    
    
b1=Button(root,text="1", padx=40, pady=20,command=lambda: b_click(1))
b2=Button(root,text="2", padx=40, pady=20,command=lambda: b_click(2))
b3=Button(root,text="3", padx=40, pady=20,command=lambda: b_click(3))
b4=Button(root,text="4", padx=40, pady=20,command=lambda: b_click(4))
b5=Button(root,text="5", padx=40, pady=20,command=lambda: b_click(5))
b6=Button(root,text="6", padx=40, pady=20,command=lambda: b_click(6))
b7=Button(root,text="7", padx=40, pady=20,command=lambda: b_click(7))
b8=Button(root,text="8", padx=40, pady=20,command=lambda: b_click(8))
b9=Button(root,text="9", padx=40, pady=20,command=lambda: b_click(9))
b0=Button(root,text="0", padx=40, pady=20,command=lambda: b_click(0))

b_add=Button(root,text="+",padx=40,pady=20,command=b_addf)
b_clear=Button(root,text="Clear",padx=78,pady=20,command=b_clearf)
b_equal=Button(root,text="=",padx=87,pady=20,command=b_equalf)

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

b_add.grid(row=5,column=0)
b_clear.grid(row=4,column=1,columnspan=2)
b_equal.grid(row=5,column=1,columnspan=2)





root.mainloop()