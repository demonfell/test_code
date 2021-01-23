# used example from https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-1.php

animal_list = ['anteater',
 'antelope',
 'bird',
 'cat',
 'deer',
 'monkey',
 'penguin',
 'snake',
 'turtle',
 'walrus',
 'zebra']

def list_bisect(search_term, list_name):
    first = 0
    end = len(list_name)-1
    found = False
    while (first <= end and not found):
        mid = (first + end)//2
        if list_name[mid] == search_term:
            found = True
            return mid
        else:
            if search_term  < list_name[mid]:
                end = mid - 1
            elif search_term  > list_name[mid]:
                first = mid + 1
            else:
                return -1

list_bisect('snake', animal_list)
