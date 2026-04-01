class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            hm[target - nums[i]] = i
        print(hm)
        for j in range(len(nums)):
            if nums[j] in hm and hm[nums[j]]!=j:
                return [j,hm[nums[j]]]