# Concept
# Converting a string to a list with .split()
# .split() by default, splits a string at spaces (" ") to create a list


# Examples

tip = "Notebooks can be exported as .pdf"
tip_words = tip.split()
print("STRING:", tip)
# ouput
# STRING:Notebooks can be exported as .pdf
print("LIST:", tip_words, "\n")
# ouput
# LIST: ['Notebooks', 'can', 'be', 'exported', 'as', '.pdf']

for word in tip_words:
    print(word)
# ouput
# Notebooks
# can
# be
# exported
# as
# .pdf   
    

# [ ] review and run example
rhyme = "London bridge is falling down"
rhyme_words = rhyme.split()
rhyme_words.reverse()
for word in rhyme_words:
    print(word)
# ouput :
# down
# falling
# is
# bridge
# London

print("\n\n\n\n")

# .split('-')
# to split on characters other than " " (space), provide .split() a string argument to use as break points

# Examples
# .split('-') : split with an argument
code_tip = "Python-uses-spaces-for-indentation"
tip_words = code_tip.split('-')
print(tip_words)
# output
# ['Python', 'uses', 'spaces', 'for', 'indentation']

code_tip = "Python uses spaces for indentation"
# split on "a"
tip_words = code_tip.split('a')
print(code_tip)
# output
# Python uses spaces for indentation
print(tip_words)
# output
# ['Python uses sp', 'ces for indent', 'tion']

print()

# triple quotes ''' ''' preserve formatting such as spaces and line breaks
big_quote = """Jack and Jill went up the hill
To fetch a pail of water
Jack fell down and broke his crown
And Jill came tumbling after"""

# split on line breaks (\n)
quote_lines = big_quote.split('\n')
print(quote_lines, '\n')
# output 
# ['Jack and Jill went up the hill', 'To fetch a pail of water', 'Jack fell down and broke his crown', 'And Jill came tumbling after']

# print the list in reverse with index slicing
for line in quote_lines[::-1]:
    print(line)
# output = les lignes ont été inversées !!!
# And Jill came tumbling after
# Jack fell down and broke his crown
# To fetch a pail of water
# Jack and Jill went up the hill