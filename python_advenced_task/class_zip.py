"""
Implementing program Zip in class.
"""


class Zip:
    """
    Create class Zip.
    """
    def __init__(self, *args):
        self._iterables = [iter(item) for item in args]

    def __iter__(self):
        return self

    def __next__(self):
        return tuple([next(iter_obj) for iter_obj in self._iterables])


list_zip = Zip(["doom", "peace", "love"], [4, 6, 7, 8])
print(list(list_zip))
