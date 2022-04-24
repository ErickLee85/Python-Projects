import datetime
from datetime import timedelta
import pytz
from tkinter import *

root = Tk()
root.minsize(400,200)
root.title('Store Hours: 8am - 5pm')
root.configure(bg="darkgray")
          

OPTIONS = [
"Portland",
"New York",
"England"
        ] 

def storeHours(selection): #selection is being passed in as an argument from OptionMenu when user selects a store command is called and selection is returned to it
    morningHours = datetime.time(8, 0, 0)
    print(morningHours)
    eveningHours = datetime.time(17, 0, 0)
    midnight = datetime.time(23,59,0)
    store = selection
    if store == "Portland":
        portland = datetime.datetime.now(pytz.timezone('US/Pacific'))
        print(portland.time())
        if portland.time() >= morningHours and portland.time() <= eveningHours:
            storeLabel.configure(text="The Portland branch is open!")
        else:
            storeLabel.configure(text="The Portland branch is currently closed.")
        
    if store == "New York":
        NewYork = datetime.datetime.now(pytz.timezone('US/Eastern'))
        if NewYork.time() >= morningHours and NewYork.time() <= eveningHours:
            storeLabel.configure(text="The New York branch is open!")
        else:
            storeLabel.configure(text="The New York branch is currently closed.")
    if store == "England":
        England = datetime.datetime.now(pytz.timezone('Etc/GMT'))
        if England.time() >= morningHours and England.time() <= eveningHours:
            storeLabel.configure(text="The England branch is open!")
        else:
            storeLabel.configure(text="The England branch is currently closed.")
         
        

variable = StringVar(root)
variable.set("Choose Store") # default value

theLabel = Label(pady=10, bg="darkgray", text="Check to see if your store is open!")
theLabel.pack()

stores = OptionMenu(root, variable, *OPTIONS, command=storeHours) 
stores.pack(pady=10)

storeLabel= Label(pady=20, bg="darkgray", font="bold", text="")
storeLabel.pack()






















if __name__ == "__main__":
    root.mainloop()
