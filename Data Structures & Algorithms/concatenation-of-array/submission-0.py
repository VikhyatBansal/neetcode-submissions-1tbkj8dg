class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        n = len(nums)
        ans = [0]*(2*n)
        k=0
        for i in range(0,2*n):
            ans[i]=nums[k]
            k+=1
            if k==n:
                k=0
        return ans