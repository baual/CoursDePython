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




#inheritance

# You defined a new class (subclass) named MissingPerson that inherits from Person.
#  When created, a MissingPerson object creates a Person object by calling the latter's __init__() method.
#  Then, it defines an instance attribute of its own (missing_since) and a method that subtracts the date
#  the person went missing from today's date to compute how long that person has been missing.
class MissingPerson(Person):
    def __init__(self, name, date_of_birth, date_missing):
        # Construct the base object
        Person.__init__(self, name, date_of_birth)

        # Add a missing_since attribute
        self.missing_since = date_missing

    # Add a get_years_missing() method
    def get_years_missing(self):
        return int((datetime.datetime.now() - self.missing_since).days / 365.25)
    





#override a method

#inheritance from missing person
class MissingSKPerson(MissingPerson):
    def __init__(self, name, date_of_birth, date_missing):
        MissingPerson.__init__(self, name, date_of_birth, date_missing)

    # Override an inherited method
    # Occasionally, it's useful to override a method that's inherited from the base class to modify
    #  the way the method works in the subclass. You have already seen how to override methods:
    #  implement a method of the same name in the subclass. But what if you need to call
    #  the base class's version of the method from the inherited class?
    # In South Korea, babies are considered one year old when they are born.
    #  Consequently, they turn age two on their first birthday, age three on their second birthday,
    #  and so on. Suppose you wanted to create a special version of the MissingPerson class named MissingSKPerson
    #  that adds 1 to the integer returned by the get_age() method. That's what Python's super() method is for.
    # Override the get_age() method
    def get_age(self):
        return super().get_age() + 1    #super() used to call the get_age() method from parent class
    
 
 
 
    
# Remove an inherited attribute


# Suppose you defined a new class named AnonymousPerson that inherits from Person. In that case, you might want
#  to remove the name attribute so that an anonymous person remains just that—anonymous.
# You can include calls to Python's delattr() function in a class definition to remove attributes
#  that are inherited from the base class. Here's how an AnonymousPerson class might look:
class AnonymousPerson(Person):
    def __init__(self, date_of_birth):
        Person.__init__(self, '', date_of_birth)
        delattr(self, 'name')   #removing the attribute from inheritade class

    # in order to print we  need to surcharge also the print methjod
    def __str__(self):
        return 'His age is ' + str(self.get_age()) #no need to use super() because we didn't use the parent method





#classes in action :-) !!!
aPerson1 = Person("Adam", datetime.datetime(1990, 9, 16)) 
print(str(aPerson1.get_age()))
print(aPerson1)

#inheritance
aPerson2 = MissingPerson("Eve", datetime.datetime(1980, 7, 1), datetime.datetime(2016, 1, 1))
print(aPerson2.name + ' has been missing for ' + str(aPerson2.get_years_missing()) + ' years')

#method override
date_birth = datetime.datetime(1970, 2, 11)
date_missing = datetime.datetime(2017, 1, 1)
name = "Abel"
aPerson3 = MissingSKPerson(name,date_birth, date_missing)
print(str(aPerson3.get_age()))

#removing attibute
aPerson4 = AnonymousPerson( datetime.datetime(1990, 9, 16))
print(aPerson4)
