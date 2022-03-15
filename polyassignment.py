
class Employee:
    
    raise_amount = 1.10

    def __init__(self,first,last,salary):
        self.first = first
        self.last = last
        self.salary = salary

    def name(self):
        return "{} {}".format(self.first,self.last)

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)

class Professor(Employee):
    
    raise_amount = 1.20

    def __init__(self,first,last,salary,tenure,classes=[]):
        super().__init__(first,last,salary)
        self.classes = classes
        self.tenure = tenure

    def name(self):
        return("{} {} is Professor at Cornell University and teaches both {} and {}.".format(self.first,self.last,self.classes[0],self.classes[1]))


class campusPolice(Employee):

    raise_amount = 1.15
    
    def __init__(self,first,last,salary,badge_id,squad_car):
        super().__init__(first,last,salary)
        self.badge_id = badge_id
        self.squad_car = squad_car

    def name(self):
        return('Officer {} {} patrols campus during night hours, his Badge ID is {} and squad car number is {}.'.format(self.first,self.last,self.badge_id,self.squad_car))
        


professor1 = Professor("Carl", "Sagan", 75000, True,  ["Astronomy", "Physics"])
officer1 = campusPolice("Norrin", "Radd", 65000, "A564F", 214)

print(professor1.name())
print(officer1.name())





