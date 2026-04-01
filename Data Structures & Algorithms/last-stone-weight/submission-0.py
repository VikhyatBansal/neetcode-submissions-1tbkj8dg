class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -1*stones[i]
        heapq.heapify(stones)
        # print(stones)
        if stones:
            while len(stones)>1:
                x = -1*heapq.heappop(stones)
                y = -1*heapq.heappop(stones)
                if x>y:
                    heapq.heappush(stones,-1*(x-y))
                elif y>x:
                    heapq.heappush(stones,-1*(y-x))        
        if stones:
            return -1*stones[0]
        return 0
