class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        sorted_nums = [0] * N

        def replace_or_insert(val, right):
            l, r = 0, right
            while l < r:
                mid = (r + l) // 2
                if sorted_nums[mid] >= val:
                    r = mid
                else:
                    l = mid + 1
            sorted_nums[l] = val
            return l

        max_len = 0
        for val in nums:
            curr_len = replace_or_insert(val, max_len) + 1
            max_len = max(max_len, curr_len)

        return max_len

    # def lengthOfLIS(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     record = {}
    #     max_len = 0
    #     for val in nums:
    #         curr_len = 1
    #         for key, length in record.items():
    #             if key < val:
    #                 curr_len = max(curr_len, length + 1)
    #         record[val] = curr_len
    #         max_len = max(max_len, curr_len)
    #     return max_len


if __name__ == '__main__':
    result = Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
    print(result)
