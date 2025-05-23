import app
import math

class InvalidPermissions(Exception):
    pass


class Calculator:
    def add(self, x, y):
        self.check_types(x, y)
        return x + y

    def substract(self, x, y):
        self.check_types(x, y)
        return x - y

    def multiply(self, x, y):
        if not app.util.validate_permissions(f"{x} * {y}", "user1"):
            raise InvalidPermissions('User has no permissions')

        self.check_types(x, y)
        return x * y

    def divide(self, x, y):
        self.check_types(x, y)
        if y == 0:
            raise TypeError("Division by zero is not possible")

        return x / y

    def power(self, x, y):
        self.check_types(x, y)
        return x ** y
# NUEVO
    def sqrt(self, x):
        if not isinstance(x, (int, float)):
            raise TypeError("Parameter must be a number")
        if x < 0:
            raise TypeError("Cannot compute square root of negative number")
        return math.sqrt(x)

    def log10(self, x):
        if not isinstance(x, (int, float)):
            raise TypeError("Parameter must be a number")
        if x <= 0:
            raise TypeError("Cannot compute log10 of non-positive number")
        return math.log10(x)
# NUEVO
    def check_types(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Parameters must be numbers")


# if __name__ == "__main__":  # pragma: no cover
#     calc = Calculator()
#     result = calc.add(2, 2)
#     print(result)

if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    calc = Calculator()
    result = calc.add(2, 2)
    print("Suma:", calc.add(2, 2))
    print(result)
    print("Raíz:", calc.sqrt(16))
    print("Log:", calc.log10(100))
