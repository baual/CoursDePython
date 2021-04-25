#       .readlines()
# File read as a list with .readlines()
# converts the lines of a file into a list of strings


# open address to file
poem1 = open('poem1.txt', 'r')

# readlines and print as a list
poem_lines = poem1.readlines()

for line in poem_lines:
    print(line)
    
# output
# Loops I repeat
# 
# loops
# 
# loops
# 
# loops
# 
# I repeat
# 
# until I
# 
# break


print('\n\n\n')

# same with cities
cities = open('cities.txt', 'r')

# readlines and print as a list
cities_lines = cities.readlines()

for line in cities_lines:
    print(line)