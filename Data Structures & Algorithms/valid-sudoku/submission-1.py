class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in board:
            used = []
            for cell in row:
                if cell == '.':
                    continue
                if cell in used:
                    return False
                used.append(cell)
        for col in range(9):
            used = []
            for row in range(9):
                cell = board[row][col]
                if cell == '.':
                    continue
                if cell in used:
                    return False
                used.append(cell)
        for box in range(9):
            used = []
            for cell in range(9):
                i = (box // 3) * 3 + cell // 3
                j = (box % 3) * 3 + cell % 3
                val = board[i][j]
                if val == '.':
                    continue
                if val in used:
                    return False
                used.append(val)
        return True
                