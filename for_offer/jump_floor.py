class Solution:
    def jumpFloor(self, number):
        # 动态规划解法
        # dp[i] i阶台阶的跳法，求 dp[number]
        dp = [0] * (number + 1)
        dp[0], dp[1] = 1, 1

        for i in range(2, number + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[number]
