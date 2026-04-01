class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cache = [0]*n
        nums.append(0)
        # print(cache)
        def maxamt(i,cache):
            # print(cache)
            if i>=n:
                return 0
            else:
                if cache[i]>0:
                    return cache[i]
                cache[i] = max(nums[i]+maxamt(i+2,cache),nums[i+1]+maxamt(i+3,cache))
            # print(cache)
            # print('----')
            return cache[i]
        return maxamt(0,cache)