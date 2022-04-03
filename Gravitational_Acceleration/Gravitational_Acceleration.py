from tkinter import *
from tkinter import messagebox
import math
import time

root = Tk()
root.minsize(600,400)
root.maxsize(600,400)
root.title('Gravitational Acceleration - Solar System')


def freeFall(selection):
        fallTime = float(theSeconds.get())
        if selection == "Mercury":
            formula = 0.5 * 3.7 * fallTime**2 * 3.37
            theDistance = Label(width=75, text="", bg="#0080ff", fg="white", font="bold")
            theDistance.pack()
            theDistance.configure(text="You just fell {} ft in {} seconds on {}!".format(round(formula,2),fallTime,selection))
            theDistance_window=my_canvas.create_window(300,225, window=theDistance)
        if selection == "Venus":
            formula = 0.5 * 8.87 * fallTime**2 * 3.37
            theDistance = Label(width=75, text="", bg="#0080ff", fg="white", font="bold")
            theDistance.pack()
            theDistance.configure(text="You just fell {} ft in {} seconds on {}!".format(round(formula,2),fallTime,selection))
            theDistance_window=my_canvas.create_window(300,225, window=theDistance)
        if selection == "Earth":
            formula = 0.5 * 9.87 * fallTime**2 * 3.37
            theDistance = Label(width=75, text="", bg="#0080ff", fg="white", font="bold")
            theDistance.pack()
            theDistance.configure(text="You just fell {} ft in {} seconds on {}!".format(round(formula,2),fallTime,selection))
            theDistance_window=my_canvas.create_window(300,225, window=theDistance)
        if selection == "Our Moon":
            formula = 0.5 * 1.62 * fallTime**2 * 3.37
            theDistance = Label(width=75, text="", bg="#0080ff", fg="white", font="bold")
            theDistance.pack()
            theDistance.configure(text="You just fell {} ft in {} seconds on {}!".format(round(formula,2),fallTime,selection))
            theDistance_window=my_canvas.create_window(300,225, window=theDistance)
        if selection == "Mars":
            formula = 0.5 * 3.721 * fallTime**2 * 3.37
            theDistance = Label(width=75, text="", bg="#0080ff", fg="white", font="bold")
            theDistance.pack()
            theDistance.configure(text="You just fell {} ft in {} seconds on {}!".format(round(formula,2),fallTime,selection))
            theDistance_window=my_canvas.create_window(300,225, window=theDistance)
        if selection == "Mars\' moon: Phobos":
            formula = 0.5 * 0.0057 * fallTime**2 * 3.37
            theDistance = Label(width=75, text="", bg="#0080ff", fg="white", font="bold")
            theDistance.pack()
            theDistance.configure(text="You only fell {} ft in {} seconds on {}!".format(round(formula,2),fallTime,selection))
            theDistance_window=my_canvas.create_window(300,225, window=theDistance)
        if selection == "Mars\' moon: Deimos":
            formula = 0.5 * 0.003 * fallTime**2 * 3.37
            theDistance = Label(width=75, text="", bg="#0080ff", fg="white", font="bold")
            theDistance.pack()
            theDistance.configure(text="You only fell {} ft in {} seconds on {}!".format(round(formula,2),fallTime,selection))
            theDistance_window=my_canvas.create_window(300,225, window=theDistance)
        if selection == "Jupiter":
            formula = 0.5 * 24.79 * fallTime**2 * 3.37
            theDistance = Label(width=75, text="", bg="#0080ff", fg="white", font="bold")
            theDistance.pack()
            theDistance.configure(text="You just fell {} ft in {} seconds on {}!".format(round(formula,2),fallTime,selection))
            theDistance_window=my_canvas.create_window(300,225, window=theDistance)
        if selection == "Jupiters\' moon: Ganymede(Largest in Solar System)":
            formula = 0.5 * 3.7 * fallTime**2 * 3.37
            theDistance = Label(width=75, text="", bg="#0080ff", fg="white", font="bold")
            theDistance.pack()
            theDistance.configure(text="You just fell {} ft in {} seconds on {}!".format(round(formula,2),fallTime,selection))
            theDistance_window=my_canvas.create_window(300,225, window=theDistance)
        if selection == "Saturn":
            formula = 0.5 * 10.44 * fallTime**2 * 3.37
            theDistance = Label(width=75, text="", bg="#0080ff", fg="white", font="bold")
            theDistance.pack()
            theDistance.configure(text="You just fell {} ft in {} seconds on {}!".format(round(formula,2),fallTime,selection))
            theDistance_window=my_canvas.create_window(300,225, window=theDistance)
        if selection == "Uranus":
            formula = 0.5 * 8.87 * fallTime**2 * 3.37
            theDistance = Label(width=75, text="", bg="#0080ff", fg="white", font="bold")
            theDistance.pack()
            theDistance.configure(text="You just fell {} ft in {} seconds on {}!".format(round(formula,2),fallTime,selection))
            theDistance_window=my_canvas.create_window(300,225, window=theDistance)
        if selection == "Neptune":
            formula = 0.5 * 11.15 * fallTime**2 * 3.37
            theDistance = Label(width=75, text="", bg="#0080ff", fg="white", font="bold")
            theDistance.pack()
            theDistance.configure(text="You just fell {} ft in {} seconds on {}!".format(round(formula,2),fallTime,selection))
            theDistance_window=my_canvas.create_window(300,225, window=theDistance)
        if selection == "Pluto":
            formula = 0.5 * 0.62 * fallTime**2 * 3.37
            theDistance = Label(width=75, text="", bg="#0080ff", fg="white", font="bold")
            theDistance.pack()
            theDistance.configure(text="You just fell {} ft in {} seconds on {}!".format(round(formula,2),fallTime,selection))
            theDistance_window=my_canvas.create_window(300,225, window=theDistance)
        if selection == "The SUN!":
            formula = 0.5 * 274 * fallTime**2 * 3.37 / 5280
            theDistance = Label(width=75, text="", bg="#0080ff", fg="white", font="bold")
            theDistance.pack()
            theDistance.configure(text="You just fell {} miles in {} seconds on {}!".format(round(formula,2),fallTime,selection))
            theDistance_window=my_canvas.create_window(300,225, window=theDistance)
            messagebox.showinfo("Sun Gravity", "Thats crazy right?!")

    
    
    

options = ['Mercury',
           'Venus',
           'Earth',
           'Our Moon',
           'Mars',
           'Mars\' moon: Phobos',
           'Mars\' moon: Deimos',
           'Jupiter',
           'Jupiters\' moon: Ganymede(Largest in Solar System)',
           'Saturn',
           'Uranus',
           'Neptune',
           'Pluto',
           'The SUN!'
           ]



bg = PhotoImage(file="Image/rays.png") 
my_canvas = Canvas(root, width=500, height=300)
my_canvas.pack(fill="both", expand=True, anchor="center")
my_canvas.create_image(0,0, image=bg)



my_canvas.create_text(300, 50, text="Enter the seconds you are falling for.", fill="white", font="bold")

theSeconds = Entry(width=50)
theSeconds.pack()
theSeconds_window=my_canvas.create_window(300, 75, window=theSeconds)


my_canvas.create_text(300, 120, text="Select the body you are falling from!", fill="white", font="bold")

variable = StringVar(root)
variable.set("Pick a Body")
planets = OptionMenu(root, variable, *options, command=freeFall)
planets.pack()
planet_window=my_canvas.create_window(300, 175, window=planets)


root.mainloop()
