class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        curr_str, next_num = '', 0
        stack = []
        for c in s:
            if c == "[":
                stack.append(curr_str)
                stack.append(next_num)
                curr_str, next_num = '', 0
            elif c == "]":
                curr_num = stack.pop()
                prev_str = stack.pop()
                curr_str = prev_str + curr_num * curr_str
            elif c.isnumeric():
                next_num = next_num * 10 + int(c)
            else:
                curr_str += c
        return curr_str
