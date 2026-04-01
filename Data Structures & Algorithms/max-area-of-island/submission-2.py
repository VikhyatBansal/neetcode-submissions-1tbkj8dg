class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        def dfs(i,j):
            if 0<=i<row and 0<=j<col and grid[i][j]==1:
                grid[i][j]=0
                return 1+dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1)
            else:
                return 0


        area = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    area = max(area, dfs(i,j))
        return area