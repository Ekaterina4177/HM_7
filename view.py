def print_start():
    print('Калькулятор')


def type_number():
    while True:
        type = input(
            'Выберите тип чисел: \n1. Рациональные \n2. Комплексные \n0. Завершить \n> ')
        if type == '1':
            return 1
        if type == '2':
            return 2
        if type == '0':
            return 0
        else:
            print('Вы ввели неккореткное значение типа данных. Повторите ввод.')
            continue


def entering_number_rational():
    number1 = float(input('Введите первое число: '))
    number2 = float(input('Введите второе число: '))
    return number1, number2


def entering_number_complex():
    number1 = complex(input('Введите первое число: '))
    number2 = complex(input('Введите второе число: '))
    return number1, number2


def get_menu():
    while True:
        operation = input('Выберите тип операции: \n1. Сложение \n2. Вычетание \n3. Умножение \n4. Деление \n0. Завершить \n> ')
        if operation == '1':
            return 1
        elif operation == '2':
            return 2
        elif operation == '3':
            return 3
        elif operation == '4':
            return 4
        elif operation == '0':
            return 0
        else:
            print('Вы ввели неккореткное значение типа операции. Повторите ввод.')
            continue

dict_function = {1: 'Сложение', 2: 'Вычетание', 3: 'Сложение', 4: 'Вычетание' }

def print_result(res):
    print(f'Результат = {res}')
