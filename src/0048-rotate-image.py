class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return []
        d = len(matrix[0])
        for i in range(d):
            for j in range(d):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(d):
            for j in range(d // 2):
                matrix[i][j], matrix[i][d - 1 - j] = matrix[i][d - 1 - j], matrix[i][j]
