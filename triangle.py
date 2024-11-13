import math


def area(a, b, c):
    # Проверка на неотрицательные значения
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Value of triangle sides can not be below 0")
    # Проверка на неравенство треугольника
    if not (a + b > c and a + c > b and b + c > a):
        raise ValueError("Value of this sides can not make triangle")

    # Формула Герона
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def perimeter(a, b, c):
    # Проверка на неотрицательные значения
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Value of triangle sides can not be below 0")
    # Проверка на неравенство треугольника
    if not (a + b > c and a + c > b and b + c > a):
        raise ValueError("Value of this sides can not make triangle")

    return a + b + c
