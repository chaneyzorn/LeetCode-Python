def insertion_sort(items):
    if not items:
        return items

    for i in range(len(items)):
        j, temp = i, items[i]
        # 针对 j - 1
        while j >= 1 and items[j - 1] > temp:
            items[j] = items[j - 1]  # 向后移动
            j -= 1
        items[j] = temp


if __name__ == '__main__':
    input = [3, 0, 5, 6, 4, 9, 1, 7, 8]
    insertion_sort(input)
    print(input)
