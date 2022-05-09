"""
Implement binary search and how it works.
"""


def binary_search(array, item):
    """
    Create finc binary_search with parameters array and item.
    """
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = (left + right) // 2
        if array[middle] == item:
            return middle
        elif array[middle] < item:
            left = middle + 1
        else:
            right = middle - 1

    return -1


print(binary_search([5, 6, 10, 8], 2))
print(binary_search([5, 6, 10, 8], 6))
print(binary_search([7, 1, 2, 5, 9, 3], 5))



