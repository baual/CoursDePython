#      Concept
#      .readline() with .strip()
#      .strip() whitespace

#      poem_line = poem1.readline().strip()
#      .strip() removes leading and trailing whitespace, including the '\n' formatting character
#      .strip('*\n') removes leading and trailing * and \n

#      Examples
poem1 = open('poem1.txt', 'r')

# [ ] review and run example - readline while loop without removing '\n'
poem_line = poem1.readline()

while poem_line:
    print(poem_line)
    poem_line = poem1.readline()
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
poem1.close()



#      
#      now with .strip() to remove leading and trailing whitespace characters
#      

poem1 = open('poem1.txt', 'r')
poem_line = poem1.readline().strip()

while poem_line:
    print(poem_line)
    poem_line = poem1.readline().strip()
# output 
# Loops I repeat
# loops
# loops
# loops
# I repeat
# until I
# break    
poem1.close()