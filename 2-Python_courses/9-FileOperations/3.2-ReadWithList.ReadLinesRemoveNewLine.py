#       .readlines()
# File read as a list with .readlines()
# converts the lines of a file into a list of strings


# open address to file
poem1 = open('poem1.txt', 'r')

# readlines and print as a list
poem_lines = poem1.readlines()
# output
# ['Loops I repeat\n', 'loops\n', 'loops\n', 'loops\n', 'I repeat\n', 'until I\n', 'break\n']
print(poem_lines)
# [ ] print each list item 
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
# 




# remove newline characters from lists created using .readlines()
count=0
for line in poem_lines:
    poem_lines[count] = line[:-1]
    count += 1
# line[:-1] sets the end point at the last character of the string, the result is the '\n' (newline) character is omitted

# list item	list item contents
# poem_lines[0]	'Loops I repeat\n'
# poem_lines[1]	'loops\n'
# poem_lines[2]	'loops\n'
# poem_lines[3]	'I repeat\n'
# ...	...
print(poem_lines)
# output
# ['Loops I repeat', 'loops', 'loops', 'loops', 'I repeat', 'until I', 'break']

# [ ] print each list item 
for line in poem_lines:
    print(line)
# output
# Loops I repeat
# loops
# loops
# loops
# I repeat
# until I
# break

print('\n\n\n')

# same with cities
cities = open('cities.txt', 'r')

# readlines and print as a list
cities_lines = cities.readlines()

count=0
for line in cities_lines:
    cities_lines[count] = line[:-1]
    count += 1
    
print(cities_lines)
# output
# ['Beijing', 'Cairo', 'London', 'Nairobi', 'New York City', 'Sydney', 'Tokyo']

for line in cities_lines:
    print(line)
# output
# Beijing
# Cairo
# London
# Nairobi
# New York City
# Sydney
# Tokyo