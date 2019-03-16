class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rob_1 = 0
        rob_2 = 0
        result = 0
        for num in nums:
            result = max(rob_2 + num, rob_1)
            rob_2 = rob_1
            rob_1 = result
        return result
