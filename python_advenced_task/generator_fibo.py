"""
Create program generator Fibonacci numbers.
"""


def fib(n):

    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield b

x = fib(10)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))



