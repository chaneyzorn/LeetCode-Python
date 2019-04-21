class Solution:
    # array 二维列表
    def Find(self, target, array):
        if not array:
            return False
        row_count = len(array)
        col_count = len(array[0])
        r, c = row_count - 1, 0
        while r >= 0 and c < col_count:
            if target < array[r][c]:
                r -= 1
            elif target > array[r][c]:
                c += 1
            else:
                return True
        return False
