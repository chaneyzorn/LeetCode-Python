class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = prices and prices[0] or 0
        max_profit = 0
        for price in prices:
            if price < buy:
                buy = price
            elif max_profit < price - buy:
                max_profit = price - buy
        return max_profit
