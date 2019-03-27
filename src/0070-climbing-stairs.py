class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev, prev_prev, ans = 1, 1, 1

        for i in range(2, n + 1):
            ans = prev_prev + prev
            prev, prev_prev = ans, prev
        return ans

    # def climbStairs(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     dp = [0] * (n + 1)
    #     dp[0], dp[1] = 1, 1
    #
    #     for i in range(2, n + 1):
    #         dp[i] = dp[i-2] + dp[i - 1]
    #     return dp[n]
