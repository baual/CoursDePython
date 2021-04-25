#       Concept
#       using .seek() offset and whence
#       setting the pointer in a file with positive offset values and whence location
#   new_file.seek(13)
#   new_contents = new_file.read()
#   print(new_contents)
#   new_file.seek(0,2)
#       using .seek() to set the read/write pointer in a file
#       offset values and whence arguments
#       .seek() can set the pointer to a desired index from the beginning of the file
#       the example below moves to the character to offset 10 (the 11th character)

#   IMPORTANT IMPORTANT
#   new_file.seek(10)
#       which is also written with an optional second argument, know as whence ("from where")

#   new_file.seek(10,0)
#       using 0 for whence starts the offset from the beginning of the file

#   Note: the offset must be a positive integer in Python 3, so we cannot offset backwards from the end of the file

#       file.seek(offset, whence)
#       whence mode	description
#       0	points to the beginning of the file
#       1	points to the current location
#       2	points to the end of the file & offset is always 0
#       using whence 
#           the index can be offset from either the beginning, current location or to the end of the 
#           file (where there is no offset applied)

# Examples
# seek to a specific location

# create, write, read and print a file
tips_file = open('code_tips.txt', 'w+')
tips_file.write('-use simple function and variable names\n-comment code\n-organize code into functions\n')
tips_file.seek(0)
tips_text = tips_file.read()
print(tips_text)
# output
# -use simple function and variable names
# -comment code
# -organize code into functions

# setting a specific seek() index 
tips_file.seek(13)
# now read starts from 14th character of file
tips_text = tips_file.read()
print(tips_text)
# ouput
# unction and variable names
# -comment code
# -organize code into functions

# string slicing on a read of an entire file
# read from the start
tips_file.seek(0)
tips_text = tips_file.read()

# slice from the 14th character to end
print(tips_text[13:])
# ouput
# unction and variable names
# -comment code
# -organize code into functions


# Examples
# seek() with optional whence argument

# setting pointer to end of file with whence value = 2
tips_file.seek(0,2)
tips_file.write("-use seek(0,2) to set read/write at end of file\n")

# read from beginning of file - .seek(0,0) is same as .seek(0)
tips_file.seek(0,0)
tips_text = tips_file.read()
print(tips_text)
# ouput
# -use simple function and variable names
# -comment code
# -organize code into functions
# -use seek(0,2) to set read/write at end of file


# point to file beginning and overwrite 1st line
tips_file.seek(0)
tips_file.write('-use simple function and variable names\n'.upper())

# show new file contents
tips_file.seek(0,0)
tips_text = tips_file.read()
print(tips_text)
# ouput
# -USE SIMPLE FUNCTION AND VARIABLE NAMES
# -comment code
# -organize code into functions
# -use seek(0,2) to set read/write at end of file

#BE CAREFUL TO DO NOT OVERWRITE SOMETHING YOU WON'T
# point to file beginning and overwrite 1st line
tips_file.seek(0)
tips_file.write('-use simple function and variable names BLABLABLA\n'.upper())

# show new file contents
tips_file.seek(0,0)
tips_text = tips_file.read()
print(tips_text)
# ouput
# -USE SIMPLE FUNCTION AND VARIABLE NAMES BLABLABLA
# ode
# -organize code into functions
# -use seek(0,2) to set read/write at end of file