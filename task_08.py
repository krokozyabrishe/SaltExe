"""Упражнение 8
Написать метод multiply_numbers(inputs), который вернет произведение цифр,
входящих в inputs.

Тест для примеров и проверки:
multiply_numbers() # => None
multiply_numbers('ss') # => None
multiply_numbers('1234') # => 24
multiply_numbers('sssdd34') # => 12
multiply_numbers(2.3) # => 6
multiply_numbers([5, 6, 4]) # => 120
"""

import re


def multiply_numbers(inputs):

    not_a_symbols = r'\D'
    inputs = re.sub(not_a_symbols, '', str(inputs))
    if not inputs:
        return None
    s = 1
    for i in inputs:
        s *= int(i)

    return s


if __name__ == '__main__':
    try:
        print(multiply_numbers([5, 6, 4]))
    except TypeError:
        print(None)
