# Concept
# .readline(): read files a line at a time
# use .readline() to read a line in a file as a string
# each .readline() moves to the next available line in the file


# Examples
# open address to file
poem1 = open('poem1.txt', 'r')
# [ ] review and run example
# readline 1, 2, 3
poem_line1 = poem1.readline()
poem_line2 = poem1.readline()
poem_line3 = poem1.readline()

print(poem_line1 + poem_line2 + poem_line3)
# ouput
# Loops I repeat
# loops
# loops
# 
print(poem1.readline()) #will pick up the next line after the previous ones
# ouput
# loops
# 

poem1.close()