from tkinter import *
from tkinter import messagebox

class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        self.title("Login")
        self.image_back =PhotoImage(file=r"C:\Users\PC\OneDrive\Pictures\Saved Pictures\hi2.png")
        self.lbl_back=Label(self,image=self.image_back,bd=0)
        self.lbl_back.place(x=0,y=0)
        self.title=Label(self,text="Login",font=("arial",15,"bold"))
        self.title.place(x=250,y=90)

        self.var_username=StringVar()
        self.ent_username=Entry(self,bg="white",fg="black",highlightthickness=1,highlightcolor="#00ffff",font=("arial",13),textvariable=self.var_username)
        self.ent_username.place(x=150,y=150,width=260,height=30)

        self.var_password=StringVar()
        self.ent_password=Entry(self,bg="white",fg="black",highlightthickness=1,highlightcolor="#00ffff",font=("arial",13),show="*",textvariable=self.var_password)
        self.ent_password.place(x=150,y=200,width=260,height=30)

        self.b_login=Button(self,text="Login",bg="#031616",fg="white",command=self.b_login_chek,bd=0,relief="flat",font=("arial",13,"bold"),activebackground="white",activeforeground="#031616")
        self.b_login.place(x=150,y=250,width=110,height=30)
        self.b_login.bind("<Enter>",self.b_login_enter)
        self.b_login.bind("<Leave>",self.b_login_leave)

        self.b_signup=Button(self,text="Signup",bg="#031616",fg="white",bd=0,relief="flat",font=("arial",13,"bold"),activebackground="white",activeforeground="#031616")
        self.b_signup.place(x=300,y=250,width=110,height=30)
        self.b_signup.bind("<Enter>",self.b_signup_enter)
        self.b_signup.bind("<Leave>",self.b_signup_leave)


    
    def b_login_chek(self):
        username=self.var_username.get()
        password=self.var_password.get()
        if username.lower()=="mhamed" and password=="mhamed1234":
            messagebox.showinfo("Login Successful",f"Welcome {username}")
        else:
            messagebox.showerror("Login Failed","Incorrect username or password")
        
    def b_login_enter(self,e):
        self.b_login.config(bg="#073535")
    def b_login_leave(self,e):
        self.b_login.config(bg="#031616")
    def b_signup_enter(self,e):
        self.b_signup.config(bg="#073535")
    def b_signup_leave(self,e):
        self.b_signup.config(bg="#031616")



    
    






a=App()

a.mainloop()
