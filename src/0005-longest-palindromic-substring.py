class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        et = "@#" + "#".join(s) + "#$"
        manacher = [1] * len(et)

        center, right = 0, 0
        max_i, max_r = 0, 1
        for i in range(1, len(et) - 1):
            if i < right:
                manacher[i] = min(right - i, manacher[2 * center - i])
            while et[i + manacher[i]] == et[i - manacher[i]]:
                manacher[i] += 1
            if i + manacher[i] > right:
                center, right = i, i + manacher[i]
            if manacher[i] > max_r:
                max_i, max_r = i, manacher[i]
        start = (max_i - max_r) // 2
        end = start + max_r - 1
        return s[start:end]
