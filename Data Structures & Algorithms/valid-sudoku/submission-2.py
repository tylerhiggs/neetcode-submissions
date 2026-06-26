class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            freq = [0 for _ in range(9)]
            for item in row:
                if item == '.':
                    continue
                freq[int(item) - 1] += 1
            if (len([f for f in freq if f > 1])):
                return False
        for c in range(9):
            freq = [0 for _ in range(9)]
            for r in range(9):
                if board[r][c] == '.':
                    continue
                freq[int(board[r][c]) - 1] += 1
            if (len([f for f in freq if f > 1])):
                return False
        for i in range(9): # which box l to r top to bottom
            freq = [0 for _ in range(9)]
            for j in range(9): # which item in box
                r = (i // 3) * 3 + (j // 3)
                c = (i % 3) * 3 + (j % 3)
                if board[r][c] == '.':
                    continue
                freq[int(board[r][c]) - 1] += 1
            if (len([f for f in freq if f > 1])):
                return False
        return True