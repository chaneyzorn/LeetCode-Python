class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []

        frequent_map = {}
        for i in nums:
            frequent_map[i] = frequent_map.get(i, 0) + 1
        counts = list(frequent_map.items())

        def quick_select(left, right):
            pivot = left
            l, r = left, right
            while l < r:
                while l < r and counts[r][1] <= counts[pivot][1]:
                    r -= 1
                while l < r and counts[l][1] >= counts[pivot][1]:
                    l += 1
                counts[l], counts[r] = counts[r], counts[l]
            counts[left], counts[l] = counts[l], counts[left]

            if l + 1 == k:
                return counts[:l + 1]
            elif l + 1 > k:
                return quick_select(left, l - 1)
            else:
                return quick_select(l + 1, right)

        return [c[0] for c in quick_select(0, len(counts) - 1)]
