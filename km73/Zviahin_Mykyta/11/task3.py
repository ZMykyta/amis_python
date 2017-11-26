""" Эта часть кода считывает количество элементов списка, и проверяет
их на правильность типа данных"""
def getnumber():
    quantity = input("Enter number of element in list: ")

    if not quantity.isdigit():
        print("Enter a natural number!")
        return getnumber()

    if len(quantity) < 1:
        print("Enter a natural number!")
        return getnumber()
    if int(quantity) == 0:

        print("Enter a natural number!")
        return getnumber()

    else:
        print("Great!")
        return int(quantity)


quantity = getnumber()

numbers = []

new_el = ''
# эта часть кода считывает список, и проверяет каждый элемент списка рекурсивным методом
# на правильность типа введенных данных
def getlist(quantity):
    global numbers

    if len(numbers) < quantity:

        def getelement():

            global new_el
            new_el = input("Enter a number: ")

            if not new_el.isdigit():

                print("Enter a number!")
                return getelement()

            else:
                return int(new_el)

        getelement()
        numbers.append(new_el)
        getlist(quantity)
        return numbers
    else:
        return numbers


List = getlist(quantity)

# эта функция будет возвращать иходный список в обратном порядке,
# за счет работы со списком, длина которого больше или равна двум , рекурсивно деля его
# на два, и проверяя на размер, в последствии склеивая за счет slice -операций и операции конкатенации
def reverse(List):
    if len(List) < 2:
      return List
    else:
      Listhalf = len(List) // 2
      return reverse(List[Listhalf:]) + reverse(List[:Listhalf])

print("Reversed list: ", reverse(List))
input()
