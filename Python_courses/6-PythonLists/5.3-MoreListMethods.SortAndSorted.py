#Concept
# .sort() and sorted()



# .sort() in place
# .sort() - orders a list in place

quiz_scores = [20, 19, 20, 15, 20, 20, 20, 18, 18, 18, 19]
print("quiz_scores:",quiz_scores)
# output
# quiz_scores: [20, 19, 20, 15, 20, 20, 20, 18, 18, 18, 19]
quiz_scores.sort()
print("in place sorted quiz_scores:",quiz_scores,"\n")
# output
# in place sorted quiz_scores: [15, 18, 18, 18, 19, 19, 20, 20, 20, 20, 20]

#sorted() - creates an ordered list copy
game_points = [3, 14, 0, 8, 21, 1, 3, 8]
sorted_points = sorted(game_points)
print("game_points:", game_points)
print("sorted_points:", sorted_points)
# output
# game_points: [3, 14, 0, 8, 21, 1, 3, 8]
# sorted_points: [0, 1, 3, 3, 8, 8, 14, 21]

print()


# sort STRINGS
# [ ] review and run example
cities_1 = ["Dubai", "Mexico City", "São Paulo", "Hyderabad"]

print("Unsorted", cities_1)
# ouput
# Unsorted ['Dubai', 'Mexico City', 'São Paulo', 'Hyderabad']
cities_1.sort()
print("Sorted", cities_1)
# ouput
# Sorted ['Dubai', 'Hyderabad', 'Mexico City', 'São Paulo']