'''
Разработайте метод is_palindrome(string), который будет определять, является ли
параметр string палиндромом (строкой, которая читается одинаково как сначала
так и с конца), при условии игнорирования пробелов, знаков препинания и
регистра.

is_palindrome("A man, a plan, a canal -- Panama") # => True
is_palindrome("Madam, I'm Adam!") # => True
is_palindrome(333) # => True
is_palindrome(None) # => False
is_palindrome("Abracadabra") # => False
'''
import re


def is_palindrome(a):
    not_a_symbols = r'\W'  # \W - Не буквенные символы, \w -исключительно буквенные
    if a:
        s = re.sub(not_a_symbols, '', str(a).lower())
        return list(s) == list(reversed(s))
    else:
        return False



if __name__ == '__main__':
    #data = input()
    print(is_palindrome("2A man, a plan, a1 c1anal -- Panama2"))
