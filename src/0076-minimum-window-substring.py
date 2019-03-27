class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not (s and t):
            return ""

        from collections import Counter
        dict_t = Counter(t)
        required = len(dict_t)

        filter_s = [(i, c) for i, c in enumerate(s) if c in dict_t]

        l, r, formed, window_count = 0, 0, 0, {}
        ans = (float("inf"), None, None)

        while r < len(filter_s):
            c = filter_s[r][1]
            window_count[c] = window_count.get(c, 0) + 1

            if window_count[c] == dict_t[c]:
                formed += 1

            while formed == required and l <= r:
                c = filter_s[l][1]

                start = filter_s[l][0]
                end = filter_s[r][0]
                if end - start + 1 < ans[0]:
                    ans = (end - start + 1, start, end)

                window_count[c] -= 1
                if window_count[c] < dict_t[c]:
                    formed -= 1
                l += 1

            r += 1
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]
