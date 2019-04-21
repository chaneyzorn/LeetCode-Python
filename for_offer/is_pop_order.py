class Solution:
    def IsPopOrder(self, pushV, popV):
        if not pushV:
            return False
        stack = []
        i = 0
        for c in pushV:
            stack.append(c)
            while i < len(popV) and stack[-1] == popV[i]:
                stack.pop()
                i += 1
        return True if not stack else False
