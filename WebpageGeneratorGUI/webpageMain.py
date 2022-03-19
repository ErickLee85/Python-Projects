import tkinter as tk
from tkinter import *
from tkinter import messagebox

import webpageGUI
import webpageFunc

class ParentWindow(Frame): #initializing my parent frame
    def __init__(self,master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master 
        self.master.minsize(400,300)
        self.master.maxsize(400,300)
        self.master.configure(bg='lightgray')
        self.master.title("Webpage Generator")
        webpageGUI.load_gui(self) #calling my load_gui function from webpageGUI.py 

if __name__== "__main__":
    root=tk.Tk()
    App = ParentWindow(root)
    root.mainloop() #creating an infinite loop so GUI stays active
