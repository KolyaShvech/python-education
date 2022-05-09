"""
Implement recursion factorial.
"""


def recursion_factorial(num: int):
    """
    Create func recursion_factorial.
    """

    if (num == 1) or (num == 0):
        return 1
    else:
        return (num * recursion_factorial(num - 1))


num = 10

print(recursion_factorial(num))
