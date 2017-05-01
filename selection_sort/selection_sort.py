# implementation of selection sort in Python


def selection_sort(a_list):
    """Performs selection sort on a given list.

    a_list -- list of integers

    >>> my_list = [100,6,34,78,2,100,10000,5,789]
    >>> selection_sort(my_list)
    [2, 5, 6, 34, 78, 100, 100, 789, 10000]
    """

    for pass_num in range(len(a_list) - 1, 0, -1):
        max_num = 0
        for i in range(1, pass_num + 1):
            if a_list[i] > a_list[max_num]:
                max_num = i

        a_list[pass_num], a_list[max_num] = a_list[max_num], a_list[pass_num]

    return a_list
