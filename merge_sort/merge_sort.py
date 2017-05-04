# implementation of merge sort in Python


def merge_sort(a_list):
    """Performs merge sort on a given list.

    a_list -- list of integers

    >>> my_list = [100,6,34,78,2,100,10000,5,789]
    >>> merge_sort(my_list)
    [2, 5, 6, 34, 78, 100, 100, 789, 10000]
    """

    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                a_list[k] = left_half[i]
                i += 1
            else:
                a_list[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            a_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            a_list[k] = right_half[j]
            j += 1
            k += 1
    return a_list
