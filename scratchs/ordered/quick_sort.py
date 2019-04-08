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


if __name__ == '__main__':
    input = [3, 0, 5, 6, 4, 9, 1, 7, 8, 2]
    quick_sort(input)
    print(input)
