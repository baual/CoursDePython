#    Concept
#    .readline() in a while loop

#    poem_line = poem1.readline()
#    while poem_line:
#        print(poem_line.capitalize())
#        poem_line = poem1.readline()


#    while .readline()
#    while loop continues while the readline() value in poem_line returns text
#    a string value evaluates as True in the while loop
#    an empty string, '', evaluates not True in the while loop
#    when readline() reaches the end of the file, an empty string is returned


#    Examples
poem1 = open('poem1.txt', 'r')

#  remove last character ('\n') and print as upper case
poem_line = poem1.readline()

while poem_line:
    print(poem_line[:-1].upper())  #on enleve le '\n' puis on met en majuscule
    poem_line = poem1.readline()

# output
# LOOPS I REPEAT
# LOOPS
# LOOPS
# LOOPS
# I REPEAT
# UNTIL I
# BREAK

poem1.close()