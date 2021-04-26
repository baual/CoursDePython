#celsius = (fahrenheit - 32) * 5/9

#ouput
#What is the temperature in fahrenheit?  55
#Temperature in celsius is 12

#input not numical:
#output:Input is not a number.


Faren = input('What is the temperature in fahrenheit? ')

if Faren.isnumeric() == False:
    print('Value is not a number.')
    exit()
    
Faren=int(Faren)
Celsius=round((Faren-32)*(5/9), 3)

print('Temperature in celsius is ' + str(Celsius))
