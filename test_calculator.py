# test_calculator.py
import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

# 1 & 2. Тестирование метода add с параметризацией
@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 15),       # Положительные числа
    (-1, 1, 0),        # Отрицательное и положительное
    (-5, -5, -10),     # Отрицательные числа
    (0, 0, 0),         # Нули
    (2.5, 3.5, 6.0)    # Дробные числа
])
def test_add(calc, a, b, expected):
    assert calc.add(a, b) == expected

# 1 & 2. Тестирование метода divide с параметризацией (успешные кейсы)
@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (5, 2, 2.5),
    (-10, 2, -5),
    (0, 5, 0)
])
def test_divide(calc, a, b, expected):
    assert calc.divide(a, b) == expected

# 3. Проверка возникновения исключения при делении на ноль
def test_divide_by_zero(calc):
    with pytest.raises(ZeroDivisionError):
        calc.divide(10, 0)

# 1 & 2. Тестирование метода is_prime_number с параметризацией
@pytest.mark.parametrize("n, expected", [
    (1, False),        # 1 не является простым
    (0, False),        # 0 не является простым
    (-5, False),       # Отрицательные не являются простыми
    (2, True),         # 2 - самое маленькое простое число
    (3, True),
    (4, False),        # Четное число
    (17, True),        # Простое число
    (20, False)        # Составное число
])
def test_is_prime_number(calc, n, expected):
    assert calc.is_prime_number(n) == expected