class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not (nums and k):
            return []
        N = len(nums)
        k = min(k, N)

        res = []
        m = max(nums[:k])
        res.append(m)

        for i in range(1, N - k + 1):
            if m != nums[i - 1]:
                m = max(m, nums[i + k - 1])
            else:
                m = max(nums[i: i + k])
            res.append(m)
        return res

    # def maxSlidingWindow(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: List[int]
    #     """
    #     if not (nums and k):
    #         return []
    #     from collections import deque
    #
    #     N = len(nums)
    #     k = min(k, N)
    #     queue = deque()
    #
    #     for i in range(k):
    #         while queue:
    #             if nums[i] > nums[queue[-1]]:
    #                 queue.pop()
    #             else:
    #                 break
    #         queue.append(i)
    #
    #     res = [nums[queue[0]]]
    #
    #     for i in range(k, N):
    #         if i - queue[0] >= k:
    #             queue.popleft()
    #
    #         while queue:
    #             if nums[i] > nums[queue[-1]]:
    #                 queue.pop()
    #             else:
    #                 break
    #         queue.append(i)
    #         res.append(nums[queue[0]])
    #
    #     return res
