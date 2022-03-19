import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os


def path(self):
    paths = filedialog.askdirectory(initialdir="/", title="Select file")
    self.first_browse.delete(1.0,END)#deletes previous directory
    self.first_browse.insert(INSERT, paths)#inserts selected dir into text widget
    
def path2(self):
    paths = filedialog.askdirectory(initialdir="/", title="Select file")
    self.second_browse.delete(1.0,END)
    self.second_browse.insert(INSERT, paths)
    
def ask_quit(self):
    if messagebox.askokcancel("Exiting the program", "Are you sure you want to close?"):
        #This closes app
        self.master.destroy()
        os._exit(0)


if __name__ == "__main__":
    pass
