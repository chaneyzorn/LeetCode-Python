class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        extend = "@#" + "#".join(s) + "#$"
        manacher = [1] * len(extend)

        center, right = 0, 0

        for i in range(1, len(extend) - 1):
            if i < right:
                manacher[i] = min(manacher[2 * center - i], right - i)
            while extend[i - manacher[i]] == extend[i + manacher[i]]:
                manacher[i] += 1
            if i + manacher[i] > right:
                center = i
                right = i + manacher[i]
        return sum([r // 2 for r in manacher])

    # def countSubstrings(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     ans, N = 0, len(s)
    #
    #     for c in range(2 * N - 1):
    #         l = c // 2
    #         r = l + c % 2
    #         while l >= 0 and r < N and s[l] == s[r]:
    #             ans += 1
    #             l -= 1
    #             r += 1
    #     return ans
