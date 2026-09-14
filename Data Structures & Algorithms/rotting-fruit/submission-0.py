class Solution:
    # [1, 0, 1]
    # [0, 2, 0]
    # [1, 0, 1]
    def orangesRotting(self, grid: List[List[int]]) -> int:
        current = [(i, j) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] == 2]
        res = 0
        while current:
            new_current = []
            res += 1
            fruit_was_contaminated = False
            for i, j in current:
                for row, col in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if row < 0 or row == len(grid) or col < 0 or col == len(grid[row]):
                        continue
                    if grid[row][col] != 1:
                        continue
                    fruit_was_contaminated = True
                    new_current.append((row, col))
                    grid[row][col] = 2
            current = new_current
            if not current and not fruit_was_contaminated:
                res -= 1
        return -1 if [val for row in grid for val in row if val == 1] else res