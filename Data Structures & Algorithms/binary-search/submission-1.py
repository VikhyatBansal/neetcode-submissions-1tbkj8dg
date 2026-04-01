class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        mid = n//2
        low,high = 0,n-1
        while low<=high:
            if nums[mid]>target:
                high = mid-1
            elif nums[mid]<target:
                low = mid+1
            else:
                return mid
            mid = (low+high)//2
        return -1
