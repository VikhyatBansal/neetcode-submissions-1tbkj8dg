class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        cache = [[0 for _ in range(col)]for _ in range(row)]
        def path(i,j):
            if i>=row or j>=col or obstacleGrid[i][j]==1:
                return 0
            if i==row-1 and j==col-1:
                return 1
            if cache[i][j]>0:
                return cache[i][j]
            
            cache[i][j] = path(i+1,j)+path(i,j+1)
            return cache[i][j]

        return path(0,0)