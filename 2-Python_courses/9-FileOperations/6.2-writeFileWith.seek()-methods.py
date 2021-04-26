#          Concept
#          using .seek(0)


#          setting the pointer to beginning of file
#          new_file.seek(0)
#          new_contents = new_file.read()
#          print(new_contents)

#          using .seek() to set the read/write pointer to beginning of file
#          new_file.seek(0) moves the file read\write pointer to the start of the file

# Examples
# seek() with 'w+'

# creates a new local file or overwrites the local file (makes it blank)
new_file = open('new_file.txt', 'w+')
# write plus read 'w+'
# 'w+' overwrites existing files of the same name - rendering the file blank
# the file is writable and readable


# - 'w+' overwrites, we can read, but the file is ***BLANK***
new_text = new_file.read()
print(new_text)
# write to the blank file
new_file.write("This is line #1 with 'w+'\nThis is line #2 with 'w+'\n")
# read and print (Note: the pointer is at the end of the file - result = empty string)  
new_text = new_file.read()

print(new_text)
# Expected: prints empty string above
# pointer was at end of file where there is nothing to read

# seek(0)
# sets the pointer to the beginning of the file, enabling read() to input the entire file contents

# [ ] review and run example - sets pointer to beginning of file
new_file.seek(0)
# [ ] review and run example - now read starts from beginning of file
new_text = new_file.read()
print(new_text)

# # [ ] review and run example - clean up and close file
new_file.close()
