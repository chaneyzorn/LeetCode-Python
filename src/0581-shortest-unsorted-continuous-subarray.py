class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        imax, right = 0, 0

        for i in range(N):
            if nums[i] < nums[imax]:
                right = i
            if nums[i] > nums[imax]:
                imax = i

        imin, left = N - 1, N
        for i in range(N - 1, -1, -1):
            if nums[i] > nums[imin]:
                left = i
            if nums[i] < nums[imin]:
                imin = i

        return right - left + 1 if right > left else 0

    # def findUnsortedSubarray(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     N = len(nums)
    #     l, r = N, 0
    #     for i in range(N):
    #         for j in range(i + 1, N):
    #             if nums[i] > nums[j]:
    #                 l = min(l, i)
    #                 r = max(r, j)
    #     return r - l + 1 if r > l else 0

    # def findUnsortedSubarray(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     snums = sorted(nums)
    #
    #     start, end = len(nums) - 1, 0
    #     for i in range(len(nums)):
    #         if nums[i] != snums[i]:
    #             start = min(start, i)
    #             end = max(end, i)
    #     return 0 if start > end else end - start + 1
