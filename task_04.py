'''Дан список целых чисел. Необходимо разработать метод sort_list(list),который
поменяет местами все минимальные и максимальные элементы массива, а также
добавит в конец массива одно минимальное значение из него.
Тесты для примеров и проверки:
sort_list([]) # => []
sort_list([2, 4, 6, 8]) # => [8, 4, 6, 2, 2]
sort_list([1]) # => [1, 1]
sort_list([1, 2, 1, 3]) # => [3, 2, 3, 1, 1]
'''


def sort_list(data):
    if not data:
        return data

    mx=max(data)
    mn=min(data)
    for i in range(len(data)):
        if data[i] ==mn:
            data[i] = mx
        elif data[i] ==mx:
            data[i] = mn
    data.append(mn)
    return data


if __name__ == '__main__':

        print(sort_list([1, 2, 1, 3]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
