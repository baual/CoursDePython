import processor

my_list = [5, 'Dan', '4', 7, 'Steve', 'Amy', 'Rhonda', 4, '9', 'Jill', 7, 'Kim']
my_bad_list = 5

numbers = processor.process_numbers(my_list)
print(numbers)

names = processor.process_names(my_list)
print(names)

numbers = processor.process_numbers(my_bad_list)
print(numbers)

names = processor.process_names(my_bad_list)
print(names)


# Rule 1: You can't modify the code in the challenge.py file at all. Instead,
#  create a new module named processor.py in the same working folder.

# Rule 2: After you finish, running the challenge.py file must produce the following output:
# [4, 4, 5, 7, 7, 9]
# ['Amy', 'Dan', 'Jill', 'Kim', 'Rhonda', 'Steve']
# []
# []

# Rule 3: The process_numbers() function must select all numeric values, even those values
#  that are strings, and return them as a list. The values must be converted to numbers and
#  included in the returned list. The list must be sorted. The function must handle the
#  possibility that the input parameter isn't formatted as a list. In that case, it must return an empty list.

# Rule 4: The process_names() function must select all string values that aren't numeric
#  and return them as a list. The list must be sorted. The function must handle the
#  possibility that the input parameter isn't formatted as a list. In that case, it must return an empty list.