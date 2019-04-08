def binary_search(items, target):
    def _search(items, start, end, target):
        l, r = start, end
        while l <= r:
            mid = l + (r - l) // 2
            if items[mid] == target:
                return mid
            elif items[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1

    return _search(items, 0, len(items) - 1, target)


if __name__ == '__main__':
    print(binary_search([1, 2, 3, 4, 5], 2))
