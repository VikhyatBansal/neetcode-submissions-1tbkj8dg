class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []
        def dfs(i):
            if i>=len(nums):
                res.append(sub[:])
                return
            dfs(i+1)
            sub.append(nums[i])
            dfs(i+1)
            sub.pop()
        dfs(0)
        return res