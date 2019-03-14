class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in nums:
            result ^= i
        return result

    # def singleNumber(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     num_set = set()
    #     for i in nums:
    #         if i in num_set:
    #             num_set.remove(i)
    #         else:
    #             num_set.add(i)
    #     return num_set.pop()
