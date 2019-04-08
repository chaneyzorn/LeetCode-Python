# insertion_sort


def insertion_sort(items):
    if not items:
        return items
    for i in range(len(items)):
        j, temp = i, items[i]
        while j >= 1 and items[j - 1] > temp:
            items[j] = items[j - 1]
            j -= 1
        items[j] = temp


# shell_sort

def shell_sort(items):
    if not items:
        return items
    length = len(items)
    gap = length
    while gap >= 1:
        gap >>= 2
        for i in range(gap, length):
            j, temp = i, items[i]
            while j >= gap and items[j - gap] > temp:
                items[j] = items[j - gap]
                j -= gap
            items[j] = temp


# bubble_sort

def bubble_sort(items):
    if not items:
        return items
    length = len(items)
    swap_change = True
    turn_count = 0
    while swap_change:
        swap_change = False
        for i in range(1, length - turn_count):
            if items[i] < items[i - 1]:
                items[i], items[i - 1] = items[i - 1], items[i]
                swap_change = True
        turn_count += 1


# quick_sort

def quick_sort(items):
    def _sort(items, l, r):
        if l < r:
            q = partition(items, l, r)
            _sort(items, l, q - 1)
            _sort(items, q + 1, r)

    def partition(items, start, end):
        pivot = items[end]
        i = start - 1
        for j in range(start, end):
            if items[j] < pivot:
                i += 1
                items[i], items[j] = items[j], items[i]
        items[i + 1], items[end] = items[end], items[i + 1]
        return i + 1

    if not items:
        return items
    _sort(items, 0, len(items) - 1)


# quick_select

def quick_select(items, k):
    def _select(items, l, r, k):
        if l < r:
            q = partition(items, l, r)
            if q > (k - 1):
                _select(items, l, q - 1, k)
            elif q < (k - 1):
                _select(items, q + 1, r, k)

    def partition(items, start, end):
        pivot = items[end]
        i = start - 1
        for j in range(start, end):
            if items[j] < pivot:
                i += 1
                items[i], items[j] = items[j], items[i]
        items[i + 1], items[end] = items[end], items[i + 1]
        return i + 1

    if not items:
        return items
    _select(items, 0, len(items) - 1, k)
