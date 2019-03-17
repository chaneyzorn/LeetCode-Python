class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m > n:
            return self.uniquePaths(n, m)
        res = [1] * m
        for i in range(1, n):
            for j in range(1, m):
                res[j] += res[j - 1]
        return res[-1]
