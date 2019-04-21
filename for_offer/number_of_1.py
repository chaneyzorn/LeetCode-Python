class Solution:
    def NumberOf1(self, n):
        result = 0
        if n < 0:
            n = n & 0xffffffff
        while n:
            result += 1
            n = (n - 1) & n
        return result
