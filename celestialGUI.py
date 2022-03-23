from tkinter import *
import math

root = Tk()
root.minsize(400,200)
root.title('Planetary Calculator')


def orbitalTime():
    distance = float(theEntry.get())
    formula = math.sqrt(distance**3)
    orbitalLabel.configure(text="The orbital period of your planet is {} Earth years!".format(formula))

    
theLabel = Label(pady=20,text="Enter the distance of your planet in AU(Astronomical Units).\nExample: Jupiters' AU is 5.20")
theLabel.pack()

theEntry = Entry(width=50)
theEntry.pack()

theButton = Button(pady=10, text="Calculate your planets year!",command=orbitalTime)
theButton.pack()

orbitalLabel = Label(pady=20,text="")
orbitalLabel.pack()

root.mainloop()


