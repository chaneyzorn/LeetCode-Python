class Solution:
    def rectCover(self, number):
        if not number:
            return 0
        dp = [0] * (number + 1)
        dp[0], dp[1] = 1, 1

        for i in range(2, number + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[number]
