class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        N = len(candidates)
        candidates.sort()
        res = []

        def backtracking(nums, target, index, path):
            if target == 0:
                res.append(path)
                return
            for i in range(index, N):
                if nums[i] > target:
                    break
                backtracking(nums, target - nums[i], i, path + [nums[i]])

        backtracking(candidates, target, 0, [])
        return res
