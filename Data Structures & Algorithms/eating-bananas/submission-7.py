class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        check = float('inf')
        while l<=r:
            hr = 0
            m = (l+r)//2
            for banana in piles:
                if banana%m != 0:
                    hr+=1
                hr+=banana//m
            if hr>h:
                l = m+1
            else:
                check = m
                r = m-1
        return check

