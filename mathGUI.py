from tkinter import *
import math

root = Tk()
root.minsize(600,800) #(width,height)

def volSphere():
    """Returns the volume of a Sphere with radius r"""
    r = float(sphereEntry.get()) #float convers number stored in a string or integer into a
                                #floating point number, without float we would receieve
                                #this error "TypeError: unsupported operand type(s) for ** or
                                #pow(): 'str' and 'int'"
    v = 4.0/3.0 * math.pi * r**3
    sphereLabel.configure(text = "The volume of the sphere is: {}.".format(v))

def Triangle_area():
    base = float(baseEntry.get())
    height = float(heightEntry.get())
    Area = base * height * 0.5
    areaLabel.configure(text = "The area of this Triangle is: {}.".format(Area))

def centimeters():
    Feet = float(ftEntry.get())
    Inches = float(inEntry.get())
    foot_cm = Feet * 12 * 2.54
    inches_cm = Inches * 2.54
    Total = foot_cm + inches_cm
    conversionLabel.configure(text = "The object is {} cm long!".format(Total))

def lightPower():
    telescope = float(lightEntry.get())
    human = 0.25 #human pupil is 0.5cm but I have already squared it here so I set it to 0.25
    conversion = telescope**2 / human
    light_Power.configure(text = "Your telescope is collecting {} times more light than your eye!".format(conversion))
    

sphereBtn = Button(root,pady=10, text="Calculate the volume of a Sphere",command=volSphere)
sphereBtn.pack()

sphereLabel = Label(root,pady=10,width=50,text="Enter the radius")
sphereLabel.pack()

sphereEntry = Entry(root,width=50)
sphereEntry.pack()

sphereLabel = Label(root, text="")
sphereLabel.pack()

####################################################################################

triangleBtn = Button(root,pady=20, text="Calculate the area of a Triangle",command=Triangle_area)
triangleBtn.pack()

triangleBase = Label(root,pady=10, width=50, text="Enter the base")
triangleBase.pack()

baseEntry = Entry(root,width=50)
baseEntry.pack()

triangleHeight = Label(root, pady=10,width=50, text="Enter the height")
triangleHeight.pack()

heightEntry = Entry(root,width=50)
heightEntry.pack()

areaLabel = Label(root, text="")
areaLabel.pack()

###################################################################################

cmButton = Button(root,pady=20, text = "Convert feet and inches to centimers\nFill out both fields",command=centimeters)
cmButton.pack()

ftLabel = Label(root,pady=10, width = 50, text="Enter feet")
ftLabel.pack()

ftEntry = Entry(root,width=50)
ftEntry.pack()

inLabel = Label(root,pady=10, width=50, text="Enter inches")
inLabel.pack()

inEntry = Entry(root, width=50)
inEntry.pack()

conversionLabel = Label(root,text="")
conversionLabel.pack()

######################################################################################

lightButton = Button(root,pady=20,command=lightPower,text="Compare the light gathering power of your telescope vs your Eye")
lightButton.pack()

lightLabel = Label(root,pady=10,width=50,text="Enter your telescopes diameter in centimers")
lightLabel.pack()

lightEntry = Entry(root,width=50)
lightEntry.pack()

light_Power = Label(root,text="")
light_Power.pack()

























root.mainloop()
