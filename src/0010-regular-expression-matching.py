class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[-1][-1] = True

        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                match = i < len(s) and p[j] in {s[i], "."}
                if j + 1 < len(p) and p[j + 1] == "*":
                    dp[i][j] = dp[i][j + 2] or (match and dp[i + 1][j])
                else:
                    dp[i][j] = match and dp[i + 1][j + 1]
        return dp[0][0]

    # def isMatch(self, s, p):
    #     """
    #     :type s: str
    #     :type p: str
    #     :rtype: bool
    #     """
    #     memo = {}
    #
    #     def dp(i, j):
    #         if (i, j) not in memo:
    #             if j == len(p):
    #                 ans = i == len(s)
    #             else:
    #                 match = i < len(s) and p[j] in (s[i], ".")
    #                 if j + 1 < len(p) and p[j + 1] == "*":
    #                     ans = dp(i, j + 2) or (match and dp(i + 1, j))
    #                 else:
    #                     ans = match and dp(i + 1, j + 1)
    #             memo[(i, j)] = ans
    #         return memo[(i, j)]
    #
    #     return dp(0, 0)

    # def isMatch(self, s, p):
    #     """
    #     :type s: str
    #     :type p: str
    #     :rtype: bool
    #     """
    #     if not p:
    #         return not s
    #
    #     match = s and p[0] in {s[0], "."}
    #
    #     if len(p) >= 2 and p[1] == "*":
    #         return self.isMatch(s, p[2:]) or (match and self.isMatch(s[1:], p))
    #     else:
    #         return match and self.isMatch(s[1:], p[1:])
