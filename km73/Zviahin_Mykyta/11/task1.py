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

            if not (new_el[1:] if new_el[0] == '-' else new_el).isdigit():

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

#эта часть кода будет записывать новый список, в котором не будет содержаться нулевых элементов
it = 0
finalList = []
def nulesdeleter(List, it):

    global finalList

    if it < len(List):

        if List[it] != '0':
            finalList.append(List[it])
            return nulesdeleter(List, it + 1)

        else:

            return nulesdeleter(List, it + 1)
    else:
        return finalList

nonules = nulesdeleter(List, it)

print("List wothout nules: ", nonules)

input()




