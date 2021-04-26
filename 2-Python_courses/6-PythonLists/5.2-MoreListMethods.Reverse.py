# .reverse() : 
# reverse a list in place

cities_1 = ["Dubai", "Mexico City", "São Paulo", "Hyderabad"]

#Examples
print("regular", cities_1)
# output 
# regular ['Dubai', 'Mexico City', 'São Paulo', 'Hyderabad']

cities_1.reverse()
print("reversed", cities_1)
# output 
# reversed ['Hyderabad', 'São Paulo', 'Mexico City', 'Dubai']

print()


# [ ] review and run example
all_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("regular list",all_num, "\n")
# output 
# regular list [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
all_num.reverse()
print("reverse list",all_num, "\n")
# output 
# reverse list [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

num_len = len(all_num)
print("Three Multiple")
for num in all_num:
    if num/3 == int(num/3):
        print(num)
    else:
        pass
# output 
# Three Multiple
# 90
# 60
# 30
# 9
# 6
# 3
# 0

    
# create a list of  numbers by casting a range 
count_list = list(range(21))
print("before list", count_list)
# output 
# before list [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# and reverse
count_list.reverse()
print("after list", count_list)
# output
# after list [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
