#Using the techniques we learned in this module, generate a random number between 1 and 5
#  and allow the user to guess. Keep prompting the user for their guess until they guess correctly.
#  Then, display the number of guesses.
#No matter how you do it, your code should produce similar results to the following output
#  (given the randomly generated answer and guesses):
# 
# Guess a number between 1 and 5: 3
# Guess a number between 1 and 5: 4
# You guessed it in 2 tries!


import random

roll = random.randint(1, 5)
count = 0
guess = 0

while roll != guess:
  count += 1
  guess = input('Guess a number between 1 and 5:' )
  if guess.isnumeric():
      guess = int(guess)

else:
    print(f'You guessed it in {count} times.')
