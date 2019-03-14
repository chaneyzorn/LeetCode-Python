class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        count = 0
        result = x ^ y
        while result:
            if result & 1 == 1:
                count += 1
            result = result >> 1

        return count
