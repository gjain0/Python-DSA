"""
Sort the array using quick sort algorithm
>>> mylist = [17, 87, 62, 55, 42, 42, 5, 37, 50, 88]
>>> quick_sort(mylist)
>>> mylist
[5, 17, 37, 42, 42, 50, 55, 62, 87, 88]
>>>
"""


def partition(alist, start, end):
    """
    This function assumes last element as pivot, places all smaller (smaller than pivot) to
    left of pivot and all greater elements to right of pivot, this way the pivot element will be at correct position
    """
    pivot = alist[start]
    i = start
    j = end

    while True:
        while (i <= j and alist[i] <= pivot):
            i = i + 1
        while (i <= j and alist[j] >= pivot):
            j = j - 1

        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
        else:
            alist[start], alist[j] = alist[j], alist[start]
            return j


def quick_sort_helper(alist, start, end):
    if start < end:
        # p is partitioning index, the element alist[p] is now at right position
        p = partition(alist, start, end)

        # Individually sort elements before and after partition, recursively!
        quick_sort_helper(alist, start, p - 1)
        quick_sort_helper(alist, p + 1, end)


def quick_sort(alist):
    quick_sort_helper(alist, 0, len(alist) - 1)
