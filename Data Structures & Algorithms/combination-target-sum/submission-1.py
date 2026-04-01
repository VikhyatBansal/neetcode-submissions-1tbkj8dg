class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        def dfs(i):
            if i>=len(nums):
                return
            sub.append(nums[i])
            s = sum(sub)
            if s==target:
                res.append(sub.copy())
            elif s<target:
                dfs(i)
            sub.pop()
            dfs(i+1)
        dfs(0)
        return res
