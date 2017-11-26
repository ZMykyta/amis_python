# Звягін М.С. КМ-72 9.Принцип модульності.Функції. Завдання 1

from math import sqrt


def distance(x1, y1, x2, y2):
    # Визначимо відстань між двома точками за допомогою формули Піфагора
    result = (sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
    return result


# Зчитаємо значення параметрів функції distance
firstCoord1 = float(input("Введіть координату x1: "))
firstCoord2 = float(input("Введіть координату y1: "))
secondCoord1 = float(input("Введіть координату x2: "))
secondCoord2 = float(input("Введіть координату y2: "))


print("Відстань між цими двома точками: ", distance(firstCoord1, firstCoord2, secondCoord1, secondCoord2))
