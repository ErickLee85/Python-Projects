import tkinter as tk
from tkinter import *

import webpageFunc

def load_gui(self): #setting up GUI using grid
    self.pagebtn = tk.Button(self.master,command=lambda: webpageFunc.website(self), width=15,height=2, bg='lightgreen',text="Generate Page!")
    self.pagebtn.grid(row=0,column=1,padx=(120,0),pady=(25,0),sticky=E)

    self.pageEntry = tk.Entry(self.master,width=50)
    self.pageEntry.grid(row=3,column=1,columnspan=5, padx=(50,0),pady=(0,0))

    self.pageLabel = tk.Label(self.master,text="Type below!")
    self.pageLabel.grid(row=2,column=1, padx=(150,0),pady=(10,0))


if __name__ == "__main__":
    pass
    
