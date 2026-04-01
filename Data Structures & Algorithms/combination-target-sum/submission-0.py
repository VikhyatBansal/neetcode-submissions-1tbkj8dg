class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        def subsum(i):
            if i>=len(nums):
                return
            sub.append(nums[i])
            n=sum(sub)
            if n==target:
                res.append(sub.copy())
            elif n<target:
                subsum(i)
            sub.pop()
            # sub.pop()
            subsum(i+1)

        subsum(0)
        return res