class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # grid = [[0 for _ in range(n)]for _ in range(m)]
        cache = {}
        def dfs(i,j):
            if i==(m-1) and j==(n-1):
                return 1
            if 0<=i<m and 0<=j<n:
                if (i,j) not in cache:
                    cache[(i,j)] = dfs(i+1,j)+dfs(i,j+1)
                return cache[(i,j)]
                # return dfs(i+1,j)+dfs(i,j+1)
            return 0

        return dfs(0,0)