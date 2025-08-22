from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Image Viewer")


img1=ImageTk.PhotoImage(Image.open(r"C:\Users\PC\OneDrive\Pictures\Saved Pictures\cut1.png").resize((400,400)))
img2=ImageTk.PhotoImage(Image.open(r"C:\Users\PC\OneDrive\Pictures\Screenshots\red.png").resize((400,340)))
img3=ImageTk.PhotoImage(Image.open(r"C:\Users\PC\OneDrive\Pictures\Screenshots\math.jpg").resize((400,400)))

img_list=[img1,img2,img3]


myLabel=Label(image=img1)
myLabel.grid(row=0,column=0,columnspan=3)




def forward(x):
    global myLabel
    global button_forward
    global button_back

    myLabel.grid_forget()
    myLabel=Label(image=img_list[x-1])
    myLabel.grid(row=0,column=0,columnspan=3)
    
    button_forward=Button(root,text=">>",command=lambda:forward(x+1))
    button_forward.grid(row=1,column=2)
    button_back=Button(root,text="<<",command=lambda:back(x-1))
    button_back.grid(row=1,column=0)
    
    
    
    

def back(x):
    global myLabel
    global button_forward
    global button_back
    myLabel.grid_forget()
    myLabel=Label(image=img_list[x-1])
    myLabel.grid(row=0,column=0,columnspan=3)
    button_back=Button(root,text="<<",command=lambda:back(x-1))
    button_back.grid(row=1,column=0)
    button_forward=Button(root,text=">>",command=lambda:forward(x+1))
    button_forward.grid(row=1,column=2)
    

    

button_back=Button(root,text="<<",command=lambda:back(),state=DISABLED)
button_quit=Button(root,text="EXIT PROGRAM",command=root.quit)
button_forward=Button(root,text=">>",command=lambda:forward(2))

button_back.grid(row=1,column=0)
button_quit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)



root.mainloop()