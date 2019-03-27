class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        bit = 1
        total = 0
        for num in nums:
            total += num
            bit |= bit << num
        if (total & 1) == 1:
            return False
        return (bit >> (total // 2)) & 1 == 1

    # def canPartition(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: bool
    #     """
    #     N = len(nums)
    #     total = sum(nums)
    #     if (total & 1) == 1:
    #         return False
    #
    #     total //= 2
    #
    #     dp = [False] * (total + 1)
    #     dp[0] = True
    #
    #     for num in nums:
    #         for i in range(total, num - 1, -1):
    #             dp[i] = dp[i] or dp[i - num]
    #
    #     return dp[total]
