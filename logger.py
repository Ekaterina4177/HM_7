from datetime import datetime as dt

def logger_write(num1, num2, func, res):
    time = dt.now().strftime('%H:%H')
    with open('log.txt', 'a', encoding='utf8') as file:
        file.writelines(f'\nВремя внесения данных {time}, Число первое = {num1}, Число второе = {num2}, Функция {func}, Результат = {res}')
    