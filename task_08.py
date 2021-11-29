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
    str_mult = re.sub(not_a_symbols, '', inputs)
    if not str_mult:
        return None
    s = 1
    for i in str_mult:
        s *= int(i)
    print(inputs)
    return s


if __name__ == '__main__':
    try:
        print(multiply_numbers('ss2255s'))
    except TypeError:
        print(None)
