# get the list of methods supported by an objecty.
#  here under 1 which is an integer
print(dir(1))
# output
# ['__abs__', '__add__', '__and__', '__bool__',
# '__ceil__', '__class__', '__delattr__', '__dir__',
# '__divmod__', '__doc__', '__eq__', '__float__',
# '__floor__', '__floordiv__', '__format__', '__ge__',
# '__getattribute__', '__getnewargs__', '__gt__',
# '__hash__', '__index__', '__init__', '__int__', 
# '__invert__', '__le__', '__lshift__', '__lt__',
# '__mod__', '__mul__', '__ne__', '__neg__', '__new__',
# '__or__', '__pos__', '__pow__', '__radd__', '__rand__',
# '__rdivmod__', '__reduce__', '__reduce_ex__',
# '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__',
# '__rmul__', '__ror__', '__round__', '__rpow__',
# '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__',
# '__rxor__', '__setattr__', '__sizeof__', '__str__',
# '__sub__', '__subclasshook__', '__truediv__',
# '__trunc__', '__xor__', 'bit_length', 'conjugate',
# 'denominator', 'from_bytes', 'imag', 'numerator',
# 'real', 'to_bytes']

# This confusing list is all the int object's methods. The dir() function provides a list
#  of attributes and methods for whatever you put in the parentheses.

# When you work with Python, you might hear methods referred to as functions.
#  In Python, the two terms, methods and functions, are synonymous. But you
#  can avoid confusion when talking with other people about Python by calling them methods.
print()
# All the entries you see in the output list are methods. A method represents an action that
#  you can perform on an object. For example, to_bytes() outputs the object value in byte
#  format, which is just a specific way of looking at the data.

# Notice the __str__ method in the list. This method turns a value into a str type.
#  An object's type is simply the class it was created from. So the type of 1 is int.

myVar = 1
print(type(myVar.__str__()))
# output <class 'str'>

