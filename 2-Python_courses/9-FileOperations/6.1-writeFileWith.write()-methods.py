#      Concept
#      writing to a file opened in write mode 'w' or 'w+'
poem_file = open('poem.txt', 'w') 
poem_file.write("Hello World!\n")  
#      write mode: 'w'
#      write mode plus read: 'w+'
#      'w' and 'w+' modes will create a new file or overwrite existing files
#      All previous data will be lost

#      Examples

# - creates a new local file or overwrites the local file (makes it blank)
new_file = open('new_file.txt', 'w')

new_file.write("This is line #1 with 'w'\nThis is line #2 with 'w'\nThis is line #3 withn 'w'!\n")

# - close file and re-open in read mode 
# - head pointer is at start of file
new_file.close()
new_file = open('new_file.txt', 'r')

new_text = new_file.read()
print(new_text)

new_file.close()
#      'w+' means the file is in write plus read mode
#      after any write, the pointer is at the end of text that has been written
#      to read the entire file, the pointer needs to be at the beginning of the file - see .seek() below to set the file pointer