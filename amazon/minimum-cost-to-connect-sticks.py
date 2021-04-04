def connect(nums):
    li = []
    cost = 0
    for i in range(len(nums)):
        heapq.heappush(li,nums[i])
    while len(li)>1:
        res = heapq.heappop(li) + heapq.heappop(li)
        cost+=res
        heapq.heappush(li,res)
    return cost

# cost to connect sticks such that cost = X+Y
# nums = [1,8,3,5]
# cost = 4 , li = 4,5,8
# cost = 4+9 = 13 , li = 8,9
# cost = 4+9+17 = 30 , li = 30