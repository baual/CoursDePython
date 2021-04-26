#multiple args
# That variable args stores a collection of the arguments that the function can iterate through.
def print_args(*args):
    for arg in args:
        print(f'arg = {arg}')

print_args('a')
print_args('a', 'b')
print_args('a', 'b', 'c')
# output
# arg = a
# arg = a
# arg = b
# arg = a
# arg = b
# arg = c

print()

#what is the data type or args
def print_args(*args):
      #for arg in args:
  #  print(f'arg = {arg}')
  print(args)
  print(type(args))

print_args('a')
print_args('a', 'b')
print_args('a', 'b', 'c')

# output
# ('a',)
# <class 'tuple'>
# ('a', 'b')
# <class 'tuple'>
# ('a', 'b', 'c')
# <class 'tuple'>

# it is a tuple !
# What is a tuple? In short, it's just like a list with a few differences.
#  The most notable difference is that you can't modify the contents of a tuple.
#  In the current code sample, the function can't call append() or remove(),
#  call sort() or reverse(), or assign a new value to an element

# so args[0] = 'z' is forbidden