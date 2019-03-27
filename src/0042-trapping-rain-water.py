class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        N = len(height)
        res, l, r = 0, 0, N - 1
        l_max, r_max = 0, 0

        while l < r:
            if height[l] < height[r]:
                if height[l] >= l_max:
                    l_max = height[l]
                else:
                    res += l_max - height[l]
                l += 1
            else:
                if height[r] >= r_max:
                    r_max = height[r]
                else:
                    res += r_max - height[r]
                r -= 1
        return res


    # def trap(self, height):
    #     """
    #     :type height: List[int]
    #     :rtype: int
    #     """
    #     N = len(height)
    #     if N < 2:
    #         return 0
    #     res, l, r = 0, 0, 1
    #
    #     left_max, right_max = [0] * N, [0] * N
    #     left_max[0], right_max[-1] = height[0], height[-1]
    #
    #     for i in range(1, N):
    #         left_max[i] = max(left_max[i - 1], height[i])
    #     for i in range(N - 2, -1, -1):
    #         right_max[i] = max(right_max[i + 1], height[i])
    #     for i in range(N):
    #         res += min(left_max[i], right_max[i]) - height[i]
    #     return res
