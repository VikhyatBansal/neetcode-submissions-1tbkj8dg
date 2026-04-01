class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm = {}
        for i in nums:
            if i not in hm:
                hm[i] = 1
            else:
                return True
        return False