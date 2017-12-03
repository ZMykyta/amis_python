# This programm gets a list of natural numbers from the user, creates a list
# of groups of same numbers, if they stay near to each other in default list,
# finds the biggest grop, and prints the number of elements in group and the group itself

# getting a number of elements in default list
N = int(input("Enter number of elements(natural number): "))
# buffer variables
massive = []
new_el = ''

# this function gets a list from the user using recursion
def getlist(N):
    if N < 2:
        global new_el
        new_el = int(input("Enter an element(natural number): "))
        massive.append(new_el)
        return massive
    else:
        new_el = int(input("Enter an element(natural number): "))
        massive.append(new_el)
        return getlist(N-1)

# buffer variables for the next function
getlist(N)
groupmassive = []
group_el = []
comparer = ''

# this function creates a new list, which contains groups of the same elements if the stay next to each
# other in default list
def groupfinder(massive):
    global comparer
    global new_el
    new_el = ''
    global group_el

    if len(massive) < 1:
        return groupmassive
    elif len(massive) == 1:
        if comparer == massive[0]:

            new_el = massive[0]
            group_el.append(new_el)
            groupmassive.append(group_el)
            return groupmassive
        else:
            new_el = massive[0]

            group_el.append(new_el)
            groupmassive.append(group_el)
        return groupmassive
    else:
        if massive[0] == massive[1]:
            new_el = massive[0]
            group_el.append(new_el)
            return groupfinder(massive[1:])
        else:
            new_el = massive[0]
            group_el.append(new_el)
            groupmassive.append(group_el)
            comparer = group_el[-1]
            group_el = []
            return groupfinder(massive[1:])


groupfinder(massive)
print(groupmassive)
iterator = 0
longest = ''

# this function finds the longest group and returns it
def longestfinder(massive, iterator):
    global longest
    if len(massive) < iterator:
        return longest

    if len(massive[0]) > len(massive[1]):
        longest = massive[0]
        return longestfinder(massive, iterator+1)
    else:
        longest = massive[1]
        return longestfinder(massive, iterator+1)


longestfinder(groupmassive, iterator)
joiner = ' '
print("The biggest group - ", len(longest), " : ", longest)
