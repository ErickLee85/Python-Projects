#Protected and private encapsulation

class Encap:
    def __init__(self):
        self.__private = "I am private!" #creating a private attribute using double unders __
        print(self.__private)

class Derived(Encap):
    def __init__(self):
        Encap.__init__(self) #accessing Encap Parent Class
        self._protect = "I am protected!" #creating a protected attribute using a single underscore _
        print(self._protect)
        #If i put a print command "print(self.__private)" I will get an error because it is outside Encap and set to private.

obj1 = Derived()


