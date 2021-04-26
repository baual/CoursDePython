print(type('7'))
print(type(7))
print(type(7.1))
#output
#<class 'str'>
#<class 'int'>
#<class 'float'>

#The isinstance() function
#The next technique uses the isinstance() function, which allows you to assert that you expect a value
#  to be a certain data type. The isinstance() function tells you whether the value is what you expected. 
# It returns the value True if your expectation is correct and False if it's incorrect.

print(isinstance('7', str))         #output:True
print(isinstance(7, int))           #output:True
print(isinstance(7.1, float))       #output:True

print(isinstance(7, str))           #output:False
print(isinstance('7', int))         #output:False
print(isinstance('7.1', float))     #output:False

print()

#What is the relationship between data types and variables?
#It's important to understand that the data type is part of the value. The data type is not part of the
#  variable that you might use to access the value. A variable can point to any value, regardless of the
#  value's data type.
x = 'a string'
print(type(x))
x = 7
print(type(x))
x = False 
print(type(x))

print()


#In the preceding module, you built an example that allows users to input two values. Your program would add
#  the values together after converting them by using the int() function.
#try one of the valure with a string and that'll fail
first_value = int(input('First Number: '))
second_value = int(input('Second number: '))
sum = first_value + second_value
print("Sum: " + str(sum))

#see file #2