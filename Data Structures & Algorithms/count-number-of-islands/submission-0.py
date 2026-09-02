class Solution:
    '''
    grid=[
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"],
    ]
    '''
    def numIslands(self, grid: List[List[str]]) -> int:
        l: List[Set[(int, int)]] = []
        visited = [[False for _ in row] for row in grid]
        def help(i=0, j=0):
            if i == -1 or i == len(grid):
                return
            if j == -1 or j == len(grid[i]):
                return
            if visited[i][j]:
                return
            if grid[i][j] == '0':
                return
            visited[i][j] = True
            help(i + 1, j)
            help(i - 1, j)
            help(i, j + 1)
            help(i, j - 1)
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '0' or visited[i][j]:
                    continue
                res += 1
                help(i, j)
        return res

            
