numbers = [1, 3, 5]

print(5 in numbers)         #output : True
print(8 in numbers)         #output : False

print(5 not in numbers)     #output : False
print(8 not in numbers)     #output : True

print()

#loop for a list
cities = ["Chicago", "London", "Tokyo"]

for city in cities:
  print(city)
  
print()
  
# Break out of a for loop
numbers = [42, 77, 16, 101, 23, 8, 4, 15, 55]
numbers.sort()

for number in numbers:
  if number > 42:
    break # voila on sort des que number est supérieur à 42
  print(number)
# number est défini dans le  for  
# output
# 4
# 8
# 15
# 16
# 23
# 42


print()


#avec else
import random
numbers = []


#on génère la liste avec 5 nombres aléatoires de 1 à 100
while len(numbers) < 5:
  numbers.append(random.randint(1, 100))

for number in numbers:
  print(number)
  if number >= 90:
    print('Found at least one number greater than 90')
    break
else:
  print('No numbers greater than 90')

print('Complete')
# output
# 49
# 99
# Found at least one number greater than 90 : ON A DU BOL AVEC LE RANDOM :-)
# Complete

print()

#avec continue
values = ["laptop", 7, "phone", 3, "dslr", 5]
equipment = []

for value in values:
  if isinstance(value, str) == False:
    continue    #on zappe la fin du for pour entrer dans une novelle itération donc on ajoute pas les 'int' à la liste
  equipment.append(value)

print(equipment)
# output
# ['laptop', 'phone', 'dslr']

print()

#Create nested 'for' loops
suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

for  suit in suits:
  for rank in ranks:
    print(f'{rank} of {suit}')
    
# output
# ben la liste est longue ......

print()








#Choose randomly from a list
import random

numbers = [42, 77, 16, 101, 23, 8, 4, 15, 55]

#on en veut 1
selected_number = random.choice(numbers)
print(selected_number)

# on en veut 3
selected_numbers = random.choices(numbers, k=3)
print(selected_numbers)

