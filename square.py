def area(a):
    if a < 0:
        raise ValueError("Value of square sides can not be below 0")
    return a * a


def perimeter(a):
    if a < 0:
        raise ValueError("Value of square sides can not be below 0")
    return 4 * a