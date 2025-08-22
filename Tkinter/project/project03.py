from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Image Viewer")


img1=ImageTk.PhotoImage(Image.open(r"C:\Users\PC\OneDrive\Pictures\Saved Pictures\cut.png").resize((400,400)))
img2=ImageTk.PhotoImage(Image.open(r"C:\Users\PC\OneDrive\Pictures\Screenshots\red.png").resize((400,400)))
img3=ImageTk.PhotoImage(Image.open(r"C:\Users\PC\OneDrive\Pictures\Screenshots\math.jpg").resize((400,400)))

img_list=[img1,img2,img3]


myLabel=Label(image=img_list[0])
myLabel.grid(row=0,column=0,columnspan=3)



index=0
def forward(x):
    myLabel.config(image=img_list[x])
    global index 
    index=x 
    if index == len(img_list)-1:
        button_forward.config(state=DISABLED)
    else:
        button_forward.config(state=NORMAL,command=lambda:forward(x+1))
    if index==0:
        button_back.config(state=DISABLED)
    else:
        button_back.config(state=NORMAL,command=lambda:back(x-1))
       

    

def back(x):
    myLabel.config(image=img_list[x])
    global index
    index=x
    if index == len(img_list)-1:
        button_forward.config(state=DISABLED)
    else:
        button_forward.config(state=NORMAL,command=lambda:forward(x+1))
    if index==0:
        button_back.config(state=DISABLED)
    else:
        button_back.config(state=NORMAL,command=lambda:back(x-1))


button_back=Button(root,text="<<",command=lambda:back(0),state=DISABLED)
button_quit=Button(root,text="EXIT PROGRAM",command=root.quit)
button_forward=Button(root,text=">>",command=lambda:forward(1))

button_back.grid(row=1,column=0)
button_quit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)



root.mainloop()