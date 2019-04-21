class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # c 风格思路
        s_arr = [c for c in s]

        space_count = 0
        for c in s_arr:
            if c == " ":
                space_count += 1

        new_len = len(s) + space_count * 2
        new_arr = [""] * new_len
        for c in s_arr[::-1]:
            new_len -= 1
            if c == " ":
                new_arr[new_len] = "0"
                new_len -= 1
                new_arr[new_len] = "2"
                new_len -= 1
                new_arr[new_len] = "%"
            else:
                new_arr[new_len] = c
        return "".join(new_arr)
