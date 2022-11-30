num1 = 0
num2 = 0


def init_complex(a, b:complex):  # начало
    global num1
    global num2
    num1 = a
    num2 = b


def sum_complex(a, b:complex):  # сложение
    return a + b


def difference_complex(a, b:complex):  # вычетание
    return a - b


def mult_complex(a, b:complex):  # умножение
    return a * b


def division_complex(a, b:complex):  # деление
    return a / b