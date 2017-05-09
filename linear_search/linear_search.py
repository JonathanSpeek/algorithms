# iterative implementation of linear search in Python


def linear_search(item, a_list):
    """Performs iterative linear search to find the position of an integer in a given, sorted, list.

    a_list -- sorted list of integers
    item -- integer you are searching for the position of
    """
    i = 0
    while i < len(a_list):
        if item == a_list[i]:
            print('{item} found at position {i}'.format(item=item, i=i))
        i += 1
    print('{item} not found in the list'.format(item=item))
