class Solution:
    def jumpFloorII(self, number):
        # dp[i] i阶台阶的跳法，求 dp[number]
        dp = [0] * (number + 1)
        dp[0], dp[1] = 1, 1

        for i in range(2, number + 1):
            # dp[i] = sum(dp[:i]) = sum(dp[:i-1]) + dp[i-1] = dp[i - 1] * 2
            dp[i] = dp[i - 1] * 2
        return dp[number]
