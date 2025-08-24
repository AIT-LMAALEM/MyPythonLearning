from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()
root.title("Open Files Dialog Box")

# Créer un label dès le départ
image_label = Label(root)
image_label.pack()

def openimage():
    filename = filedialog.askopenfilename(
        initialdir="C:/Users/PC/OneDrive/Pictures/Saved Pictures/images",
        title="Select A File",
        filetypes=(("png files","*.png"),("jpg files","*.jpg"),("all files","*.*"))
    )
    if filename:
        new_img = ImageTk.PhotoImage(Image.open(filename))
        image_label.config(image=new_img)      # Mettre à jour l'image
        image_label.image = new_img             # Conserver la référence
    else:
        root.quit()

Button(root, text="Open Image", command=openimage).pack()

root.mainloop()
