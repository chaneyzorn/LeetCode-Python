def shell_sort(items):
    if not items:
        return items

    length = len(items)
    gap = length
    while gap >= 1:
        gap >>= 1
        for i in range(gap, length):
            j, temp = i, items[i]
            while j >= gap and items[j - gap] > temp:
                items[j] = items[j - gap]
                j -= gap
            items[j] = temp


if __name__ == '__main__':
    input = [3, 0, 5, 6, 4, 9, 1, 7, 8]
    shell_sort(input)
    print(input)
