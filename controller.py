from init_rational import init, sum, division, mult, difference 
from view import print_start, type_number, entering_number_rational, entering_number_complex, get_menu, print_result
from logger import logger_write
import sys

def unification():
    print_start()
    tp_num = type_number()
    if tp_num == 0:
        sys.exit()
    if tp_num == 1:
        menu = get_menu()
        if menu == 0:
            sys.exit()
        num1, num2 = entering_number_rational()
        init(num1, num2)
        if menu == 1:
            result = sum(num1, num2)
        if menu == 2:
            result = difference(num1, num2)
        if menu == 3:
            result = mult(num1, num2)
        if menu == 4:
            result = division(num1, num2)
        print_result(round(result, 4))
        logger_write(num1, num2, menu, result)
    if tp_num == 2:
        menu = get_menu()
        if menu == 0:
            sys.exit()
        num1, num2 = entering_number_complex()
        init(num1, num2)
        if menu == 1:
            result = sum(num1, num2)
        elif menu == 2:
            result = difference(num1, num2)
        elif menu == 3:
            result = mult(num1, num2)
        elif menu == 4:
            result = division(num1, num2)
        print_result(result)
        logger_write(num1, num2, menu, result)

