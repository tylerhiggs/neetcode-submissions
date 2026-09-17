class Solution:
    '''
    [
    [1, 2, 2,  3 , 5],
    [3, 2, 3, [4], 4],
    [2, 4, 5,  3 , 1],
    [6, 7, 1,  4 , 5],
    [5, 1, 1,  2 , 4]
    ]

    [
    [False, False, False, False, True],
    [False, False, False, True,  True],
    [False, False, True,  True,  True],
    [True,  True,  True,  True,  True],
    [True,  True,  True,  True,  True]
    ]
    [
    [True, True,  True,  True,  True],
    [True, False, True,  True,  False],
    [True, True,  True,  False, False],
    [True, True,  False, False, False],
    [True, False, False, False, False]
    ]
    '''
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(i: int, j: int, visited: List[List[int]]):
            if i < 0 or i == len(heights) or j < 0 or j == len(heights[i]):
                return
            if visited[i][j]:
                return
            visited[i][j] = True
            if i + 1 < len(heights) and heights[i][j] <= heights[i+1][j]:
                dfs(i+1, j, visited)
            if i - 1 >= 0 and heights[i][j] <= heights[i-1][j]:
                dfs(i-1, j, visited)
            if j + 1 < len(heights[i]) and heights[i][j] <= heights[i][j+1]:
                dfs(i, j+1, visited)
            if j - 1 >= 0 and heights[i][j] <= heights[i][j-1]:
                dfs(i, j-1, visited)
        p_border = [(i, j) for i in range(len(heights)) for j in range(len(heights[i])) if i == 0 or j == 0]
        a_border = [(i, j) for i in range(len(heights)) for j in range(len(heights[i])) if i == len(heights) - 1 or j == len(heights[i]) - 1]
        p_visited = [[False for _ in row] for row in heights]
        for i, j in p_border:
            dfs(i, j, p_visited)
        a_visited = [[False for _ in row] for row in heights]
        for i, j in a_border:
            dfs(i, j, a_visited)
        res = []
        for i in range(len(p_visited)):
            for j in range(len(p_visited[i])):
                if not p_visited[i][j]:
                    continue
                if not a_visited[i][j]:
                    continue
                res.append([i, j])
        return res
        

            