'''Дан список элементов произвольной природы. Необходимо разработать метод
max_odd(array), который определит максимальный нечетный элемент (21.000 = 21 и
тоже считается нечетным элементом). Вернуть None, если таких элементов нет в
переданном массиве.
Тесты для примеров и проверки:
max_odd([1, 2, 3, 4, 4]) # => 3
max_odd([21.0, 2, 3, 4, 4]) # => 21
max_odd(['ololo', 2, 3, 4, [1, 2], None]) # => 3
max_odd(['ololo', 'fufufu']) # => None
max_odd([2, 2, 4]) # => None
'''
def max_odd(data):
    s=None
    for i in data:
        try:
            if i%2==1:
                if s is not None:
                    if i>s:
                        s=i
                else :
                    s=i
        except TypeError:
           # print(i)
           continue
    return s
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(max_odd([2, 2, 4]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
