class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not (matrix and matrix[0]):
            return 0

        max_area = 0
        heights = [0] * len(matrix[0]) + [0]

        for row in matrix:
            stack = [-1]
            for index, val in enumerate(row + [0]):
                if val == "1":
                    heights[index] += 1
                else:
                    heights[index] = 0

                while heights[index] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = index - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(index)
        return max_area
