#function definition
#definition need to be done before the call of the function
def say_hello():
      print('Hello World!')

#function called
say_hello()

print()

#funtion with argument
def say_hello(name):
      print(f'Hello {name}!')
#that function will 'print' Hello Bob!
#if no argument then an error will appear : TypeError: say_hello() missing 1 required positional argument: 'name'
say_hello('Bob')

print()

#deafult value of name is 'World'
def say_hello(name='World'):
      print(f'Hello {name}!')

say_hello()     #default value used so "hello World!"" will be print
say_hello('Bob')



print()

#multiple arguments with default values
def say_hello(name='World', greeting=None): #none is a type by itself : <class 'NoneType'>
      if greeting == None:
          print(f'Hello {name}!')
      else:
          print(f'{greeting} {name}!')

say_hello()                     # Hello World!
say_hello('Bob')                # Hello Bob!
say_hello(greeting='Howdy')     # Howdy World!
say_hello('Bob', 'Howdy')       # Howdy Bob!

print()


#function with return 
def add_two_numbers(x, y):
    return x + y

add_two_numbers(4, 6)
result = add_two_numbers(5, 7)
print(result)
#x+Y has been returned

print()

#function will return a list 
def create_deck():
    suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    deck = []
      
    for suit in suits:
      for rank in ranks:
        deck.append(f'{rank} of {suit}')
            
    return deck

my_deck = create_deck()
print(len(my_deck))
# output : 52

print()

# won't work because value is only known into the function 
# not visible outside the block so not when you call it
#def some_function():
#    value = 10
#print(value)

#on other hand a variabkle define outside a function is not know into the function
value = 1

def some_function():
    value = 10
    return value

print(value)    # output : 1
some_function() 
print(value)    # output : 1 because the valur into the main block is not the same of the one into the function !!!!

