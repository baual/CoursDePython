medicine = 'Coughussin'
dosage = 5
duration = 4.5

instructions = '{} - Take {} ML by mouth every {} hours'.format(medicine, dosage, duration)
#remplace les accolades dans l'ordre des paramètres
print(instructions)

instructions = '{2} - Take {1} ML by mouth every {0} hours'.format(medicine, dosage, duration)
#remplace les accolades dans l'ordre des POSITIONS des paramètres - {2} = dosage etc...
print(instructions)

instructions = '{medicine} - Take {dosage} ML by mouth every {duration} hours'.format(medicine = 'Sneezergen', dosage = 10, duration = 6)
#remplace les {VARIABLES} par leur valeur définie dans la fonction format()
print(instructions)

#output
#Coughussin - Take 5 ML by mouth every 4.5 hours
#4.5 - Take 5 ML by mouth every Coughussin hours
#Sneezergen - Take 10 ML by mouth every 6 hours


print()


#formatted strings literal : 
name = 'World'
message = f'Hello, {name}.' #use formatted string literals, also known as f-strings
print(message)
#output : Hello, World.

count = 10
value = 3.14
message = f'Count to {count}.  Multiply by {value}.'
print(message)
#output : Count to 10.  Multiply by 3.14.

width = 5
height = 10
print(f'The perimeter is {(2 * width) + (2 * height)} and the area is {width * height}.')
#output : The perimeter is 30 and the area is 50. calculatiosn occured between the {}
print()


# Format string literal replacement fields have a special format specifier syntax 
# that is almost a mini-programming language unto itself. We'll merely scratch the 
# surface of what's possible in this step of the exercise. You can use the format specifier 
# syntax to format numbers, dates, time, percentages, and exponents.
value = 'hi'

print(f'.{value:<25}.')
print(f'.{value:>25}.')
print(f'.{value:^25}.')
print(f'.{value:-^25}.')

#A format specifier uses a colon symbol (:) after the variable name, to specify how that value should be formatted.
#In the first f-string, we use the less-than symbol (<) to align the text to the left of a string that is 25 total 
# characters wide. The string hi occupies two of the 25 total characters. We add period symbols (.) on the left 
# and right of the replacement field, to help us see the total width of the string.
#In the second f-string, we use the greater-than symbol (>) to align the text to the right of a string
#  that is 25 total characters wide.
#In the third f-string, we use the caret symbol (^) to center the text in the middle of a string that is 25 total characters wide.
#In the fourth f-string, we use the caret symbol (^) again. But this time, we preface it with a single dash symbol (-) 
# to use instead of an empty space to fill the remaining width of the string.
#When you run the code, you should see the following output:
#.hi                       .
#.                       hi.
#.           hi            .
#.-----------hi------------.

