class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if not (s and p and len(s) >= len(p)):
            return []
        result = []
        p_map = {}
        for c in p:
            p_map[c] = p_map.get(c, 0) + 1

        start = end = 0
        count = len(p)
        while end < len(s):
            # 如果下一个字符无效，则不能 end++
            # 解决方法：归还 start end 之间的字符，并双双向前
            if s[end] not in p_map:
                while start < end:
                    p_map[s[start]] += 1
                    start += 1
                    count += 1
                start += 1
                end += 1
                continue

            # 需要的字符被耗光，则不能 end++
            # 解决办法：归还直到有指定的字符可用
            while p_map[s[end]] <= 0:
                p_map[s[start]] += 1
                start += 1
                count += 1
            else:  # 终于可以正常的消耗一个p中的字符了
                p_map[s[end]] -= 1
                end += 1
                count -= 1
                # 如果已经耗尽了 p 中的字符，则不能 end++
                # 解决办法：归还一个start位置的字符
                if count == 0:
                    result.append(start)
                    p_map[s[start]] += 1
                    start += 1
                    count += 1
        return result


if __name__ == '__main__':
    result = Solution().findAnagrams("abab", "ab")
    print(result)
