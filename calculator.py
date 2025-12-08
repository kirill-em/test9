import math

class Calculator:
    def add(self, a, b):
        """Возвращает сумму двух чисел."""
        return a + b

    def divide(self, a, b):
        """Возвращает результат деления a на b. При делении на 0 вызывает ошибку."""
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

    def is_prime_number(self, n):
        """Проверяет, является ли число простым."""
        if not isinstance(n, int):
            raise TypeError("Input must be an integer")
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True