class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n <= 0:
            return []

        res = []
        for i in range(n):
            for left in self.generateParenthesis(i):
                for right in self.generateParenthesis(n - 1 - i):
                    res.append("({}){}".format(left, right))
        return res

    # def generateParenthesis(self, n):
    #     """
    #     :type n: int
    #     :rtype: List[str]
    #     """
    #     res = []
    #
    #     def backtrack(pare, left, right):
    #         if len(pare) == n * 2:
    #             res.append(pare)
    #         if left < n:
    #             backtrack(pare + '(', left + 1, right)
    #         if right < left:
    #             backtrack(pare + ')', left, right + 1)
    #
    #     backtrack('', 0, 0)
    #     return res
