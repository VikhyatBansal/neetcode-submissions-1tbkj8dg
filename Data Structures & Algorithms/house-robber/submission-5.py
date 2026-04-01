class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        N=len(nums)
        def dfs(ptr):
            if ptr>=N:
                return 0
            if ptr in cache:
                return cache[ptr]

            rob = nums[ptr]+dfs(ptr+2)
            skip = dfs(ptr+1)
            cache[ptr] = max(rob,skip)
            return cache[ptr]

        return dfs(0)