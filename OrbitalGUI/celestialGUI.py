from tkinter import *
import math

root = Tk()
root.minsize(400,275)
root.maxsize(400,275)
root.title('Orbital Period Calculator')


def orbitalTime():
    distance = float(theEntry.get())
    formula = math.sqrt(distance**3)
    theYears = Label(width=50,text="",bg="darkblue",fg="white")
    theYears.pack()
    theYears.configure(text="The orbital period of your planet is {} Earth years!".format(round(formula,2))) #round(formula,2) is rounding the variable formula to two decimal places.
    theYears_window=my_canvas.create_window(200,200,window=theYears)
    
    
    
    
    

bg = PhotoImage(file="Image/spaceimage1.png")

#use canvas to overlay widgets on image
my_canvas = Canvas(root, width=400, height=300)
my_canvas.pack(fill="both", expand=True, anchor="ne")
    
#set image in canvas
my_canvas.create_image(0,0, image=bg)
#creating transparent text with image as bg
my_canvas.create_text(200,60,text="Enter the distance of your planet in AU(Astronomical Units).\n                            Example: Jupiters' AU is 5.20", fill="white")
               
theEntry = Entry(width=25) #be sure to script widgets above canvas script or program won't find them.
theEntry.pack()
theEntry_window=my_canvas.create_window(200,90, window=theEntry)


theButton = Button(pady=10, text="Calculate your planets year!",command=orbitalTime)
theButton.pack()
theButton_window=my_canvas.create_window(200,155,window=theButton)

root.mainloop()


