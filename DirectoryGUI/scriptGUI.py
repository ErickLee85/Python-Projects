import tkinter as tk
from tkinter import *
from tkinter import messagebox

import scriptFunc


def load_gui(self):
        self.btn_browse1 = tk.Button(self.master,command=lambda:scriptFunc.Source(self), width=15,height=1,bg='lightgray',text="Browse...")
        self.btn_browse1.grid(row=2,column=0,padx=(25,0),pady=(50,0))
        self.btn_browse2 = tk.Button(self.master,command=lambda:scriptFunc.Destination(self), width=15,height=1,bg='lightgray',text="Browse...")
        self.btn_browse2.grid(row=3,column=0,padx=(25,0),pady=(12,0))
        self.btn_check = tk.Button(self.master,command=lambda: scriptFunc.CheckFile(self), width=15,height=2,bg='lightgray',text="Check for files...")
        self.btn_check.grid(row=4,column=0,padx=(25,0),pady=(12,0))
        self.btn_close = tk.Button(self.master,command=lambda:scriptFunc.ask_quit(self), width=15,height=2,bg='lightgray',text="Close Program")
        self.btn_close.grid(row=4,column=10,padx=(0,0),pady=(10,0),sticky=E)

        self.first_browse = Entry(self.master,width=40)
        self.first_browse.grid(row=2,column=1,columnspan=10,padx=(10,0),pady=(50,0))
        self.second_browse = Entry(self.master,width=40)
        self.second_browse.grid(row=3,column=1,columnspan=10,padx=(10,0),pady=(10,0))

        
if __name__ == "__main__":
    pass
