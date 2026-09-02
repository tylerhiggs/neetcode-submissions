class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = [[False for _ in row] for row in grid]
        res = 0

        def help(i: int, j: int) -> int:
            if i == -1 or i == len(grid):
                return 0
            if j == -1 or j == len(grid[i]):
                return 0
            if visited[i][j] or grid[i][j] == 0:
                return 0
            visited[i][j] = True
            return 1 + help(i + 1, j) + help(i - 1, j) + help(i, j + 1) + help(i, j - 1)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if visited[i][j] or grid[i][j] == 0:
                    continue
                res = max(res, help(i, j))

        return res