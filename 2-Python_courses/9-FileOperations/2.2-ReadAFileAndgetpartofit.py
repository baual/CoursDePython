# reading a file with .read(n) where n = number of characters to read


# each time poem_file.read(10) runs, the next 10 characters are read.
# Note: if .read(10) result is = '' (or empty string with no characters), it is likely that the end of the file has been reached. Perform a fresh .open() to reset read() to the beginning of the file.

# Examples
# examples expect that the cells that import and open of poem1.txt has been run without a read()
# Run the cell at the top of the notebook to import poem1.txt
# each line is a different approach to reading and displaying 10 characters of the poem

# [ ] review and run example to read poem1.txt 10 characters at a time
poem_file = open('poem1.txt', 'r')
poem_10char = poem_file.read(10)
print(poem_10char)
# output
# Loops I re

poem_parts = poem_file.read(10)
print(poem_parts)
# ouput
# peat
# loops
#cela 'imprime' la suite des 10 premiers. Le curseur n'est pas remis à zéro tant que l'on ne re ouvre pas le fichier

# [ ] REPEATEDLY RUN this cell,  + 5 more characters each time run are appended using string addition
# [ ]  consider why no additional text displays after multiple runs
poem_parts += poem_file.read(5)
print(poem_parts)
# ouput
# peat
# loops
# loop

print()

#doing same with cities
cities_file= open('cities.txt', 'r')
cities_10char = cities_file.read(10)
print(cities_10char)
# output
# Beijing
# Ca

cities_parts = cities_file.read(10)
print(cities_parts)
# ouput
# iro
# London
#cela 'imprime' la suite des 10 premiers. Le curseur n'est pas remis à zéro tant que l'on ne re ouvre pas le fichier

# [ ] REPEATEDLY RUN this cell,  + 5 more characters each time run are appended using string addition
# [ ]  consider why no additional text displays after multiple runs
cities_parts += cities_file.read(5)
print(cities_parts)
# ouput
# iro
# London
# Nair