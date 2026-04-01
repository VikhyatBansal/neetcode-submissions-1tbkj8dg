class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [0]*n
        def dfs(i,cache):
            if i<=0:
                return 0
            elif i==1:
                return 1
            elif i==2:
                return 2
            else:
                if cache[i-1]>0:
                    return cache[i-1]
                cache[i-1] = dfs(i-1,cache)+dfs(i-2,cache)
                return cache[i-1]
        return dfs(n,cache)