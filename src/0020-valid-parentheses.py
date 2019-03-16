class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        stack = []
        mapping = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        for c in s:
            if c in mapping:
                if mapping[c] != stack.pop() if stack else "#":
                    return False
            else:
                stack.append(c)
        return not stack
