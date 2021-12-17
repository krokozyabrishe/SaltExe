'''
Дан список list и числовой диапазон range. Разработайте метод coincidence(list,
range) для определения элементов из массива list, значения которого входят в
указанный диапазон range. Если не передан хотя бы один из параметров, то
должен вернуться пустой массив.

Тесты для примеров и проверки:
coincidence([1, 2, 3, 4, 5], range(3, 6)) # => [3, 4, 5]
coincidence() # => []
coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)) # => [1, 2, 2.5]
'''


def coincidence(data, rang):
    res = []
    rang = list(rang)
    for i in data:
        try:
            if rang[0] <=  float(i) <= rang[-1]:
                res.append(i)
        except:
            continue
    return res

if __name__ == '__main__':

    try:
        print(coincidence([None, "1", 'foo', "3", 2, 2.5555], range(1, 4)))
    except:
        print([])



