class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        used = [[False for _ in row] for row in board]
        def help(i=0, j=0, k=0) -> bool:
            if k == len(word):
                return True
            if i == len(board) or i < 0 or j < 0 or j == len(board[i]):
                return False
            if board[i][j] != word[k] or used[i][j]:
                return False
            used[i][j] = True
            res = help(i+1, j, k+1) or help(i-1, j, k+1) or help(i, j+1, k+1) or help(i, j-1, k+1)
            used[i][j] = False
            return res
        for i in range(len(board)):
            for j in range(len(board[i])):
                if help(i, j):
                    return True
        return False
            
             