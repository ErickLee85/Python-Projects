import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os

def source(self):
    path_source = filedialog.askdirectory(initialdir="/", title="Source Folder")
    self.ent_src.insert(INSERT, path_source)#inserts selected dir into widget
    
def destination(self):
    path_dest = filedialog.askdirectory(initialdir="/", title="Destination Folder")
    self.ent_dest.insert(INSERT, path_dest)
    
def ask_quit(self):
    if messagebox.askokcancel("Exiting the program", "Are you sure you want to close?"):
        #This closes app
        self.master.destroy()
        os._exit(0)


sourceLocation = StringVar()
destinationLocation = StringVar()

if __name__ == "__main__":
    pass
