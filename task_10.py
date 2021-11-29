"""
Разработайте функцию count_words(string), которая будет возвращать словарь со
статистикой частоты употребления входящих в неё слов.
Тесты для примеров и проверки:
count_words("A man, a plan, a canal -- Panama") # => {"a": 3, "man": 1,
"canal": 1, "panama": 1, "plan": 1}
count_words("Doo bee doo bee doo") # => {"doo": 3, "bee": 2}
"""
import re


def count_words(string):
    numberwords = {}
    not_a_symbols = r'\W'  # \W - Не буквенные символы, \w -исключительно буквенные
    s = re.sub(not_a_symbols, ' ', string.lower())
    s = list(s.split())
    for i in s:
        if numberwords.get(i):
            numberwords.update([(i, numberwords.get(i)+1)])
        else:
            numberwords.update([(i, 1)])

    return numberwords






if __name__ == '__main__':
    print (count_words("Doo bee doo bee doo"))