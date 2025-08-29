from tkinter import *
import sqlite3

root=Tk()
root.title("GUI With Database")
root.geometry("400x400")

db=sqlite3.connect("GUI1.db")
cr=db.cursor()
cr.execute("CREATE TABLE addresses(first_name TEXT, last_name TEXT, address TEXT, city TEXT, stast TEXT, zipcode INTEGER)")


db.commit()

db.close()


root.mainloop()