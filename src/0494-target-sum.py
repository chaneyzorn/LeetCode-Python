class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        # 如果交换正负号，那么就会得到对应的正负S，这样并不会影响最后的方案数
        S = abs(S)
        total = sum(nums)

        # 正数部分 - 负数部分 = S
        # 2x正数部分 = S + 负数部分 + 正数部分 = S + sum(nums)
        # 正数部分 = [S + sum(nums)] / 2

        # 如果总和都无法满足方案，或者上述无法整除2，则说明没有满足的方案
        if total < S or ((total + S) & 1) == 1:
            return 0

        # 以正数部分为目标，求给定集合中，有多少种方案可以拼凑出 target
        target = (total + S) // 2

        # dp[i][j] : 在前 i 个元素中，可以拼凑出 j 的方法种数
        # dp[i][j] = dp[i - 1][j] + dp[i - 1][j -nums[i]]
        # 前 i - 1 个元素即可拼凑出 j，或者可以拼凑出 j - nums[i]

        dp = [0] * (target + 1)
        dp[0] = 1  # 前任意个元素都可以拼凑出0，即正数部分不包含任何元素

        for num in nums:
            for i in range(target, num - 1, -1):
                # [i - 1] 对于 [i] 表示上一次循环的结果，优化为一维空间
                # 倒序以防止覆盖上一次循环结果
                dp[i] += dp[i - num]
        return dp[target]

    # def findTargetSumWays(self, nums, S):
    #     """
    #     :type nums: List[int]
    #     :type S: int
    #     :rtype: int
    #     """
    #     N = len(nums)
    #     self.ans = 0
    #
    #     def recurse(curr, index):
    #         if index == N:
    #             if curr == S:
    #                 self.ans += 1
    #         else:
    #             recurse(curr + nums[index], index + 1)
    #             recurse(curr - nums[index], index + 1)
    #
    #     recurse(0, 0)
    #     return self.ans
