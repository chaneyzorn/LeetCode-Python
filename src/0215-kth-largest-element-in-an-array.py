class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def quick_select(left, right):
            pivot = nums[left]
            l, r = left, right
            while l < r:
                while l < r and nums[r] <= pivot:
                    r -= 1
                while l < r and nums[l] >= pivot:
                    l += 1
                nums[l], nums[r] = nums[r], nums[l]
            nums[l], nums[left] = nums[left], nums[l]

            if l + 1 == k:
                return nums[l]
            if l + 1 > k:
                return quick_select(left, l - 1)
            else:  # l + 1 < k
                return quick_select(l + 1, right)

        return quick_select(0, len(nums) - 1)

    # def findKthLargest(self, nums, k):
    #     nums.sort()
    #     return nums[len(nums) - k]


if __name__ == '__main__':
    Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2)
