"""
implemented class Product iterator.
"""


class Product:
    """
    Create class Product.
    """

    def __init__(self, *args, **kwargs):
        self._result = iter(self._get_result(args, kwargs))

    @staticmethod
    def _get_result(args, kwargs):
        pools = list(map(tuple, args)) * kwargs.get('repeat', 1)
        result = [[]]
        for pool in pools:
            result = [x + [y] for x in result for y in pool]
        return result

    def __iter__(self):
        return self

    def __next__(self):
        return tuple(next(self._result))


print(list(Product([1, 2], 'ac', {4, 5})))
