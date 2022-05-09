"""
Implement quick sort.
"""


def quick_sort(arr):
    """
    Create func quick sort.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]  # sorts the elements to the left of pivot
    middle = [x for x in arr if x == pivot]  # the elements in middle equel pivot.
    right = [x for x in arr if x > pivot]  # # sorts the elements to the right of pivot
    return quick_sort(left) + middle + quick_sort(right)


array = [4, 1, 8, 6, 2, 3, 0, 9, 4, 6]
print(quick_sort(array))
