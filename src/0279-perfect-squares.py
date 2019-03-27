class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]
        while len(dp) <= n:
            val = n
            k = int(len(dp) ** 0.5 + 1)
            for i in range(1, k):
                val = min(val, dp[-i * i])
            dp.append(val + 1)
        return dp[n]

    # def numSquares(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     dp = [0]
    #     for i in range(1, n + 1):
    #         j, val = 1, n
    #         while j * j <= i:
    #             val = min(val, dp[i - j * j] + 1)
    #             j += 1
    #         dp.append(val)
    #     return dp[n]
