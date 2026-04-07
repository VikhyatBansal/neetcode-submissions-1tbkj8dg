class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        path = {}
        if obstacleGrid[0][0]==1 or obstacleGrid[row-1][col-1]==1:
            return 0
        def dfs(i,j):
            if i==row-1 and j==col-1:
                return 1
            elif 0<=i<row and 0<=j<col and obstacleGrid[i][j]==0:
                if (i,j) in path:
                    return path[(i,j)]
                path[(i,j)]=dfs(i+1,j)+dfs(i,j+1)

                return path[(i,j)]
            return 0

        return dfs(0,0)