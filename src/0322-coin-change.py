class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not amount:
            return 0
        if not coins:
            return -1

        dp = [0] * (amount + 1)

        for i in range(1, amount + 1):
            imin = float("inf")
            for coin in coins:
                if (i - coin) >= 0 and (0 <= dp[i - coin] < imin):
                    imin = dp[i - coin]
            dp[i] = (imin + 1) if imin != float("inf") else -1

        return dp[amount]

    # def coinChange(self, coins, amount):
    #     """
    #     :type coins: List[int]
    #     :type amount: int
    #     :rtype: int
    #     """
    #     if not amount:
    #         return 0
    #     if not coins:
    #         return -1
    #
    #     memo = {}
    #
    #     def recurse(remain):
    #         if remain < 0:
    #             return -1
    #         if remain == 0:
    #             return 0
    #         if remain not in memo:
    #             min_count = float("inf")
    #             for coin in coins:
    #                 imin = recurse(remain - coin)
    #                 if 0 <= imin < min_count:
    #                     min_count = imin + 1
    #             memo[remain] = min_count if min_count != float("inf") else -1
    #         return memo[remain]
    #
    #     return recurse(amount)
