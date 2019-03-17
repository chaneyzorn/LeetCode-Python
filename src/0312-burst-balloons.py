class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        balls = [1] + [i for i in nums if i > 0] + [1]
        N = len(balls)
        dp = [[0] * N for _ in range(N)]

        for k in range(2, N):
            for left in range(N - k):
                right = left + k
                for i in range(left + 1, right):
                    dp[left][right] = max(
                        dp[left][right],
                        balls[left] * balls[i] * balls[right] + dp[left][i] + dp[i][right]
                    )
        return dp[0][N - 1]
