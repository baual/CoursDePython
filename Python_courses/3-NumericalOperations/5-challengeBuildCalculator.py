#output
#Simple calculator!
#First number? 4
#Operation? *
#Second number? 5
#product of 4 * 5 equals 20

print('simple calculator!')
FirstNumber=input('First Number?')
operation=input('Operator?')
SecondNumber=input('Second Number?')
if FirstNumber.isnumeric() :
    FirstNumber=int(FirstNumber)
    if SecondNumber.isnumeric:
        SecondNumber=int(SecondNumber)
    else:
        print('not a valut goodbye')
else:
    print('not a valut goodbye')
    
    
result = 0
if operation == '+':
    result = FirstNumber + SecondNumber
    label = 'sum'
elif operation == '-':
    result = FirstNumber - SecondNumber
    label = 'difference'
elif operation == '*':
    result = FirstNumber * SecondNumber
    label = 'product'
elif operation == '/':
    result = FirstNumber / SecondNumber
    label = 'quotient'
elif operation == '**':
    result = FirstNumber ** SecondNumber
    label = 'exponent'
elif operation == '%':
    result = FirstNumber % SecondNumber
    label = 'modulus'
else:
    print('Operation not recognized.')
    exit()

print(label + ' of ' + str(FirstNumber) + ' ' + operation + ' ' + str(SecondNumber) + ' equals ' + str(result))