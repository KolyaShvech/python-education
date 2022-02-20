
"""
Create two lists with 10 instances of the variables x and y. Create a list called big_list,
which contains the variables x and y, 10 times each
"""

x = 5
y = 6
x_list = [x] * 10
y_list = [y] * 10

big_list = x_list + y_list

print(f"\nx-list:{x_list} \ny-list:{y_list} \nbig-list:{big_list}")
