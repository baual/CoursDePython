#usage de base
import random
roll1=random.randint(1,10)
print(f'You rolled {roll1}.')

print()

#import avec un alias
import random as alias
roll2=alias.randint(1,10)

print(f'You rolled {roll2}.')

print()

#import avec un alias nommé autrement
import random as baba
roll3=baba.randint(1,10)

print(f'You rolled {roll3}.')