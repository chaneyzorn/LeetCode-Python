class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for val in nums:
            new_res = []
            for exist in res:
                new_res.append(list(exist) + [val])
            res += new_res
        return res
