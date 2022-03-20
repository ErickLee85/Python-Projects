from tkinter import *
import tkinter as tk
from tkinter import messagebox
import studentTrack_func
import studentTrack_main

def load_gui(self):
    #labels for table columns with grid coordinates
    self.lbl_fname = tk.Label(self.master,bg='darkgrey',text='First Name:')
    self.lbl_fname.grid(row=0,column=0,padx=(27,0),pady=(25,0),sticky=N+W)
    self.lbl_lname = tk.Label(self.master,bg='darkgrey',text='Last Name:')
    self.lbl_lname.grid(row=2,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_phone = tk.Label(self.master,bg='darkgrey',text='Phone Number:')
    self.lbl_phone.grid(row=4,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_email = tk.Label(self.master,bg='darkgrey',text='Email Address:')
    self.lbl_email.grid(row=6,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_course = tk.Label(self.master,bg='darkgrey',text='Course:')
    self.lbl_course.grid(row=8,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_info = tk.Label(self.master,bg='darkgrey',text='Student Information:')
    self.lbl_info.grid(row=0,column=3,padx=(155,0),pady=(25,0),sticky=E)
    self.lbl_info.configure(font=("Arial", 10, "italic"))
    
    #inputs for data fields
    self.txt_fname = tk.Entry(self.master,text='')
    self.txt_fname.grid(row=1,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_lname = tk.Entry(self.master,text='')
    self.txt_lname.grid(row=3,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_phone = tk.Entry(self.master,text='')
    self.txt_phone.grid(row=5,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_email = tk.Entry(self.master,text='')
    self.txt_email.grid(row=7,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_course = tk.Entry(self.master,text='')
    self.txt_course.grid(row=9,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)

    #Define the listbox with a scrollbar and grid them
    self.scrollbar1 = Scrollbar(self.master,orient=VERTICAL)
    self.lstList1 = Listbox(self.master,exportselection=0,yscrollcommand=self.scrollbar1.set)
    self.lstList1.bind('<<ListboxSelect>>',lambda event: studentTrack_func.onSelect(self,event))
    self.scrollbar1.config(command=self.lstList1.yview)
    self.scrollbar1.grid(row=1,column=5,rowspan=8,columnspan=2,padx=(15,0),pady=(25,0),sticky=N+E+S)
    self.lstList1.grid(row=1,column=2,rowspan=8,columnspan=4,padx=(0,0),pady=(25,0),sticky=N+E+S+W)

    #buttons
    self.btn_submit = tk.Button(self.master,width=12,height=2,bg='lightgreen',text='Submit',command=lambda: studentTrack_func.addToList(self))
    self.btn_submit.grid(row=9,column=0,padx=(45,0),pady=(45,10),sticky=W)

    self.btn_delete = tk.Button(self.master,width=12,height=2,bg='red',text='Delete',command=lambda: studentTrack_func.onDelete(self))
    self.btn_delete.grid(row=10,column=0,padx=(45,0),pady=(45,10),sticky=W)
    
    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close',command=lambda: studentTrack_func.ask_quit(self))
    self.btn_close.grid(row=9,column=4,columnspan=1,padx=(0,40),pady=(45,10),sticky=E)

    self.btn_clear = tk.Button(self.master,width=12,height=2,text='Clear Fields', command=lambda: studentTrack_func.onClear(self))
    self.btn_clear.grid(row=10,column=4,columnspan=1,padx=(0,40),pady=(45,10),sticky=E)

    studentTrack_func.create_db(self)

if __name__ == "__main__":
    pass
