class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        for i, val in enumerate(nums):
            for sub in self.permute(nums[:i] + nums[i + 1:]) or [[]]:
                result.append([val] + sub)
        return result
