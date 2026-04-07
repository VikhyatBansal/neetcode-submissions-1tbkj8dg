class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]
        # print(grid)
        def dfs(i,j):
            if i==m-1 and j==n-1:
                return 1
            elif 0<=i<m and 0<=j<n:
                # grid[i][j]=1
                if grid[i][j]>0:
                    return grid[i][j]
                grid[i][j] =  dfs(i+1,j)+dfs(i,j+1)
                return grid[i][j]
            return 0

        return dfs(0,0)

