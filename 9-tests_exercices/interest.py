print('Interest Calculator:')

amount = float(input('Principal amount ?'))
roi = float(input('Rate of Interest ?'))
yrs = int(input('Duration (no. of years) ?'))

total = (amount * pow(1 + (roi/100), yrs))
#pow(x,y) means x to the power y. here = 1+(roi/100) power the number of years
interest = total - amount
print('\nInterest = % f' %interest)
#%f' %interest permits to concatenate string and float
print('\nInterest = %0.2f' % interest)
#%0.2f means I guess a 2 digit after comma for the float
#%0.4f if you want get 4 digits !
#Go there to know about format specification https://docs.python.org/3.8/library/string.html#formatspec
