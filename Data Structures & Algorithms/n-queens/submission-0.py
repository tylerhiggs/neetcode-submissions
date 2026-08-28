class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        used_cols = [False for _ in range(n)]
        queen_cols = []
        def help():
            row = len(queen_cols)
            if row == n:
                res.append(["".join(['Q' if i == col else '.' for i in range(n)]) for col in queen_cols])
                return
            col_oob = [False for _ in range(n)]
            for q_row in range(row):
                q_col = queen_cols[q_row]
                diff = row - q_row
                oob_pos = q_col + diff
                oob_neg = q_col - diff
                if oob_pos < n:
                    col_oob[oob_pos] = True
                if oob_neg >= 0:
                    col_oob[oob_neg] = True
            for col in range(n):
                if used_cols[col]:
                    continue
                if col_oob[col]:
                    continue
                used_cols[col] = True
                queen_cols.append(col)
                help()
                queen_cols.pop()
                used_cols[col] = False
            
        help()
        return res
                
                
