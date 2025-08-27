from tkinter import *

root=Tk()
root.title("Menu Bars")

def new_file(): pass
def open_file(): pass
def undo(): pass
def redo(): pass
def find(): pass
def replace(): pass
def select(): pass



menubar=Menu(root)
root.config(menu=menubar)
# File menu
file_menu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Exit",command=root.quit)
# Edit menu
Edit_menu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=Edit_menu)
Edit_menu.add_command(label="Undo",command=undo)
Edit_menu.add_command(label="Redo",command=redo)
Edit_menu.add_separator()
Edit_menu.add_command(label="Find",command=find)
Edit_menu.add_command(label="Replace",command=replace)
# Selection menu
Selection_menu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Selection",menu=Selection_menu)
Selection_menu.add_command(label="Select all",command=select)




root.mainloop()