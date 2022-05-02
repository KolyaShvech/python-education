def even_odd(x):
    """Checks number if it even or odd.

    Args:
        x (int): number to check.

    Returns:
        str: result of check. `even` if given number is even
            and `odd` if the number is odd.
    """
    if (x % 2 == 0):
        return "even"
    else:
        return "odd"


def sum_all(*numbers):
    """Sums all given numbers together.

    Args:
        *args (int or float): variable length argument list.


    Returns:
        int or float: the result of adding all numbers together.
    """
    result = 0
    for num in numbers:
        result += num
    return result
