class MyClass:
    print('MyClass created!')
    
    
myVar=MyClass()

print(type(myVar))
# The output shows that the type of myVar is
#  __main__.myClass. __main__
#  is the scope in which this code is executing.
# A scope is a kind of logical grouping that holds pieces of code together.
# You don't see a scope for the int type because int is defined outside the
#  scope of the current application. You see __main__ for myClass because
#  you defined myClass in the current application. It's the default scope,
#  but you don't need to worry about it for now. The important takeaway,
#  for the moment, is that myVar is an instance of the myClass class.
print()
print(dir(myVar))
# output ['__class__', '__delattr__', '__dict__', '__dir__',
#  '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
#  '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__',
#  '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
#  '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
# Notice that you get default methods with your new class. Python provides
#  a class with these default methods for performing essential tasks.
#  These methods aren't all that important right now, but it's a good idea
#  to know that they exist. As you continue with this module, this information will become more relevant.

