from tkinter import *

root=Tk()
root.geometry("500x400")
root.title("Switcher")
root.resizable(False,False)
#Create Frame
option_frame=Frame(root,bg="#adabaa")
option_frame.pack(side=LEFT)
option_frame.pack_propagate(False)
option_frame.configure(width=120,height=400)

# main frame
main_frame=Frame(root,highlightbackground="black",highlightthickness=1,)
main_frame.pack(side=LEFT)
main_frame.pack_propagate(False)
main_frame.configure(width=380,height=400)

#functions

def home_page():
    deletes_pages()
    home_frame=Frame(main_frame)
    home_frame.pack(pady=15)
    home_label=Label(home_frame,text="Home Page \n\nPage: 1", font=("Bold",20))
    home_label.pack()

def menu_page():
    deletes_pages()
    menu_frame=Frame(main_frame)
    menu_frame.pack(pady=15)
    menu_label=Label(menu_frame,text="Menu Page \n\nPage: 2", font=("Bold",20))
    menu_label.pack()

def contact_page():
    deletes_pages()
    contact_frame=Frame(main_frame)
    contact_frame.pack(pady=15)
    contact_label=Label(contact_frame,text="Contact Page \n\nPage: 3", font=("Bold",20))
    contact_label.pack()

def about_page():
    deletes_pages()
    about_frame=Frame(main_frame)
    about_frame.pack(pady=15)
    about_label=Label(about_frame,text="About Page \n\nPage: 4", font=("Bold",20))
    about_label.pack()

def deletes_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()

def hide_indicators():
    home_indicate.config(bg="#adabaa")
    menu_indicate.config(bg="#adabaa")
    contact_indicate.config(bg="#adabaa")
    about_indicate.config(bg="#adabaa")

def indicate(lbl,page):
    hide_indicators()
    lbl.config(bg="#f3370d")
    page()

# buttons
home_bt=Button(option_frame,text="Home",font=("Bold",14),fg="#f3370d",bd=0,relief="flat",bg="#adabaa",command=lambda:indicate(home_indicate,home_page))
home_bt.place(x=25,y=50)
home_indicate=Label(option_frame,text='',bg="#adabaa")
home_indicate.place(x=1,y=50,width=4,height=45)

menu_bt=Button(option_frame,text="Menu",font=("Bold",14),fg="#f3370d",bd=0,relief="flat",bg="#adabaa",command=lambda:indicate(menu_indicate,menu_page))
menu_bt.place(x=25,y=100)
menu_indicate=Label(option_frame,text='',bg="#adabaa")
menu_indicate.place(x=1,y=100,width=4,height=45)

contact_bt=Button(option_frame,text="Contact",font=("Bold",14),fg="#f3370d",bd=0,relief="flat",bg="#adabaa",command=lambda:indicate(contact_indicate,contact_page))
contact_bt.place(x=25,y=150)
contact_indicate=Label(option_frame,text='',bg="#adabaa")
contact_indicate.place(x=1,y=150,width=4,height=45)

about_bt=Button(option_frame,text="About",font=("Bold",14),fg="#f3370d",bd=0,relief="flat",bg="#adabaa",command=lambda:indicate(about_indicate,about_page))
about_bt.place(x=25,y=200)
about_indicate=Label(option_frame,text='',bg="#adabaa")
about_indicate.place(x=1,y=200,width=4,height=45)




root.mainloop()