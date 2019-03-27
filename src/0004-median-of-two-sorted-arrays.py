class Solution(object):
    def findMedianSortedArrays(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: float
        """

        """
              left_part          |        right_part
        A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
        B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]
        """

        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m

        l, r = 0, m
        half_len = (m + n + 1) // 2
        while l <= r:
            i = (l + r) // 2
            j = half_len - i
            if i < m and B[j - 1] > A[i]:
                l = i + 1
            elif i > 0 and A[i - 1] > B[j]:
                r = i - 1
            else:
                if i == 0:
                    max_of_left = B[j - 1]
                elif j == 0:
                    max_of_left = A[i - 1]
                else:
                    max_of_left = max(A[i - 1], B[j - 1])

                if (m + n) & 1 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0

    # def findMedianSortedArrays(self, nums1, nums2):
    #     """
    #     :type nums1: List[int]
    #     :type nums2: List[int]
    #     :rtype: float
    #     """
    #     nums = nums1 + nums2
    #     nums.sort()
    #     N = len(nums)
    #     if (N & 1 == 1):
    #         return nums[N // 2]
    #     else:
    #         return (nums[N // 2 - 1] + nums[N // 2]) / 2.0
