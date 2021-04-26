import random 

roll = 0
count = 0

print('First person to roll a 5 wins!')
while roll != 5:
  
  name = input('Enter a name, or \'q\' to quit:  ' ) #Enter a name, or 'q' to quit:          \' means '
  if name == 'q':
    break               #break:on sort de la boucle "violemment"
  
  count = count + 1
  roll = random.randint(1, 5)
  print(f'{name} rolled {roll}')
else:
    print(f'{name} Wins!!!')        #si roll==5 lors print....

print(f'You rolled the dice {count} times.')