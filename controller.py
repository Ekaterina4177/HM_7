from init_rational import init_rational, sum_rational, division_rational, mult_rational, difference_rational 
from init_complex import init_complex, sum_complex, difference_complex, mult_complex, division_complex
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
        init_rational(num1, num2)
        if menu == 1:
            result = sum_rational(num1, num2)
            print_result(result)
        if menu == 2:
            result = difference_rational(num1, num2)
            print_result(result)
        if menu == 3:
            result = mult_rational(num1, num2)
            print_result(result)
        if menu == 4:
            result = division_rational(num1, num2)
            print_result(result)
        logger_write(num1, num2, menu, result)
    if tp_num == 2:
        menu = get_menu()
        if menu == 0:
            sys.exit()
        num1, num2 = entering_number_complex()
        init_complex(num1, num2)
        if menu == 1:
            result = sum_complex(num1, num2)
            print_result(result)
        elif menu == 2:
            result = difference_complex(num1, num2)
            print_result(result)
        elif menu == 3:
            result = mult_complex(num1, num2)
            print_result(result)
        elif menu == 4:
            result = division_complex(num1, num2)
            print_result(result)
        logger_write(num1, num2, menu, result)

