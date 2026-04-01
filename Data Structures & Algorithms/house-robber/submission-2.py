class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        cache = {}

        def dfs(ptr):
            if ptr < 0:
                return 0
            
            if ptr in cache:
                return cache[ptr]
            
            # Decision:
            # Rob this house
            rob = nums[ptr] + dfs(ptr - 2)
            
            # Skip this house
            skip = dfs(ptr - 1)
            
            cache[ptr] = max(rob, skip)
            return cache[ptr]

        return dfs(N - 1)