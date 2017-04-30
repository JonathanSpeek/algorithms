# implementation of binary search in Python


def binary_search(my_list, item):
    first = 0
    last = len(my_list) - 1

    while first <= last:
        i = (first + last) / 2

        if my_list[i] == item:
            return '{item} found at position {i}'.format(item=item, i=i)
        elif my_list[i] > item:
            last = i - 1
        elif my_list[i] < item:
            first = i + 1
        else:
            return '{item} not found in this list'.format(item=item)
