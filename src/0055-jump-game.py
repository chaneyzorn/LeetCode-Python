class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return True

        require = 1
        for num in nums[1:-1][::-1]:
            if num >= require:
                require = 1
            else:
                require += 1
        return nums[0] >= require
