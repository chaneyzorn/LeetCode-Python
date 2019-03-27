class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        l_no_match, r_no_match, result = 0, 0, set()

        for c in s:
            if c == "(":
                l_no_match += 1
            elif c == ")":
                r_no_match = (r_no_match + 1) if l_no_match == 0 else r_no_match
                l_no_match = (l_no_match - 1) if l_no_match > 0 else l_no_match

        def recurse(s, index, l_todo, r_todo, l_count, r_count, expr):
            if index == len(s):
                if l_todo == r_todo == 0:
                    result.add("".join(expr))
            else:
                if (s[index] == "(" and l_todo) or (s[index] == ")" and r_todo):
                    recurse(s, index + 1,
                            l_todo - (s[index] == "("),
                            r_todo - (s[index] == ")"),
                            l_count, r_count, expr)

                expr.append(s[index])
                if s[index] not in ("(", ")"):
                    recurse(s, index + 1, l_todo, r_todo, l_count, r_count, expr)
                elif s[index] == "(":
                    recurse(s, index + 1, l_todo, r_todo, l_count + 1, r_count, expr)
                elif s[index] == ")" and l_count > r_count:
                    recurse(s, index + 1, l_todo, r_todo, l_count, r_count + 1, expr)
                expr.pop()

        recurse(s, 0, l_no_match, r_no_match, 0, 0, [])

        return list(result)
