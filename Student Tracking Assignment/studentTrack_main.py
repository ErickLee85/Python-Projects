from tkinter import *
import tkinter as tk
from tkinter import messagebox

import studentTrack_GUI
import studentTrack_func


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #Defining my master frame configuration...
        self.master = master
        self.master.minsize(700,500) # (Height,Width)
        self.master.maxsize(700,500)
        studentTrack_func.center_window(self,700,500)
        self.master.configure(bg="darkgray")
        self.master.title("Student Tracking")
        self.master.protocol("WM_DELETE_WINDOW", lambda: studentTrack_func.ask_quit(self))
        arg = self.master
        studentTrack_GUI.load_gui(self)

        










if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()









