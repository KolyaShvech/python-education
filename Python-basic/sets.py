
"""

Used the given lists to print out a set containing all the participants from event A which did not attend event B

"""

a = ["Jake", "John", "Eric"]
b = ["John", "Jill"]
"""
List "a" and list "b" converted into set
"""
a = set(a)
b = set(b)
"""
Get the value that are in set "a" and not in set "b" 
"""
print(set(a) - set(b))
