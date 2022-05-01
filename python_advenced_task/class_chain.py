"""
Implementing program Chain in class.
"""


class Chain:
    """
    Create class Chain.
    """
    def __init__(self, *args):
        self._iterables = iter(args)
        self._element = iter(next(self._iterables))

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = next(self._element)
        except StopIteration:
            self._element = iter(next(self._iterables))
            item = next(self._element)

        return item


chain = Chain("honor", [7, 8, 2, 5], ["queen", "king", "lord"])
print(list(chain))
