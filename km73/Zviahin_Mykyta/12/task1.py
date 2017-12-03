# this programm gets a list from the user, and prints the second biggest number in list

while True:

    list = []  # here i have 4 buffer-variables
    el = ''


    def getlist(n):  # this is the function that gets a list using recursion
        global list
        global el

        if n < 1:
            return list
        else:
            el = int(input("Enter an element: "))
            list.append(el)
            return getlist(n - 1)


    n = int(input("Enter a number of el-s in list: "))
    getlist(n)  # resursion call

    list.sort()
    # this funcrion finds a second biggest number using recursive comparison to the last(biggest)
    # in the sorted list element, in case, when the list has all the same numbers it will print its
    # value, in case, when there is less than 2 elements in a list, it will print this element

    def min2finder(list):
        if len(list) < 2:
            return list
        if list[-2] < list[-1]:
            return list[:-1]
        else:

            return min2finder(list[:-1])


    list = min2finder(list)

    print("Second biggest: ", list[-1])
