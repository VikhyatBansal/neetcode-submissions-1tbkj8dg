class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N==1:
            return nums[0]
        cache = {}
        def dfs(ptr):
            if ptr<0:
                return 0
            if ptr in cache:
                return cache[ptr]
            rob = nums[ptr]+dfs(ptr-2)
            skip = dfs(ptr-1)
            cache[ptr] = max(rob,skip)
            return cache[ptr]
        return dfs(N-1)
