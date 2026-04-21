class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        s = 0
        while l<=r:
            m = (l+r)//2
            track = 0
            for banana in piles:
                track += banana//m
                if banana%m!=0:
                    track+=1
                if track>h:
                    break
            if track<=h:
                s = m
                r = m-1
            elif track>h:
                l = m+1

        return s
