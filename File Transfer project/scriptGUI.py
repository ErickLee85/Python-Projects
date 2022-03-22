import tkinter as tk
from tkinter import *
from tkinter import messagebox

import scriptFunc


def load_gui(self):
        self.btn_src = tk.Button(self.master,command=lambda:scriptFunc.source(self), width=15,height=1,bg='lightgray',text="Source...")
        self.btn_src.grid(row=2,column=0,padx=(25,0),pady=(50,0))
        self.btn_dest = tk.Button(self.master,command=lambda:scriptFunc.destination(self), width=15,height=1,bg='lightgray',text="Destination...")
        self.btn_dest.grid(row=3,column=0,padx=(25,0),pady=(12,0))
        self.btn_check = tk.Button(self.master, width=15,height=2,bg='lightgray',text="Check for files...")
        self.btn_check.grid(row=4,column=0,padx=(25,0),pady=(12,0))
        self.btn_close = tk.Button(self.master,command=lambda:scriptFunc.ask_quit(self), width=15,height=2,bg='lightgray',text="Close Program")
        self.btn_close.grid(row=4,column=10,padx=(0,0),pady=(10,0),sticky=E)

        self.ent_src = Entry(self.master,width=40,textvariable = sourceLocation)
        self.ent_src.grid(row=2,column=1,columnspan=10,padx=(10,0),pady=(50,0))
        self.ent_dest = Entry(self.master,width=40,textvariable = destinationLocation)
        self.ent_dest.grid(row=3,column=1,columnspan=10,padx=(10,0),pady=(10,0))

        
if __name__ == "__main__":
    pass
