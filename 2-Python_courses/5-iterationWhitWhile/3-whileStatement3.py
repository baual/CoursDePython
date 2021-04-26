import random 

roll = 0
count = 0

print('First person to roll a 5 wins!')
while roll != 5:
  name = input('Enter a name, or \'q\' to quit:  ' )

  if name.strip() == '': #strip pour enlever les espaces au cas ou
    continue

  if name.strip() == 'q':
    break  #retourne au début de la boucle sans exécuter le reste tant que pas de nom ou q de renseigner
  
  count = count + 1
  roll = random.randint(1, 5)
  print(f'{name} rolled {roll}')
else:
    print(f'{name} Wins!!!')

print(f'You rolled the dice {count} times.')


#recap
#The while statement allows you to create a looping structure that continues to loop through a code
#  block until a Boolean expression evaluates to False.
#Add the break statement to exit out of a code block prematurely before the
#  Boolean expression evaluates to False.
#Add the else statement to provide a second code block that runs after the while statement's
#  Boolean expression evaluates to False.
#Add the continue statement to skip over the remainder of the code block and set the execution
#  path back to the Boolean expression.