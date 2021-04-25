# Concept
# Read a file using .read()
# reading text and return String

poem_file = open('poem1.txt', 'r') #file opening
# .read() loads the content of the file into memory as a string, including formatting such as new line (\n)

# shows the file as a string with formatting characters such as "\n", output should be non-blank
poem_contents = poem_file.read()

# since .read() loaded the file as a string it can be printed
print(poem_contents)


#same with the cities file
cities_file=open('cities.txt','r')
cities_content=cities_file.read()
print(cities_content)

print("\n\n\n\n")


# reading a file with .read(n) where n = number of characters to read


# each time poem_file.read(10) runs, the next 10 characters are read.
# Note: if .read(10) result is = '' (or empty string with no characters), it is likely that the end of the file has been reached. Perform a fresh .open() to reset read() to the beginning of the file.

# Examples
# examples expect that the cells that import and open of poem1.txt has been run without a read()
# Run the cell at the top of the notebook to import poem1.txt
# each line is a different approach to reading and displaying 10 characters of the poem

# [ ] review and run example to read poem1.txt 10 characters at a time
# poem_file = open('poem1.txt', 'r') already open above
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


#doing same with cities
cities_10char = cities_file.read(10)
print(cities_10char)
# output
# 

cities_parts = cities_file.read(10)
print(cities_parts)
# ouput
# 
#cela 'imprime' la suite des 10 premiers. Le curseur n'est pas remis à zéro tant que l'on ne re ouvre pas le fichier

# [ ] REPEATEDLY RUN this cell,  + 5 more characters each time run are appended using string addition
# [ ]  consider why no additional text displays after multiple runs
cities_parts += cities_file.read(5)
print(cities_parts)
# ouput
# 