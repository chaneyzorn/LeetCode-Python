class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_count = {}
        for c in s:
            char_count[c] = char_count.get(c, 0) + 1

        count, odd = 0, 0
        for key, val in char_count.items():
            if val & 1:
                odd = 1
                count += max(0, val - 1)
            else:
                count += val
        return count + odd
