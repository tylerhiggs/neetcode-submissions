class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, m * n - 1
        def ind(row, col):
            return row * n + col
        def pos(idx):
            return idx // n, idx % n
        
        while i < j:
            mid = (i + j) // 2
            mid_row, mid_col = pos(mid)
            
            if matrix[mid_row][mid_col] < target:
                i = mid + 1
                continue
            if matrix[mid_row][mid_col] > target:
                j = mid - 1
                continue
            return True
        row_i, col_i = pos(i)
        row_j, col_j = pos(j)
        return matrix[row_i][col_i] == target or matrix[row_j][col_j] == target
        