class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        r = len(obstacleGrid)
        c = len(obstacleGrid[0])
        cache = [[0 for _ in range(c)]for _ in range(r)]
        def paths(r,c,rows,cols,cache):
            if r==rows or c==cols or obstacleGrid[r][c]==1:
                return 0
            if r==rows-1 and c==cols-1:
                return 1
            if cache[r][c]>0:
                return cache[r][c]
            cache[r][c] = paths(r+1,c,rows,cols,cache)+paths(r,c+1,rows,cols,cache)
            return cache[r][c]
        return paths(0,0,r,c,cache)