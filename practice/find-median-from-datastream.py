class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        using 2 heap apprach as
        pq1 : max heap 
        pq2 : min heap 
        pq1[0] will return max of first half 
        pq2[0] will return min of 2nd half
        """
        self.pq1 = []
        self.pq2 = []
        self.p1 = 0
        self.p2 = 0
        

    def addNum(self, num: int) -> None:
        """
            if size of both heap is same // means even 
                check pq1[0] < pq2[0] < num
                    pop from pq2 and push it to pq1
                    push it to pq2
                else: push it pq1
            else:
                check pq1[0]<num
                    push it to pq2
                else:
                    pop it from pq1 and push it to pq2
                    push it to pq1
                    

        """
            if self.p1 == self.p2:
                if self.pq1 and -1*self.pq1[0] < num and self.pq2 and num > self.pq2[0]:
                    heapq.heappush(self.pq1,-1*heapq.heappop(self.pq2))
                    heapq.heappush(self.pq2,num)
                else:
                    heapq.heappush(self.pq1,-1*num)
                self.p1 +=1
            else:
                if self.pq1 and -1*self.pq1[0] < num:
                    heapq.heappush(self.pq2,num)
                else:
                    heapq.heappush(self.pq2,-1*heapq.heappop(self.pq1))
                    heapq.heappush(self.pq1,-1*num)    
                self.p2 +=1
        

    def findMedian(self) -> float:
        # print(self.pq1,self.pq2)
        """
            if even : pq1[0]+pq2[0]/2
            else: pq1[0]
        """
        if self.p1 == self.p2:
            return (-1*self.pq1[0] + self.pq2[0]) / 2
        return -1*self.pq1[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()