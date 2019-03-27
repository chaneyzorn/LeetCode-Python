class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        M, N = len(word1), len(word2)
        dp = [i for i in range(N + 1)]

        for i in range(1, M + 1):
            prev, dp[0] = dp[0], i

            for j in range(1, N + 1):
                temp = dp[j]
                if word1[i-1] == word2[j-1]:
                    dp[j] = prev
                else:
                    dp[j] = min(dp[j], dp[j - 1], prev) + 1
                prev = temp
        return dp[N]

    # def minDistance(self, word1, word2):
    #     """
    #     :type word1: str
    #     :type word2: str
    #     :rtype: int
    #     """
    #     if not (word1 and word2):
    #         return len(word1 or word2)
    #     if word1[0] == word2[0]:
    #         return self.minDistance(word1[1:], word2[1:])
    #     replace = self.minDistance(word1[1:], word2[1:]) + 1
    #     insert = self.minDistance(word1, word2[1:]) + 1
    #     delete = self.minDistance(word1[1:], word2) + 1
    #     return min(replace, insert, delete)
