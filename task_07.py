'''Анаграмма — литературный приём, состоящий в перестановке букв или звуков
определённого слова (или словосочетания), что в результате даёт другое слово
или словосочетание.
Разработайте метод combine_anagrams(words_array), который принимает на вход
массив слов и разбивает их в группы по анаграммам, регистр букв не имеет
значения при определении анаграмм.
str.lower
Тест для примеров и проверки:
combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar",
"creams", "scream"]) # => [ ["cars", "racs", "scar"], ["four"], ["for"],
["potatoes"], ["creams", "scream"] ]
'''


def combine_anagrams(words_array):
    '''
    Создаём ещё один список,
    элементы в котором - представленные в виде отсортированных списков слова
    из исходного списка
    '''
    sor = []
    for i in words_array:
        sor.append(sorted(i.lower()))

    res = []#Список результат
    dig = []#Хранит в себе одну группу анаграмм
    while sor:
        a = sor.pop(0)                                      #Запоминаем первый элемент,удаляя его из списка
        dig.append(words_array.pop(0))                      #И добавляем в группу элемент из исходного списка, также удаляя его оттуда
        try:
            while b := sor.index(a) or 0:           #Если найдётся элемент идентичный раннему
                dig.append(words_array.pop(b))      #Добавили его в группу
                sor.pop(b)                          #И удалили элемент с этим индексом из обоих списков
        except:
            res.append(dig)
            dig = []
    return res


if __name__ == '__main__':
    print(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar", "abbd", "aDbb", "bbda",
                            "creams", "scream"]))
