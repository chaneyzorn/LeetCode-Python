class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        result = [1] * N
        for i in range(1, N):
            result[i] = result[i - 1] * nums[i - 1]

        right_product = 1
        i = N - 1
        while i >= 0:
            result[i] *= right_product
            right_product *= nums[i]
            i -= 1
        return result

    # def productExceptSelf(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[int]
    #     """
    #
    #     zero_count, zero_index = 0, 0
    #     for i, val in enumerate(nums):
    #         if val == 0:
    #             zero_count += 1
    #             zero_index = i
    #
    #     if zero_count >= 2:
    #         return [0] * len(nums)
    #
    #     # zero_count <= 1
    #     total_product = 1
    #     for val in nums:
    #         if not val:
    #             continue
    #         total_product *= val
    #
    #     if zero_count == 1:
    #         result = [0] * len(nums)
    #         result[zero_index] = total_product
    #     else:
    #         result = []
    #         for val in nums:
    #             result.append(total_product // val)
    #     return result
