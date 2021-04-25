colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'brown']

# print(f'0-based indexing into the list ... second item: {colors[1]}')

# print(f'Last item of the list: {colors[-1]}')

# print(f'Next to last item in the list: {colors[-2]}')

print('\nPrint a SLICE, starting at index 2 and excluding index 5:')
print(colors[2:5])
print(type(colors[2:5]))
# output
# ['blue', 'yellow', 'orange']
# <class 'list'>

print('\nPrint a slice, starting at index 0 to index 3:')
print(colors[:3])
# output
# ['red', 'green', 'blue']

print('\nPrint a slice, starting a index 4 to the end of the list:')
print(colors[4:])
# output
# ['orange', 'purple', 'brown']

print('\nPrint a slice, from the 4th from the end up until the last item:')
print(colors[-4:-1])
# output
# ['yellow', 'orange', 'purple']



# As we saw in the first print() statement, the value on the left side of the colon is inclusive.
#  So the slice includes the element at that index. The value on the right side of the colon is exclusive.
#  So the slice doesn't contain the element at that index.

