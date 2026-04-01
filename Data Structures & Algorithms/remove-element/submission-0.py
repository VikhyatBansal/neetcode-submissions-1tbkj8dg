class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l,r = 0,1
        cnt = 0
        for i in nums:
            if i!=val:
                cnt+=1
        while r<len(nums):
            if nums[l]!=val and nums[r]==val:
                l+=1
            elif nums[l]!=val and nums[r]!=val:
                l+=1
            elif nums[l]==val and nums[r]!=val:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
            r+=1
        return cnt

