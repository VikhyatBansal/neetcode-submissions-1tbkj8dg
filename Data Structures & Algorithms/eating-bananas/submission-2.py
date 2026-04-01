class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        low = 1
        high = max(piles)
        checkpoint = 0
        while low<=high:
            mid = (low+high)//2
            h_temp = 0
            idx = 0
            while h_temp<=h and idx<n:
                # print()
                if mid<piles[idx]:
                    if piles[idx]%mid != 0:
                        h_temp+=1   
                    h_temp = h_temp+(piles[idx]//mid)
                else:
                    h_temp+=1
                idx+=1
            # h_max = max(h_temp,h_max)
            # print(low,high,mid)
            # print(h_temp,h)
            # print('-----')
            if h_temp>h:
                low = mid+1
            else:
                high = mid-1
                checkpoint = mid
        return max(checkpoint,mid)
            
