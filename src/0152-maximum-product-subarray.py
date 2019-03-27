class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = float("-inf")
        imax = 1
        for val in nums:
            imax *= val
            res = max(res, imax)
            imax = 1 if imax == 0 else imax

        imax = 1
        for val in nums[::-1]:
            imax *= val
            res = max(res, imax)
            imax = 1 if imax == 0 else imax
        return res

    # def maxProduct(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     if not nums:
    #         return 0
    #
    #     imax, imin, res = nums[0], nums[0], nums[0]
    #
    #     for val in nums[1:]:
    #         if val < 0:
    #             imax, imin = imin, imax
    #
    #         imax = max(val, imax * val)
    #         imin = min(val, imin * val)
    #
    #         res = max(res, imax)
    #     return res
