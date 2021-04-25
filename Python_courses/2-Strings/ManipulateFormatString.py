first_value = '  FIRST challenge         '
second_value = '-  second challenge  -'
third_value = 'tH IR D-C HALLE NGE'

fourth_value = 'fourth'
fifth_value = 'fifth'
sixth_value = 'sixth'

#challenge output
#       First Challenge        
#Second challenge
#               Third challenge
#fourth#fifth#sixth!
#        fourth
#        fifth
#        sixth




# First challenge
print(first_value.lower().title())

# Second challenge
temp=second_value.replace('-','')
temp=temp.strip()
print(temp.capitalize())


# Third challenge
third_value=third_value.replace(' ','')
third_value=third_value.replace('-',' ')
third_value=third_value.swapcase()
print(f'{third_value:>25}')


print()
#print(first_value)
#print(second_value)
#print(third_value)
print()

# Fourth challenge - use only the print() function (no f-strings)
print(fourth_value+'#'+fifth_value+'#'+sixth_value+'!')
#autre soluce: print(fourth_value, fifth_value, sixth_value, sep='#', end='!')

# Fifth challenge - use only a single print() function.  Create tabs and new lines using f-strings.
print('\t{}\n\t{}\n\t{}\n'.format(fourth_value, fifth_value, sixth_value))
#autre soluce: print(f'\n\t{fourth_value}\n\t{fifth_value}\n\t{sixth_value}')
