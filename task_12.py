"""
Создайте класс JellyBean, расширяющий класс Dessert (из Упражнения 11) новым
геттером и сеттером для атрибута flavor (все параметры являются не
обязательными). Измените метод is_delicious таким образом, чтобы он возвращал
false только в тех случаях, когда flavor равняется «black licorice».
"""


class Dessert:

    def __init__(self, name="dessert", calories=None):
        self._name = name
        self._calories = calories

    def setName(self, name):
        self._name = name

    def setCalories(self, calories):
        self._calories = calories

    def getName(self):
        return self._name

    def getCalories(self):
        return self._calories

    def is_healthy(self):
        if self._calories < 200:
            return True
        else: return False

    def is_delicious(self):
        return True


class JellyBean(Dessert):
    def __init__(self, name="dessert", calories=None, flavor=None):
        super().__init__(name, calories)
        self.flavor = flavor

    def is_delicious(self):
        if self.flavor == "black licorice":
            return False
        else:
            return True

        def setFlavor(self, flavor):
            self._flavor = flavor

        def getFlavor(self):
            return self._flavor


