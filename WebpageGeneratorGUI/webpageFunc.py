import tkinter as tk
from tkinter import *
import webbrowser


def website(self):
    
    message = self.pageEntry.get() #assigning variable to string from entry widget. using .get() to retrieve data
    f = open("index.html", "x") #creating a new html file using "x"
    f.write("<html>\
            <body>\
                <h1>"+
            (message)+ #Passing in message variable 
                "</h1>\
            </body>\
          </html>")   
    f.close()
    webbrowser.open_new_tab('index.html') #opening the file in a new tab











if __name__ == "__main__":
    pass
