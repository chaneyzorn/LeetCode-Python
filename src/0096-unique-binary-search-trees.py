class Solution(object):
    """
    G(n) = F(1, n) + ... + F(n, n)
    G(0) = 1
    G(1) = 1
    F(i, n) = G(i - 1) * G(n - i)
    G(n) = G(0) * G(n - 1) + ... + G(n - 1) * G(0)
    """

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[-1]
