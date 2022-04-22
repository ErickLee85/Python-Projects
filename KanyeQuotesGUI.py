import requests
from tkinter import *

root = Tk()
root.minsize(500,200)
root.maxsize(500,200)
root.title('Kanye Quotes')
root.configure(bg="darkgray")

def KanyeAPI():
    response = requests.get("https://api.kanye.rest")
    req = response.json()
    Kanye = (req['quote'])
    quoteLabel.configure(text="'{}'".format(Kanye))




mylabel = Label(pady=10, bg="darkgray", font="bold", text="Get your Kanye quote!")
mylabel.pack()

theButton = Button(pady=10, font="bold", text="Click Away!", command=KanyeAPI)
theButton.pack()

quoteLabel = Label(pady=10, bg="darkgray", fg="white", font="bold", wraplength=400, text="")
quoteLabel.pack()

if __name__ == "__main__":
    root.mainloop()
    





    
