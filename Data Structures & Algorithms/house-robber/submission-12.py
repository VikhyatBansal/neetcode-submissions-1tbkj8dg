class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        c = [0]*n
        def dfs(i):
            if i>=n:
                return 0
            if c[i]>0:
                return c[i]
            c[i]=max(nums[i]+dfs(i+2),dfs(i+1))
            return c[i]
        return dfs(0)