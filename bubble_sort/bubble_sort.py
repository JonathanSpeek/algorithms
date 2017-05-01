# implementation of bubble sort in Python


def bubble_sort(a_list):
    """Performs bubble sort on a given list.

    a_list -- list of integers

    >>> my_list = [100,6,34,78,2,100,10000,5,789]
    >>> bubble_sort(my_list)
    [2, 5, 6, 34, 78, 100, 100, 789, 10000]
    """

    for pass_num in range(len(a_list) - 1, 0, -1):
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
    return a_list
