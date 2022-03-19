import datetime
import pytz


morningHours = datetime.time(8, 0, 0)
eveningHours = datetime.time(17, 0, 0)

def storeHours():
    portland = datetime.datetime.now(pytz.timezone('US/Pacific'))
    if portland.time() >= morningHours and portland.time() <= eveningHours:
        print("The Portland branch is open!")
    else:
        print("The Portland branch is closed!")

    newyork = datetime.datetime.now(pytz.timezone('US/Eastern'))
    if newyork.time() >= morningHours and newyork.time() <= eveningHours:
        print("The NewYork branch is open!")
    else:
        print("The NewYork branch is closed!")

    england = datetime.datetime.now(pytz.timezone('Etc/GMT'))
    if england.time() >= morningHours and england.time() <= eveningHours:
        print("The England branch is open!")
    else:
        print("The England branch is closed!")




if __name__ == "__main__":
    storeHours()

