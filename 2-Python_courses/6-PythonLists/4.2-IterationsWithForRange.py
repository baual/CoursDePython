#range(stop)
#The range(stop) function creates a sequence
#using 1 argument with range(stop)

#default start: 0
#stop: stopping integer, does not process stop number
for count in range(10):
  print(count)
#same as
for count in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
  print(count)
#range runs from 0 through the integer before stop!!!!!!
#range(10) means 10 values starting from 0 to 9 included

print()

# review and run example
digits = range(10)
print("digits =", list(digits), "\n")
#output: digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for count in digits:
    print(count)
# output:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9


print()

sub_total = 0
for item in range(10):
    sub_total += item
    print("sub_total:", sub_total)
print("Total =", sub_total)
#output


print()


# print the first half of a spelling list
spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]

# find length of 1st half of list (must be int)
# find length list 
spell_len = len(spell_list)
half_1 = int(spell_len/2)

for word in range(half_1):
    print(spell_list[word])
# output
# Tuesday
# Wednesday
# February

print()

#range(start,stop)
#The range(start,stop) function creates a sequence
#using 2 arguments with range(start,stop)

#start: starting integer value of a range loop
#stop: stopping integer (second argument), does not process stop number
for count in range(5,10):
  print(count)
# output:
# 5
# 6
# 7
# 8
# 9
print()

#Example from spell list 
# spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]
# print 2nd half list
for word in range(half_1,spell_len):
    print(spell_list[word])
# output
# November
# Annual
# Calendar
# Solstice

print()

#range(start,stop,step)
#The range(start,stop,step) function creates a sequence
#using 3 arguments with range(start,stop,step)

#start: starting integer value of a range loop
#stop: stopping integer (second argument), does not process stop number
#step: skip value for each loop
for count in range(10,101,10):
  print(count)
# output
# 10
# 20
# 30
# 40
# 50
# 60
# 70
# 80
# 90
# 100

print()

# [ ] review and run example
sub_total = 0
temp = 0
for item in range(25,46,5):
    temp = sub_total
    sub_total += item
    print("sub_total:", temp, "+", item, "=",sub_total)
print("Total =", sub_total)
# output 
# sub_total: 0 + 25 = 25
# sub_total: 25 + 30 = 55
# sub_total: 55 + 35 = 90
# sub_total: 90 + 40 = 130
# sub_total: 130 + 45 = 175
# Total = 175

print()

# [ ] review and run example printing the 1st and then every other word in spell_list
# spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]
for index in range(0,spell_len,2):
    print(spell_list[index])
# output
# Tuesday
# February
# Annual
# Solstice

print()

# [ ] review and run example casting range to list
odd_list = list(range(1,20,2))
print(odd_list)
# output 
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

print()

