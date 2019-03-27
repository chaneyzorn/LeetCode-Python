class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        sum = 0
        record = {0: 1}
        for num in nums:
            sum += num
            if (sum - k) in record:
                res += record[sum - k]
            record[sum] = record.get(sum, 0) + 1
        return res

    # def subarraySum(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: int
    #     """
    #     N = len(nums)
    #     res = 0
    #     for start in range(N):
    #         sum = 0
    #         for end in range(start, N):
    #             sum += nums[end]
    #             if sum == k:
    #                 res += 1
    #     return res
