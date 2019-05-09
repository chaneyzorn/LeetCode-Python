"""
2.  一个无序不重复的整数数组，给一个数值K，问有多少对数之和为K？ 有多少对之差为K？ 如果数组中有重复数呢？
"""


def sum_k(array, k):
    """一个无序不重复的整数数组，给一个数值K，问有多少对数之和为K(数字不重复)"""
    result = 0
    array_dict = {}

    debug = []

    for i, val in enumerate(array):
        array_dict[val] = i

    for i, val in enumerate(array):
        # val + target = k
        target = k - val

        # 如果是指定求差
        # val - target = k 则 target = val - k
        # target - val = k 则 target = val + k

        # 存在一个与当前数和为 k 的数，并且这个数不是自己
        if target in array_dict and array_dict.get(target) != i:
            debug.append((val, target))
            array_dict.pop(target)
            array_dict.pop(val)
            result += 1

    print(debug)
    return result


def sum_k_when_duplicate(array, k):
    """一个无序不重复的整数数组，给一个数值K，问有多少对数之和为K(数字重复)"""
    result = 0
    # 重复数字，使用计数
    count_dict = {}

    debug = []

    for i, val in enumerate(array):
        count_dict[val] = count_dict.get(val, 0) + 1

    for i, val in enumerate(array):
        target = k - val
        # 存在一个与当前数和为 k 的数
        if target in count_dict and count_dict.get(target) > 0:
            # 如果这个数是自己，但是只有一个，不计入结果
            if val == target and count_dict.get(target) < 2:
                continue
            debug.append((val, target))
            count_dict[target] -= 1
            count_dict[val] -= 1
            result += 1

    print(debug)
    return result


if __name__ == '__main__':
    print(sum_k([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6))
    print("====================")
    print(sum_k_when_duplicate([1, 2, 2, 2, 3, 1, 3, 1, 3, 4, 5, 6, 7, 8, 9, 10], 4))
