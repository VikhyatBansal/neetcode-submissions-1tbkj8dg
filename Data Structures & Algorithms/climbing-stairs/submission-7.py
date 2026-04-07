class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [0]*(n+1)
        def dfs(n):
            if n==0:
                return 0
            elif n==1:
                return 1
            elif n==2:
                return 2
            else:
                if cache[n]>0:
                    return cache[n]
                cache[n] = dfs(n-1)+dfs(n-2)
            return cache[n]
        # dfs(n)
        return dfs(n)