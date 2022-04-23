
"""
Program Calculator
"""


class Calculator:
    """
    create class Calculator
    """
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sum_num(self, num1, num2):
        """

        A function that adds up two numbers.

        """
        self.num1 = num1
        self.num2 = num2

        return num1 + num2

    def multi(self, num1, num2):
        """

        A function that multiplies two numbers.

        """
        self.num1 = num1
        self.num2 = num2

        return num1 * num2

    def divine(self, num1, num2):
        """

        A function that divines two numbers.

        """
        self.num1 = num1
        self.num2 = num2

        try:  # Catch a error.
            return num1 / num2  # Divine two numbers.
        except ZeroDivisionError:  # Catch error division by zero.
            return "Division by zero!"

    def subtract(self, num1, num2):
        """
        A function that subtracts two numbers.

        """
        self.num1 = num1
        self.num2 = num2

        return num1 - num2


calc = Calculator(None, None)
print(calc.multi(4, 6))
print(calc.divine(10, 2))
print(calc.sum_num(100, 34))
