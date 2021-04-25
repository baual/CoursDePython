colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'brown']






# de dernier au premier on réordonne la liste
colors.reverse()
print(colors)
# output
# ['brown', 'purple', 'orange', 'yellow', 'blue', 'green', 'red']

# on trie la liste et en fonction du type 
colors.sort()
print(colors)
# output
# ['blue', 'brown', 'green', 'orange', 'purple', 'red', 'yellow']

print()








#treat list like a queue
# A pop operation removes an item from the queue for processing. You
#  can remove an item from the beginning of the list ("first in, first out", or FIFO).
#  Or you can remove an item from the end of the list ("last in, first out", or LIFO).

print(colors)
# output
# ['blue', 'brown', 'green', 'orange', 'purple', 'red', 'yellow']

color = colors.pop(0)
print('popped', color)
# out 'blue'

print(colors)
# output
# ['brown', 'green', 'orange', 'purple', 'red', 'yellow']


print()


#Add and remove elements from a list
print(colors)

#ajoute black and white à la fin
colors.append('black')
colors.append('white')

#enleve 'yellow' and 'orange'
colors.remove('yellow')
colors.remove('orange')

print(colors)
# output
# ['brown', 'green', 'purple', 'red', 'black', 'white']

#colors.remove('whatever')
# output
# ValueError: list.remove(x): x not in list

print()




#Combine a new list with an existing list
new_colors = ['lime', 'gray']
colors.extend(new_colors)
print(colors)

# output
# ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'brown']
# ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'brown', 'lime', 'gray']

print()

#Clear all items from a list
colors.clear()
print(colors)

# ouput
# []


#2comparaison methods:*
foot_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", 
            "intermediate cuneiform", "medial cuneiform"]
# [ ] review and run example of sorting into strings to display
longer_names = ""
shorter_names = ""

for bone_name in foot_bones:
    if len(bone_name) < 10:
        shorter_names += "\n" + bone_name
    else:
        longer_names += "\n" + bone_name

print(shorter_names)
print(longer_names)

# [ ] review and run example of sorting into lists
longer_names = []
shorter_names = []

for bone_name in foot_bones:
    if len(bone_name) < 10:
        shorter_names.append(bone_name)
    else:
        longer_names.append(bone_name)

print(shorter_names)
print(longer_names)