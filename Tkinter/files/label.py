from tkinter import *

win=Tk()
win.geometry("517x522")
win.resizable(False,False)
# win.config(bg="black")

back_ground=PhotoImage(file=r"C:\Users\PC\OneDrive\Pictures\Saved Pictures\cut1.png")
lbl=Label(win,image=back_ground)
lbl.place(x=0,y=0)
# image_label=PhotoImage(file=r"C:\Users\PC\OneDrive\Pictures\Saved Pictures\cut.png")

# lbl=Label(win,image=image_label)
lbl2=Label(win,text="Login",bg="white",fg="black",font=("arial",12,"bold"))
lbl2.place(x=70,y=100)

win.mainloop()