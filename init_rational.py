x = 0
y = 0


def init_rational(a, b: float):  # начало
    global x
    global y
    x = a
    y = b


def sum_rational(a, b: float):  # сложение
    return round(a + b, 4)


def difference_rational(a, b: float):  # вычетание
    return round(a - b, 4)


def mult_rational(a, b: float):  # умножение
    return round(a * b, 4)


def division_rational(a, b):  # деление
    return round(a / b, 4)
