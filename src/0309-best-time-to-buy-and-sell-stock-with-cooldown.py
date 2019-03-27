class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        b0 = -prices[0]
        b1 = b0
        s0 = s1 = s2 = 0

        for price in prices[1:]:
            b0 = max(b1, s2 - price)
            s0 = max(s1, b1 + price)
            b1, s2, s1 = b0, s1, s0

        return s0
