from tkinter import *

root= Tk()
root.title("sliders")

var=StringVar()
def value():
    Label(root,text=var.get()).pack()

slider=Scale(root,from_=0,
             to=100,
             orient="horizontal",
             variable=var,
             length=300,
             resolution=2,
             fg="red",
             sliderlength=20,
             sliderrelief="flat",
             border=1,
             
             )
slider.pack()
my_bt=Button(root,text="Click me!",command=value).pack()

root.mainloop()