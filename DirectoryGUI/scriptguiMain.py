import tkinter as tk
from tkinter import *
from tkinter import messagebox

import scriptGUI
import scriptFunc

class ParentWindow(Frame):
    def __init__(self,master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(500,200)
        self.master.maxsize(500,200)
        self.master.configure(bg='lightgray')
        self.master.title("Check Files")
        arg = self.master
        scriptGUI.load_gui(self)

        



if __name__=="__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
