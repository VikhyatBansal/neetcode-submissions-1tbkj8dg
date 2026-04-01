class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 0
        l,r = 0,1
        while r<len(nums):
            if nums[l]==nums[r]:
                nums[r]=-101
            else:
                l=r
            r+=1
            
        for i in range(0,len(nums)):
            if nums[i]!=-101:
                nums[cnt]=nums[i]
                cnt+=1
        return cnt