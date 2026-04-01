class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[0 for _ in range(n)]for _ in range(m)]
        def path(i,j):
            if i>=m or j>=n:
                return 0

            if i==m-1 and j==n-1:
                return 1

            if cache[i][j]>0:
                return cache[i][j]
            cache[i][j] =  path(i+1,j)+path(i,j+1)
            return cache[i][j]
        return path(0,0)