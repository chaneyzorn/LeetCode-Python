class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return sum(nums)

        center = len(nums) // 2
        left = nums[:center]
        right = nums[center:]
        left_max = self.maxSubArray(left)
        right_max = self.maxSubArray(right)

        left_border_sum = 0
        left_border_max = left[-1]
        for i in reversed(left):
            left_border_sum += i
            if left_border_max < left_border_sum:
                left_border_max = left_border_sum

        right_border_sum = 0
        right_border_max = right[0]
        for i in right:
            right_border_sum += i
            if right_border_max < right_border_sum:
                right_border_max = right_border_sum

        return max(left_max, right_max, right_border_max + left_border_max)

    # def maxSubArray(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     if not nums:
    #         return 0
    #
    #     cur_sum = 0
    #     max_sum = 0
    #     max_single = nums[0]
    #     for i in nums:
    #         if i > max_single:
    #             max_single = i
    #         cur_sum += i
    #         if cur_sum > max_sum:
    #             max_sum = cur_sum
    #         if cur_sum < 0:
    #             cur_sum = 0
    #     return max_sum if max_sum > 0 else max_single
