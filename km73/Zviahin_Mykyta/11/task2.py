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

iterat = 0

min_el = List[iterat]

def minimumfinder(List, iterat):

    global min_el
    if iterat < len(List) - 1:
        if min_el > List[iterat + 1]:
            min_el = List[iterat + 1]
            return minimumfinder(List, iterat + 1)
    else:
        return minimumfounder(List, iterat + 1)

    return min_el


print("The minimum element: ", minimumfinder(List, iterat))

input()
