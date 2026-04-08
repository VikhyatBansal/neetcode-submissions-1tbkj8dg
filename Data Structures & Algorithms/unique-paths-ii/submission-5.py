class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # grid = [[0 for _ in range(n)]for _ in range(m)]
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[row-1][col-1]==1:
            return 0
        cache = {}
        def dfs(i,j):
            if i==(row-1) and j==(col-1):
                return 1
            if 0<=i<row and 0<=j<col and obstacleGrid[i][j]!=1:
                if (i,j) not in cache:
                    cache[(i,j)] = dfs(i+1,j)+dfs(i,j+1)
                return cache[(i,j)]
                # return dfs(i+1,j)+dfs(i,j+1)
            return 0

        return dfs(0,0)