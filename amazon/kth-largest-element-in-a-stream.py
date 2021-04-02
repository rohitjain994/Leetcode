class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for i in range(len(nums)):
            if i < k:
                heapq.heappush(self.heap,nums[i])
            elif nums[i] > self.heap[0]:
                heapq.heappushpop(self.heap,nums[i])

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap,val)
        elif val > self.heap[0]:
                heapq.heappushpop(self.heap,val)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)