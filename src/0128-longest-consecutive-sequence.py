class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        max_longest = 0
        for num in nums:
            if num - 1 not in nums:
                curr_num = num
                curr_longest = 1
                while curr_num + 1 in nums:
                    curr_num += 1
                    curr_longest += 1
                max_longest = max(max_longest, curr_longest)
        return max_longest

    # def longestConsecutive(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     dp = {}
    #     res = 0
    #     for num in sorted(nums):
    #         dp[num] = dp.get(num - 1, 0) + 1
    #         res = max(res, dp[num])
    #     return res
