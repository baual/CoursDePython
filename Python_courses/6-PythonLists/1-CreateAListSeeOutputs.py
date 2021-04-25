#list creation

colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'brown']

#empty list
my_list = []
# Creating an empty list comes in handy when you can't initialize your list with values.
#  Instead, you must add elements by using logic in your program. You'll see how to use
#  this method later in this exercise.


print(colors)
print(type(colors))
#output
# ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'brown']
# <class 'list'>

print()

#mixing data types
sundry = ['John', 3.14, 7, False]
print(sundry)
print(type(sundry))

# ouput
# ['John', 3.14, 7, False]
# <class 'list'>



print()

#first is [0]
print(f'0-based indexing into the list ... second item: {colors[1]}')

# [-value] means from the end of the list -1 = tha last one
print(f'Last item of the list: {colors[-1]}')
#-2 = the one BEFORE the last
print(f'Next to last item in the list: {colors[-2]}')

#output
# 0-based indexing into the list ... second item: green
# Last item of the list: brown
# Next to last item in the list: purple

print()


colors = ['red', 'green', 'blue']
print(colors[3])
# output
# IndexError: list index out of range 
# 3 is out of range

