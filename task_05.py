'''Разработать метод date_in_future(integer), который вернет дату через integer дней.
Если integer не является целым числом, то метод должен вывести текущую дату.
Формат возвращаемой методом даты должен иметь следующий вид '01-01-2001
22:33:44’.

Тесты для примеров и проверки:
date_in_future([]) # => текущая дата
date_in_future(2) # => текущая дата + 2 дня

%d: день месяца в виде числа

%m: порядковый номер месяца

%y: год в виде 2-х чисел

%Y: год в виде 4-х чисел

%H: час в 24-х часовом формате

%M: минута

%S: секунда
'''

from datetime import datetime, timedelta



def date_in_future(num):
    dt_obj = datetime.now()
    if type(num) != int:
        return dt_obj.strftime("%d-%m-%Y %H:%M:%S")
    return (datetime.today() + timedelta(days=num)).strftime("%d-%m-%Y %H:%M:%S")

if __name__ == '__main__':
    integer = 2
    print(date_in_future(integer))
