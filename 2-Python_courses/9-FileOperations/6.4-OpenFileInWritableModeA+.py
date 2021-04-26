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

#    Examples
#    append plus mode a+
# function writes to the open log argument
# loads function into memory but the function is not called
def logger(log):
    log_entry = input("enter log item (enter to quit): ")
    count = 0

    while log_entry:
        count += 1
        log.write(str(count) + ": " + log_entry + "\n")
        log_entry = input("enter log item (enter to quit): ")
        
    return count
    
# makes a blank file  (initialize/reset)
log_file = open('log_file.txt', 'w+')
log_file.close()
# opens the log_file before passing to logger() function call, below
# allows for calls below to run several times appending to the end of log_file

log_file = open('log_file.txt', 'a+')

# calls the above logger() function
# what happens running the cell above (a+) again before running this cell again? 
# what happens if log_file.seek(0) is run before an append?

logger(log_file)    

log_file.seek(0)
log_text = log_file.read()

print()
print(log_text)
log_file.close()



