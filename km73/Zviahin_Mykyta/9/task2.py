# Звягін М.С 9.Принцип модульності. Функції.


def power(a, n):
    result = a ** n
    return result


base = float(input("Введіть дійсне додатнє число: "))
# Введемо перевірку на доречність зчитаного числа
while base <= 0:
    base = float(input("Введіть дійсне додатнє число: "))

powerValue = int(input("Введіть степінь: "))

print("Число ", base, " у степені ", powerValue, " : ", power(base, powerValue))
