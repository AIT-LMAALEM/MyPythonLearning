from tkinter import *
import sqlite3

root=Tk()
root.title("GUI With Database")
root.geometry("600x600")
root.resizable(False,False)


#Create functions
def clear():
    #Clear the Text Boxes
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)


def submit():
    db=sqlite3.connect("addressApp.db")
    cr=db.cursor()
    cr.execute("INSERT INTO addresses(first_name, last_name, address, city, state, zipcode) VALUES (?, ?, ?, ?, ?, ?)",
           (f_name.get(), l_name.get(), address.get(), city.get(), state.get(), zipcode.get()))


    db.commit()
    db.close()
    clear()

def query():
    db=sqlite3.connect("addressApp.db")
    cr=db.cursor()
    
    cr.execute("SELECT * FROM addresses")
    results=cr.fetchall()
    print(results)

    db.commit()
    db.close()

def delete():
    
    db=sqlite3.connect("addressApp.db")
    cr=db.cursor()
    cr.execute(f"DELETE FROM addresses WHERE zipcode='{ask_zipcode.get()}'")
    for i in [ask,ask_zipcode,delete_bt]:
        i.destroy()
    
    
    db.commit()
    db.close()

def widget_delete():
    global ask_zipcode,ask,delete_bt
    ask=Label(root,text="Enter Zipcode")
    ask.grid(row=9,column=0,padx=10)
    ask_zipcode=Entry(root,width=35)
    ask_zipcode.grid(row=9,column=1,padx=10)
    delete_bt=Button(root,text="Delete",command=delete)
    delete_bt.grid(row=9,column=2)


def Enter():
    db=sqlite3.connect("addressApp.db")
    cr=db.cursor()
    
    cr.execute(f"SELECT * FROM addresses Where zipcode='{ask_zipcode.get()}'")
    option=Label(root,text="What do you Want To Update:")
    option.grid(row=12,column=0)
    option_Entry=Entry(root,width=35)
    option_Entry.grid(row=12,column=1,padx=10,pady=10)
    option_label=Label(root,text=f"{option_Entry}")
    option_label.grid(row=13,column=0)
    option_update=Entry(root,width=35)
    option_update.grid(row=13,column=1,padx=10,pady=10)
    cr.execute(f"UPDATE addresses SET '{option_Entry}'='{option_update}'")
    
    
    

    db.commit()
    db.close()



def update():
    ask=Label(root,text="Enter Your Zipcode To Update")
    ask.grid(row=11,column=0,padx=10)
    ask_zipcode=Entry(root,width=35)
    ask_zipcode.grid(row=11,column=1,padx=10)
    enter_btn=Button(root,text="Enter",command=Enter)
    enter_btn.grid(row=11,column=2,padx=10)
    
    
    

    

    




#Create Entry box 
f_name=Entry(root,width=35)
f_name.grid(row=0,column=1,padx=20)

l_name=Entry(root,width=35)
l_name.grid(row=1,column=1,padx=20)

address=Entry(root,width=35)
address.grid(row=2,column=1,padx=20)

city=Entry(root,width=35)
city.grid(row=3,column=1,padx=20)

zipcode=Entry(root,width=35)
zipcode.grid(row=4,column=1,padx=20)

state=Entry(root,width=35)
state.grid(row=5,column=1,padx=20)


#Create Text Box Labels
f_name_label=Label(root,text="First Name")
f_name_label.grid(row=0,column=0)

l_name_label=Label(root,text="Last Name")
l_name_label.grid(row=1,column=0)

address_label=Label(root,text="Address")
address_label.grid(row=2,column=0)

city_label=Label(root,text="City")
city_label.grid(row=3,column=0)

zipcode_label=Label(root,text="Zipcode")
zipcode_label.grid(row=4,column=0)

state_label=Label(root,text="State")
state_label.grid(row=5,column=0)



#Create  Buttons
submit_bt=Button(root,text="Add Record To Database",command=submit)
submit_bt.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=5)

query_btn=Button(root,text="Show Records",command=query)
query_btn.grid(row=7,column=0,columnspan=2,padx=10,pady=10,ipadx=34)

delete_btn=Button(root,text="Delete Records",command=widget_delete)
delete_btn.grid(row=8,column=0,columnspan=2,padx=10,pady=10,ipadx=34)

update_btn=Button(root,text="Update Records",command=update)
update_btn.grid(row=10,column=0,columnspan=2,padx=10,pady=10,ipadx=34)




root.mainloop()