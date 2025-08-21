from tkinter import *

root = Tk()
root.geometry("400x200")

Label(root, text="TOP", bg="red").pack(side=TOP, fill=X)
Label(root, text="BOTTOM", bg="blue").pack(side=BOTTOM, fill=X)
Label(root, text="LEFT", bg="green").pack(side=LEFT, fill=Y)
Label(root, text="RIGHT", bg="yellow").pack(side=RIGHT, fill=Y)

Button(root,text="add").pack()
Button(root,text="get").pack()
Button(root,text="set").pack()
Button(root,text="remove").pack()




root.mainloop()