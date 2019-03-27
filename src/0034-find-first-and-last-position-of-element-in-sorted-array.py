class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        N = len(nums)

        def get_insert_index(nums, target, most_left):
            l, r = 0, N
            while l < r:
                mid = (l + r) // 2
                if nums[mid] > target or (most_left and nums[mid] == target):
                    r = mid
                else:
                    l = mid + 1
            return l

        left_index = get_insert_index(nums, target, True)
        if left_index >= N or nums[left_index] != target:
            return [-1, -1]

        right_index = get_insert_index(nums, target, False) - 1
        return [left_index, right_index]

    # def searchRange(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: List[int]
    #     """
    #     if not nums:
    #         return [-1, -1]
    #
    #     N = len(nums)
    #     l, r = 0, N - 1
    #     while l < r:
    #         mid = (l + r) // 2
    #         if nums[mid] > target:
    #             r = mid - 1
    #         elif nums[mid] < target:
    #             l = mid + 1
    #         else:
    #             l = mid
    #             break
    #     if nums[l] != target:
    #         return [-1, -1]
    #
    #     l, r = l, l
    #     while l - 1 >= 0:
    #         if nums[l - 1] == target:
    #             l -= 1
    #         else:
    #             break
    #
    #     while r + 1 < N:
    #         if nums[r + 1] == target:
    #             r += 1
    #         else:
    #             break
    #
    #     return [l, r]
