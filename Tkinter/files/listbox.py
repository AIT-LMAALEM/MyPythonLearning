#listbox
from tkinter import *

win= Tk()
win.geometry("800x800")
list1=Listbox(win,relief="flat",bd=0,font=("arial",13),selectmode="multiple")
list1.place(x=10,y=10,width=300,height=200)

var=StringVar()
ent1=Entry(win,fg="black",textvariable=var,font=("arial",13))
ent1.place(x=10,y=230,width=300,height=30)

def bt_add():
    x=var.get()
    var.set("")        #ent1.delete(0,END)
    list1.insert(END,x)

# def bt_get():
#     num=list1.size()
#     for i in range(num):
#         print(list1.get(i))

def bt_select():
    value=list1.curselection()
    index=value[0]
    print(list1.get(index))

def bt_delete():
    value=list1.curselection()
    index=value[0]
    list1.delete(index)


bt1=Button(win,text="add",bg="orange",fg="white",font=("arial",13,"bold"),command=bt_add)
bt1.place(x=320,y=230,width=55,height=30)

bt2=Button(win,text="get",bg="orange",fg="white",font=("arial",13,"bold"),command=bt_select)
bt2.place(x=320,y=260,width=55,height=30)

bt3=Button(win,text="delete",bg="orange",fg="white",font=("arial",13,"bold"),command=bt_delete)
bt3.place(x=320,y=290,width=55,height=30)
win.mainloop()