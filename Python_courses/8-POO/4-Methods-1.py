# Python objects always have methods, even if you don't define any yourself. For example, every object
#  has a __str__() method added by Python that returns a string representation of the object.
#  The default __str__() method works fine for something simple like an int, but it does nothing meaningful
#  to a person object. When you call __str__() on a person object, you get something like this:

# <__main__.person object at 0x7ff9e91ab978>

# For this reason, Python programmers frequently replace the built-in __str__() method with one
#  of their own when they write custom classes to serve an application.

# like attibutes 
# Static methods vs. instance methods
#Python objects support two types of methods: static methods and instance methods.
#  Static methods apply to all objects of a certain type and can be called without instantiating
#  the class to which the methods belong. Instance methods apply to a specific object or class instance.
#  A get_age() method should be an instance method because one person's age doesn't necessarily equal
#  another person's age.

# Python's math class contains several static methods to help you perform mathematical operations.
#  For example, the following statement computes the square root of 4:
# root = math.sqrt(4)

#you can also writze your own class with a static method to do so
class mathops:
    @staticmethod
    def square(val):
        return val * val
    
#then use it
square = mathops.square(2)
print(square)


