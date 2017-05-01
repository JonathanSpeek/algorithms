# iterative implementation of insertion sort in Python


def insertion_sort(a_list):
    """Performs insertion sort on a given list.

    a_list -- list of integers
    
    >>> my_list = [100,6,34,78,2,100,10000,5,789]
    >>> insertion_sort(my_list)
    [2, 5, 6, 34, 78, 100, 100, 789, 10000]
    """

    size = len(a_list)
    i = 0
    while i < size:
        current = a_list[i]
        j = i
        while j > 0 and a_list[j - 1] > current:
            a_list[j] = a_list[j - 1]
            j -= 1
        a_list[j] = current
        i += 1
    return a_list
