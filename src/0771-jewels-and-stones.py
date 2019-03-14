class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        JSet = set(c for c in J)
        for s in S:
            if s in JSet:
                count += 1
        return count
