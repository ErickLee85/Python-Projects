import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import time
import shutil

def Source(self):
    paths = filedialog.askdirectory(initialdir="/", title="Select file")
    self.first_browse.delete(0, END)#deleting previous search so fields do not overlap
    self.first_browse.insert('1', paths)#inserts selected dir into text widget
    
def Destination(self):
    paths = filedialog.askdirectory(initialdir="/", title="Select file")
    self.second_browse.delete(0, END)
    self.second_browse.insert('1', paths)

def CheckFile(self):
    SECONDS_IN_DAY = 24 * 60 * 60

    now = time.time()
    before = now - SECONDS_IN_DAY
    sourceFolder = self.first_browse.get()
    destinationFolder = self.second_browse.get()

    for file in os.listdir(self.first_browse.get()):
        sourceLocation = os.path.join(sourceFolder, file)
        mod_time = os.path.getmtime(sourceLocation)
        if mod_time > before:
                destinationLocation_file = os.path.join(destinationFolder, file)
                shutil.move(sourceLocation, destinationLocation_file)
        messagebox.showinfo('Sucess','Files transfered successfully.')
                

    
    
def ask_quit(self):
    if messagebox.askokcancel("Exiting the program", "Are you sure you want to close?"):
        #This closes app
        self.master.destroy()
        os._exit(0)


if __name__ == "__main__":
    pass
