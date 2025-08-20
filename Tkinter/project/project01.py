from tkinter import *
from tkinter import messagebox

def b_login_enter(e):
    b_login.config(bg="#073535")
def b_login_leave(e):
    b_login.config(bg="#031616")

def b_signup_enter(e):
    b_signup.config(bg="#073535")
def b_signup_leave(e):
    b_signup.config(bg="#031616")

def b_login_chek():
    username= var_username.get()
    password=var_password.get()
    if username.lower() =="mhamed" and password=="mhamed1234":
        messagebox.showinfo("Login Successful",f"Welcome {username}")
    else:
        messagebox.showerror("Login Failed","Incorrect username or password")




win=Tk()
win.geometry("600x400")
win.resizable(False,False)
win.title("Login")
back_ground=PhotoImage(file=r"C:\Users\PC\OneDrive\Pictures\Saved Pictures\hi2.png")
lbl_back=Label(win,image=back_ground,bd=0)
lbl_back.place(x=0,y=0)

title=Label(win,text="Login",font=("arial",15,"bold"))
title.place(x=250,y=90)

var_username=StringVar()
var_password=StringVar()
ent_username=Entry(win,bg="white",fg="black",highlightthickness=1,highlightcolor="#00ffff",font=("arial",13),textvariable=var_username)
ent_username.place(x=150,y=150,width=260,height=30)

ent_password=Entry(win,bg="white",fg="black",highlightthickness=1,highlightcolor="#00ffff",font=("arial",13),show="*",textvariable=var_password)
ent_password.place(x=150,y=200,width=260,height=30)

b_login=Button(win,text="Login",bg="#031616",fg="white",bd=0,relief="flat",command=b_login_chek,font=("arial",13,"bold"),activebackground="white",activeforeground="#031616")
b_login.place(x=150,y=250,width=110,height=30)
b_login.bind("<Enter>",b_login_enter)
b_login.bind("<Leave>",b_login_leave)

b_signup=Button(win,text="Signup",bg="#031616",fg="white",bd=0,relief="flat",font=("arial",13,"bold"),activebackground="white",activeforeground="#031616")
b_signup.place(x=300,y=250,width=110,height=30)
b_signup.bind("<Enter>",b_signup_enter)
b_signup.bind("<Leave>",b_signup_leave)




win.mainloop()