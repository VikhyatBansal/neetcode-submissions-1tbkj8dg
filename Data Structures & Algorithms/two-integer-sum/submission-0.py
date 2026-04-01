class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        store = {}
        idx = 0
        for i in nums:
            if i in store:
                res.append(store[i])
                res.append(idx)
            else:
                store[target-i] = idx
            idx+=1
        return res
