# Use list methods .extend(), +, .reverse(), .sort()

# Concept
# Combine Lists
# + list addition
# .extend() list method


# combine lists with + and .extend()
visited_cities = ["New York", "Shanghai", "Munich", "Toyko", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
wish_cities = ["Reykjavík", "Moscow", "Beijing", "Lamu"]

# .extend() 
# extending visited_cities list (IN PLACE) by concatenating wish_cities
visited_cities.extend(wish_cities)
print("ALL CITIES",visited_cities,"\n")
# output:
# ALL CITIES ['New York', 'Shanghai', 'Munich', 'Toyko', 'Dubai', 'Mexico City', 'São Paulo', 'Hyderabad', 'Reykjavík', 'Moscow', 'Beijing', 'Lamu']

# (+) Addition operator for lists creates a (NEW) combined List
all_cities = visited_cities + wish_cities
print("ALL CITIES")
for city in all_cities:
    print(city)
# ouput 
# ALL CITIES
# New York
# Shanghai
# Munich
# Toyko
# Dubai
# Mexico City
# São Paulo
# Hyderabad
# Reykjavík
# Moscow
# Beijing
# Lamu
# Reykjavík
# Moscow
# Beijing
# Lamu  

print()
    
# [ ] review and run example
team_a = [0,2,2,2,4,4,4,5,6,6,6]
team_b = [0,0,0,1,1,2,3,3,3,6,8]
print("Team A:", team_a, "\nTeam B:",team_b)
# output
# Team A: [0, 2, 2, 2, 4, 4, 4, 5, 6, 6, 6]
# Team B: [0, 0, 0, 1, 1, 2, 3, 3, 3, 6, 8]
print()

# (+) Addition operator 
team_totals = team_a + team_b
print("Team Totals", team_totals)
# output
# Team Totals [0, 2, 2, 2, 4, 4, 4, 5, 6, 6, 6, 0, 0, 0, 1, 1, 2, 3, 3, 3, 6, 8]
print()

# .extend() 
team_a.extend(team_b)
print("Team_a extended", team_a)
# ouput
# Team_a extended [0, 2, 2, 2, 4, 4, 4, 5, 6, 6, 6, 0, 0, 0, 1, 1, 2, 3, 3, 3, 6, 8]
print()
