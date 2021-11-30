"""
Упражнение 11
Реализуйте класс Dessert c геттерами и сеттерами name и calories, конструктором,
принимающим на вход name и calories (не обязательные параметры), а также двумя
методами is_healthy (возвращает true при условии калорийности десерта менее
200) и is_delicious (возвращает true для всех десертов).
"""


class Dessert:

    def __init__(self, name="dessert", calories=None):
        self.name = name
        self.calories = calories

    def setName(self, name):
        self.name = name

    def setCalories(self, calories):
        self.calories = calories

    def getName(self):
        return self.name

    def getCalories(self):
        return self.calories

    def is_healthy(self):
        if self.calories < 200:
            return True

    def is_delicious(self):
        return True


