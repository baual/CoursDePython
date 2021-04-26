#Using the techniques we learned in this module, generate a random number between 1 and 5
#  and allow the user to guess. Keep prompting the user for their guess until they guess correctly.
#  Then, display the number of guesses.
#No matter how you do it, your code should produce similar results to the following output
#  (given the randomly generated answer and guesses):
# 
#Guess a number between 1 and 10
#Enter guess #1: 5
#Your guess is too low, try again!
#Enter guess #2: 8
#Your guess is too high, try again!
#Enter guess #3: 7
#Your guess is too high, try again!
#Enter guess #4: 6
#You guessed it in 4 tries!


import random

roll = random.randint(1, 5)
count = 0
guess = 0

print('Guess a number between 1 and 10')

while roll != guess:
  count += 1
  guess = input(f'Enter guess {count}:' )
  if guess.isnumeric():
      guess = int(guess)
      if guess < roll:
              print('Your guess is to low, try again')
      elif guess > roll:
              print('Your guess is to high, try again')          

else:
    print(f'You guessed it in {count} times.')
