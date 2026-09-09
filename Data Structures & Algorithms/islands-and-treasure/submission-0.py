class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        visited = [[False for _ in row] for row in grid]
        dist = 1
        current = [(i, j) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] == 0]
        while current:
            new_current = []
            for i, j in current:
                for k, l in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if k < 0 or k == len(grid) or l < 0 or l == len(grid[k]):
                        continue
                    if grid[k][l] != inf:
                        continue
                    grid[k][l] = dist
                    new_current.append((k, l))
            dist += 1
            current = new_current
        

