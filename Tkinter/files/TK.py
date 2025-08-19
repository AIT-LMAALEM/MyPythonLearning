from tkinter import *

window= Tk()
window2= Toplevel(bg="black")

window.geometry("420x320+400+150")
window2.geometry("400x300")

# window.minsize(210,110)
# window.maxsize(1200,800)
window.resizable(False,False)
# window.resizable(True,False)
# window.resizable(False,True)

window.title("encrypte programme")
window.config(bg="#36454F")       #bg back ground



window.mainloop()

