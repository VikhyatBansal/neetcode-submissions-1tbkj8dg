class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pair = []
        for i in points:
            x,y = i[0],i[1]
            dis = (x**2+y**2)**(1/2)
            pair.append([dis,[x,y]])
        heapq.heapify(pair)
        res = []
        for j in range(k):
            res.append(heapq.heappop(pair)[1])
        return res