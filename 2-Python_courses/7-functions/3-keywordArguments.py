def print_keyword_args(**kwargs):
    
  third = kwargs.get('third', None) # kwargs means KeyWord ARGumentS
  if third != None:
    print('third arg =', third)


print_keyword_args(first='a')
#keyword first is passed with a as value
print_keyword_args(first='b', second='c')
#keyword first is passed with b as value
#keyword second is passed with e as value
print_keyword_args(first='d', second='e', third='f')
#keyword first is passed with d as value
#keyword second is passed with e as value
#keyword third is passed with f as value

# output
# third arg = f

# In this case, the code calls the print_keyword_args() function three times.
#  Each time, it passes in one or more keyword arguments like first='a'.
#  The function body can access a specific existing argument by using the kwargs.get() method.

# This approach provides a flexible way for a caller to pass in arguments.
#  The downside is that you must rely on a function's documentation or source code
#  to understand what that function expects. If you didn't already know that you could
#  (or should) pass an argument called third, you might never understand how to use the function correctly.


print()

def print_keyword_args(**kwargs):
    
  print('\n')

  for key, value in kwargs.items():
    print(f'{key} = {value}')
    
#         for key, value in kwargs.items():
# In this case, you're working with not a list object but rather a dict object or dictionary = <class 'dict'>
#  A dictionary is like a list, except each item has two parts: a name (or key) and a value.
#  You'll learn more about dictionaries in another module. In your code example, key is set
#  to an argument's keyword, and value is set to that argument's value.
  
  third = kwargs.get('third', None)
  if third != None:
    print('third arg =', third)


print_keyword_args(first='a')
# printout :first = a
print_keyword_args(first='b', second='c')
# printout :first = b
# printout :second = c
print_keyword_args(first='d', second='e', third='f')
# printout :first = d
# printout :second = d
# printout :third = f
# printout :third arg = f