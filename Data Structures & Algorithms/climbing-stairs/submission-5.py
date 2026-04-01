class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1]*n
        def cnt(curr):
            if curr>n:
                return 0
            elif curr==n:
                return 1
            elif cache[curr]!=-1:
                return cache[curr]
            else:
                cache[curr]=cnt(curr+1)+cnt(curr+2)
            return cache[curr]
        return cnt(0)