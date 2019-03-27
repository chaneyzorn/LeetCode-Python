class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        N = len(nums)
        l, r = 0, N - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:  # nums[mid] <= nums[r]
                r = mid

        rot = l
        l, r = 0, N - 1
        while l <= r:
            mid = (r + l) // 2
            real_mid = (mid + rot) % N
            if nums[real_mid] == target:
                return real_mid
            if nums[real_mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
