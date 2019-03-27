class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        row = len(matrix)
        col = len(matrix[0])

        if not (row and col):
            return 0

        dp = [0] * (col + 1)
        prev, max_len = 0, 0
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                tmp = dp[j]
                if matrix[i - 1][j - 1] == '1':
                    dp[j] = min(dp[j - 1], dp[j], prev) + 1
                else:
                    dp[j] = 0
                max_len = max(max_len, dp[j])
                prev = tmp
        return max_len * max_len
