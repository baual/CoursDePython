#    Concept
#    open a file in a writable mode
#    open a file in a writing mode, with: 'w', 'w+', 'r+', 'a', 'a+'
#    MODE	Description
#    'r'	read only mode
#    'w'	write - overwrites file with same name
#    'w+'	write and read mode - overwrites file with same name
#    'r+'	read and write mode (no overwrite)
#    'a'	opens for appending to end of file (no overwrite)
#    'a+'	opens for appending to end of file (no overwrite) plus read

#    warning: 'w' and 'w+' modes will create a new file or overwrite existing files (deleting all file contents)

#    writing to a file opened in additional write modes: 'r+', 'a', 'a+'
#    Writing is the same - pointers are different




#    Concept
#    writing to a file opened in additional write modes: 'r+', 'a', 'a+'
#    Writing is the same - pointers are different


#                   writing to a file
#    read mode plus write 'r+' and append modes 'a', 'a+'
#    read plus mode 'r+' differs from write modes 'w', 'w+'
#    read plus doesn't blank out the file contents with an overwrite
#    append modes 'a', 'a+' differ from write modes 'w', 'w+'
#    append doesn't blank out the file contents with an overwrite
#    append pointer is set to the end of the file for every write
#    append plus (a+) is append mode, plus read mode
#    'r+', 'a', 'a+'
#    will not overwrite existing file content creating a blank file


#    read plus mode r+

#    read plus mode r+
#    create a file that has one line: "Count is: x"
#    overwrite with new count at the x location (x is an integer)

# [ ] review and run example - create a file with initial count of 0
count_file = open("count_file.txt", "w+")

count_file.write("Count is: 0")
count_file.seek(0)
print(count_file.readline().strip())

count_file.close()
# can rerun this cell
count_file = open("count_file.txt", "r+")

count_file.seek(0)
count_line = count_file.readline().strip()
print("BEFORE\n" + count_line)

# get the int character(s) after the colon and space, cast and increment
count = int(count_line[10:])+1

# write the incremented value to the file - overwrite before value
count_file.seek(10)
count_file.write(str(count))

count_file.seek(0)
print("\nAFTER\n" + count_file.readline().strip())

count_file.close()
# [ ]  review funtion code for inc_count() funtion that reads file and updates the count
# the file always has 1 line that is The count is: N, where N is an integer
def inc_count(cnt_file):
    cnt_file.seek(0,0)
    cnt_line = cnt_file.readline().strip()
    cnt = int(cnt_line[10:])+1
    cnt_file.seek(10,0)
    cnt_file.write(str(cnt))
    return cnt
# [ ] review and run example with call to function: inc_count() - **Run cell multiple times**
# opens file/prints initial value
count_file = open("count_file.txt", "r+")

count_file.seek(0)
count_line = count_file.readline().strip()
print("BEFORE\n" + count_line)

# call inc_count() to increase the count 5 times
for i in range(5):
    count = inc_count(count_file)
    count_file.seek(0)
    print("\nAFTER inc_count() call", i+1, "\n" + count_file.readline().strip())

count_file.close()