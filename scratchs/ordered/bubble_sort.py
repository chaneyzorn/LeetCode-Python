def bubble_sort(items):
    if not items:
        return items

    swap_change = True
    turn_count = 0
    while swap_change:
        swap_change = False
        for i in range(1, len(items) - turn_count):
            if items[i] < items[i - 1]:
                items[i], items[i - 1] = items[i - 1], items[i]
                swap_change = True
        turn_count += 1


if __name__ == '__main__':
    input = [3, 0, 5, 6, 4, 9, 1, 7, 8]
    bubble_sort(input)
    print(input)
