import types

# Write a generator function which returns the Fibonacci series

def fibe(n):
    a, b = 1, 2
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fibe(n=15)))

# will simultaneously switch the values of a and b.

def fib():
    """
    Create function Fibonacci series.
    """
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, a + b



if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    COUNTER = 0
    for s in fib():
        print(s)
        COUNTER += 1
        if COUNTER == 10:
            break

# _________________-----------------------__________________________
# Using a list comprehension, create a new list called "new_list" out of the list "numbers",
# which contains only the positive numbers from the list, as integers.

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
new_list = [int(num) for num in numbers if num > 0]
print(new_list)



# _____________________________________________________________________________

# Handle all the exception! Think back to the previous lessons to return the last name of the actor.

actor = {"name": "John Cleese", "rank": "awesome"}

# Function to modify!!!
def get_last_name():
    """
    Create function get_last_name.
    """
    return actor["name"].split()

# Test code
get_last_name()
print("All exceptions caught! Good job!")
print(f"The actor's last name is {get_last_name()}")
