# Attributes come in two varieties: class attributes and instance attributes.*
#  A class attribute is an attribute that applies to all instances of a class
#  rather than to individual instances (objects created from the class)
# . What's interesting about class attributes is that you don't have to
#  instantiate a class to access them. Class attributes are always available.

# class attributes:
# A great example of a class attribute is in Python's built-in math class.
#  The math class has class attributes named pi and e that contain the values
#  of common mathematical constants. Because you don't have to create a class
#  instance to access a class attribute, you can compute the area of a circle this way in Python:
# area = math.pi * radius * radius


# instance attibutes
# By contrast, an instance attribute is one that is "instanced" for each and every
#  object you create. A person class might have a name attribute that holds a person's name.
#  name would need to be an instance attribute so that every person could be assigned a different name.
#  That class also could have attributes that define additional information about a missing person, such as:

# A photo of the person's face
# A unique ID, such as a Social Security number
# The person's date of birth
# These attributes should be instance attributes because they vary from person to person.




# One of the many popular packages available for Python is scikit-learn, an open-source library
#  that's used to build machine learning models. scikit-learn includes several built-in datasets,
#  one of which is the Olivetti faces dataset.
# pip install sklearn then 
# Paste the following statements into your new file to load the faces dataset:

#from sklearn.datasets import fetch_olivetti_faces
import datetime
# Load the dataset
#faces = fetch_olivetti_faces()

# Prove that the dataset was loaded
#print(faces.data.shape)


class Person:
#  Inside __init__() are three instance attributes that can be accessed on Person objects:
# The self keyword refers to the object instance and is provided in the first argument to __init__().
#    def __init__(self, name, photo, date_of_birth):
    def __init__(self, name, date_of_birth):
        self.name = name            #name, which holds the person's name
        #self.photo = photo          #photo, which holds an image of the person's face
        self.dob = date_of_birth    #dob, which holds the person's date of birth

#  (the self argument is provided by Python itself). Each argument is copied into the corresponding
#  instance attribute.
#les images marchent pas donc on s'en passe :-(


#les images marchent pas donc on s'en passe :-(
# aPerson = Person("Adam", faces.images[0], datetime.datetime(1990, 9, 16))   
aPerson = Person("Adam", datetime.datetime(1990, 9, 16)) 

print(aPerson.name)


# Data hiding
# Many programming languages that support OOP also support data hiding by allowing methods and
#  attributes—"class members"—to be declared private or protected. Private class members can be
#  accessed from inside an object but not from outside the object. Protected class members can be
#  accessed inside an object and inside objects that are subclassed from it (more on this later),
#  but not from outside.

# Python doesn't support data hiding—at least not in the same sense that other languages do.
#  Guido van Rossum, the creator of Python, felt that data hiding makes languages harder to use.
#  Consequently, you can't hide class members in Python.

# But you can use well-established conventions to let others know that certain class members
#  are for internal use only and should not be accessed from the outside. Prefacing a class
#  member name with an underscore, as in _myProtectedVar, indicates that the class member
#  is protected. Using two underscores (for example, __cleanup()) indicates that the class member is private.

# so
# _xxxxx means Protected
# __xxxx means Private