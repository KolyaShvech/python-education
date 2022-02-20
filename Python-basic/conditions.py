
"""
Change the variables so that each if statement resolves as True
"""

number = 10
second_number = 10
first_array = []
second_array = [1, 2, 3]

if number < 15:
    print("1", True)

if not first_array:
    print("2", True)

if len(second_array) == 3:
    print("3", True)

if len(first_array) + len(second_array) == 3:
    print("4", True)

if second_array and second_array[0] == 1:
    print("5", True)

if second_number:
    print("6", True)