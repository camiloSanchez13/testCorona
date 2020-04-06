from tkinter import *
from tkinter import messagebox as MessageBox

def test():
    MessageBox.showwarning("Te la creiste we", 
    "Este no era un ppt.")

root = Tk()

Button(root, text = "Mira mira ....", command=test).pack()

root.mainloop()