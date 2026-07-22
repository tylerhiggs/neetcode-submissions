class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, m * n - 1 # inclusive
        while i < j:
            mid = (i + j) // 2
            midi = mid // n
            midj = mid % n

            if matrix[midi][midj] == target:
                return True
            if matrix[midi][midj] < target:
                i = mid + 1
                continue
            j = mid - 1
        return matrix[i // n][i % n] == target or matrix[j // n][j % n] == target