class Solution:
    def climbStairs(self, n: int) -> int:
        c = [0]*n
        def dfs(i):
            if i>=n:
                return i==n
            # else:
            #     return 0
            if c[i]>0:
                return c[i]

            c[i]=dfs(i+1)+dfs(i+2)
            return c[i]
        return dfs(0)