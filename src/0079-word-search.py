class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not (board and word):
            return False
        if not board[0]:
            return False

        M = len(board)
        N = len(board[0])
        if M * N < len(word):
            return False

        def dfs(i, j, remain):
            if not remain:
                return True

            if not ((0 <= i < M) and (0 <= j < N) and board[i][j] == remain[0]):
                return False

            tmp = board[i][j]
            board[i][j] = "#"
            flag = False or dfs(i, j - 1, remain[1:]) \
                   or dfs(i, j + 1, remain[1:]) \
                   or dfs(i - 1, j, remain[1:]) \
                   or dfs(i + 1, j, remain[1:])
            board[i][j] = tmp
            return flag

        for i in range(M):
            for j in range(N):
                if board[i][j] == word[0]:
                    if dfs(i, j, word):
                        return True
        return False


if __name__ == '__main__':
    result = Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED")
    print(result)
