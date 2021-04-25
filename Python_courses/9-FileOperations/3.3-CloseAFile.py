#    Concept


#  .close()
#   File .close() method frees resources
#   file.close() method removes the reference created from file open() function

#   poem1.close()


# [ ] review and run example: open and readlines of poem1.txt
poem1 = open('poem1.txt', 'r')
# [ ] review and run example: readlines breaks if file is no longer open

poem_lines = poem1.readlines()
print(poem_lines)
# output
# ['Loops I repeat\n', 'loops\n', 'loops\n', 'loops\n', 'I repeat\n', 'until I\n', 'break\n']
poem1.close()