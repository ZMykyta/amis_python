# this programm counts the number of max-elements in list

while True:

    def getlist(n):  # this function gets a list from the user
        global list
        global el

        if n < 1:
            return list
        else:
            el = int(input("Enter an element: "))
            list.append(el)
            return getlist(n - 1)

    def maxcounter(list): #this function counts the number of max-elements in list, using recursion
        global counter
        if len(list) < 2:
            counter += 1
            return
        else:
            if list[-2] < list[-1]:
                counter += 1
                return
            else:
                counter += 1
                return maxcounter(list[:-1])

    # function calls and buffer-variables
    n = int(input("Enter a number of elements:"))
    el = ''
    list = []
    counter = 0
    getlist(n)
    list.sort()
    maxcounter(list)
    print("Number of max. elements: ", counter)









