class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans, stack = 0, [-1]
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    ans = max(i - stack[-1], ans)
                else:
                    stack.append(i)
        return ans

    # def longestValidParentheses(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     l_count, r_count, curr_len, max_len = 0, 0, 0, 0
    #     for c in s:
    #         curr_len += 1
    #         if c == "(":
    #             l_count += 1
    #         else:
    #             r_count += 1
    #
    #         if l_count == r_count:
    #             max_len = max(curr_len, max_len)
    #
    #         elif r_count > l_count:
    #             l_count, r_count, curr_len = 0, 0, 0
    #
    #     l_count, r_count, curr_len = 0, 0, 0
    #     for c in s[::-1]:
    #         curr_len += 1
    #         if c == "(":
    #             l_count += 1
    #         else:
    #             r_count += 1
    #
    #         if l_count == r_count:
    #             max_len = max(curr_len, max_len)
    #
    #         elif r_count < l_count:
    #             l_count, r_count, curr_len = 0, 0, 0
    #
    #     return max_len
