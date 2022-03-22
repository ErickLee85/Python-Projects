import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import time
import shutil

import scriptGUI

def source(self):
    path_source = filedialog.askdirectory(initialdir="/", title="Source Folder")
    self.ent_src.insert(INSERT, path_source)#inserts selected dir into widget
    
def destination(self):
    path_dest = filedialog.askdirectory(initialdir="/", title="Destination Folder")
    self.ent_dest.insert(INSERT, path_dest)


def checkFile(self):
    dailyseconds = 24 * 60 *60
    now = time.time()
    before = now - dailyseconds
    source = self.ent_src.get()
    dest = self.ent_dest.get()
    #return os.path.getmtime(file) #os.path.getmtime() is retrieving the last modification time of each file from the source var

    for file in os.listdir(source): #os.listdir() retrieves a list of files in chosen directory
        source_file = os.path.join(source, file) #os.path.join() joines one or more path components
        return os.path.getmtime(file)

    if checkFile(source_file) > before: #conditional statement saying if the files are new or modified within the last 24 hours then do the next script.
        dest_file = os.path.join(dest, file)
        shutil.move(source_file, dest_file) #move the selected source files to the destination folder
   
def ask_quit(self):
    if messagebox.askokcancel("Exiting the program", "Are you sure you want to close?"):
        #This closes app
        self.master.destroy()
        os._exit(0)


if __name__ == "__main__":
    pass
