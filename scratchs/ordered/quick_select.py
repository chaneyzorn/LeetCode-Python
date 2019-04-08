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


if __name__ == '__main__':
    input = [3, 0, 5, 6, 4, 9, 1, 7, 8, 2]
    quick_select(input, 10)
    print(input)
