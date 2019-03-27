class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        N = len(s)
        word_set = set(wordDict)
        len_set = set(len(word) for word in word_set)

        dp = [False] * (N + 1)
        dp[0] = True

        for i in range(1, N + 1):
            for j in len_set:
                if i - j < 0:
                    continue
                dp[i] = dp[i - j] and (s[i - j:i] in word_set)
                if dp[i]:
                    break
        return dp[N]
