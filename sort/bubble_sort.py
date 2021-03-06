def bubble_sort(alist):
    """
    Sort the array using bubble sort algorithm
    >>> mylist = [17, 87, 62, 55, 42, 42, 5, 37, 50, 88]
    >>> bubble_sort(mylist)
    >>> mylist
    [5, 17, 37, 42, 42, 50, 55, 62, 87, 88]
    >>>
    """
    n = len(alist)  # Number of items in the list

    for i in range(n):
        for j in range(0, n - i - 1):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]


# Bubble sort implementation with controlled sorting behaviour

def bubble_sort(alist, reverse=False):
    """
    Sort the array in desired order using bubble sort algorithm
    reverse parameter controls the order of elements, if `reverse=True`, this will sort the array in descending order
    >>> mylist = [17, 87, 62, 55, 42, 42, 5, 37, 50, 88]
    >>> bubble_sort(mylist, reverse=True)
    >>> mylist
    [88, 87, 62, 55, 50, 42, 42, 37, 17, 5]
    >>>
    >>> mylist = [17, 87, 62, 55, 42, 42, 5, 37, 50, 88]
    >>> bubble_sort(mylist)
    >>> mylist
    [5, 17, 37, 42, 42, 50, 55, 62, 87, 88]
    """
    n = len(alist)  # Number of items in the list

    for i in range(n):
        for j in range(0, n - i - 1):
            if reverse and alist[j] < alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
            elif not reverse and alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
