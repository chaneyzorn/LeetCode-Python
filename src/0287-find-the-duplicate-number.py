class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        p1 = slow
        p2 = nums[0]
        while p1 != p2:
            p1 = nums[p1]
            p2 = nums[p2]
        return p1

    # def findDuplicate(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     record = set()
    #     for i in nums:
    #         if i in record:
    #             return i
    #         else:
    #             record.add(i)
    #     return 0
