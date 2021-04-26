first_value = 5
second_value = 4

sum = first_value + second_value
difference = first_value - second_value
product = first_value * second_value
quotient = first_value / second_value
modulus = first_value % second_value
exponent = first_value ** second_value 

print('Sum: ' + str(sum))
print('Difference: ' + str(difference))
print('Product: ' + str(product))
print('Quotient: ' + str(quotient))
print('Modulus: ' + str(modulus))
print('Exponent: ' + str(exponent))
print()

#Python follows the PEMDAS acronym, which indicates the order in which the operations should be performed.
#Parentheses: Resolve operations between parentheses first.
#Exponents: Resolve exponents.
#Multiplication: Perform multiplication, from left to right.
#Division: Perform division, from left to right.
#Addition: Perform addition, from left to right.
#Subtraction: Perform subtraction, from left to right.


#When you perform division, you provide a dividend and a divisor. If these are values are of an int data type,
#  they will implicitly result in a quotient of type float.
first_value = 5
second_value = 4
quotient = first_value / second_value
print(type(quotient))
print(quotient)

print()

#float into int
pi = 3.14
print(type(pi))
print(int(pi))  #output will be 3
print(round(pi))    #ouput: 3

uptime = 99.99
print(type(uptime))
print(int(uptime))  #output will be 9
print(round(uptime))    #output:100
print()

first_value = round(7.654321, 2) #round with 2 decimals
print(first_value)
second_value = round(9.87654, 3)    #round with 3 decimals
print(second_value)


