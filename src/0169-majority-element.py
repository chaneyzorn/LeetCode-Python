class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = None
        count = 0

        for num in nums:
            if count == 0:
                result = num
            count += (1 if num == result else -1)
        return result
