# More Python string tools (tricks?)
# Cast a string to a list of characters

# hello_letters = list("Hello")
# print to the same line with multiple print statements (end=)
# or insert any character as an end in print("String", end="+")

print('Hello', end = '')
print('world')
# output
# Helloworld

print('Hello', end = ' ')
print('world')
# output
# Hello world


# Examples
# on "transforme" une chaine de caractères en une liste!
hello_letters = list("Hello")
print(hello_letters)
# output
# ['H', 'e', 'l', 'l', 'o']

# cast string to list
word_letters = list("concatenates")

# .join() concatenates the list
# print on same line setting the end character
print('~'.join(word_letters))
# output
# c~o~n~c~a~t~e~n~a~t~e~s

# This  is the default print end
print("Hello World!", end="\n")
print('still something to learn about print()')
# output
# Hello World!
# still something to learn about print()

# end inserts any valid str character: A-z, 0-9,!,@,*,\n,\t or ''(empty string)...
for letter in "Concatenation":
    print(letter, end='*')
# output
# C*o*n*c*a*t*e*n*a*t*i*o*n*
#ci-dessous pareil sauf que pas de retour à la ligne depuis print précédent.
print('*'.join("Concatenation"))
# output
# C*o*n*c*a*t*e*n*a*t*i*o*n*