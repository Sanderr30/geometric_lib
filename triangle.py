def area(a, b, c):
    """Вычисляет площадь треугольника по формуле Герона.

    Args:
        a (float): Длина первой стороны треугольника.
        b (float): Длина второй стороны треугольника.
        c (float): Длина третьей стороны треугольника.

    Returns:
        float: Полупериметр треугольника.
    """
    return (a + b + c) / 2


def perimeter(a, b, c):
    """Вычисляет периметр треугольника.

    Args:
        a (float): Длина первой стороны треугольника.
        b (float): Длина второй стороны треугольника.
        c (float): Длина третьей стороны треугольника.

    Returns:
        float: Периметр треугольника.
    """
    return a + b + c