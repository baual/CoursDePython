import datetime

class Person:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.dob = date_of_birth

    # return age in years from dob to now
    def get_age(self):
        return int((datetime.datetime.now() - self.dob).days / 365.25)
    
    # You can replace the built-in ___str__() method (or any other method)
    #  by overriding it. To override a method in Python, just provide a new version of the method in the class.
    def __str__(self):
        return self.name + ', age ' + str(self.get_age())
    
aPerson = Person("Adam", datetime.datetime(1990, 9, 16)) 

print(aPerson.name)

print(str(aPerson.get_age()))

print(str(aPerson))
print(aPerson.__str__())
print(aPerson)
# same output for all of them :-) = Adam, age 29