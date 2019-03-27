class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        num_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(dig):
            if not dig:
                return []
            res = []
            for c in num_map[dig[0]]:
                for remain in dfs(dig[1:]) or [""]:
                    res.append(c + remain)
            return res

        return dfs(digits)
