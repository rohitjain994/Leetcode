class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for x,y in points:
            heapq.heappush(pq,(x*x + y*y , x , y))
        res = []
        for i in range(k):
            r,x,y = heapq.heappop(pq)
            res.append([x,y])
        return res