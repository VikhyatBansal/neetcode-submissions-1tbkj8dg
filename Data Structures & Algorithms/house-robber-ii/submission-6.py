class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums)==1:
            return nums[0]
        c1 = [0]*n
        c2 = [0]*n
        def dfs(i,nums,c):
            N = len(nums)
            if i>=N:
                return 0
            if c[i]>0:
                return c[i]
            c[i]=max(nums[i]+dfs(i+2,nums,c),dfs(i+1,nums,c))
            return c[i]
        return max(dfs(0,nums[1:],c1),dfs(0,nums[:n-1],c2))