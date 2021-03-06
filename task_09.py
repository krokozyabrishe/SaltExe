'''
Необходимо разработать метод connect_dicts(dict1, dict2), который соединит два
переданных словаря, значениями ключей в которых являются числа, и вернет
новый словарь, полученный по следующим правилам:

• приоритетными являются ключи того словаря, сумма значений ключей
которого больше (если суммы значений ключей будут равны, то второй
словарь считается более приоритетным)
• ключи со значениями меньше 10 не должны попасть в финальный
словарь
• получившийся словарь должен вернуться упорядоченным по значениям
ключей в порядке возрастания.

Тесты для примеров и проверки:
connect_dicts({ "a": 2, "b": 12 }, { "c": 11, "e": 5 }) # =>
{ "c": 11, "b": 12 }
connect_dicts({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 }) # =>
{ d: 11, "c": 12, "a": 13 }
connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 }) # =>
{ "c": 11, "b": 12, "a": 15 }
'''


def check(first, sec):
    a = {}
    for key in sec.items():
        if key[1] > 10:
            a[key[0]] = key[1]
    for key in first.items():
        if key[1] > 10:
            a[key[0]] = key[1]
    return a


def connect_dicts(dict1, dict2):
    if sum(dict1.values()) > sum(dict2.values()):
        a = check(dict1, dict2)
    else:
        a = check(dict2, dict1)
    print(dict(sorted(a.items(), key=lambda x: x[1])))


if __name__ == '__main__':
    connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 })
