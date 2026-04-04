class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        check = 0

        while l<=r:
            hr = 0  
            m = (l+r)//2
            for pile in piles:
                if pile%m:
                    hr+=1
                hr+=pile//m
            if hr>h:
                l = m+1
            else:
                check = m
                r = m-1

        return check