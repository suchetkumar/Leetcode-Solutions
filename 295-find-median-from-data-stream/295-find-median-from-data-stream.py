from heapq import heapify, heappush, heappop
class MedianFinder:
    # have a min heap and a max heap
    # peek the front of both
    # keep the size of both heaps
    def __init__(self):
        # mins is a max heap of lower values
        self.mins = []
        self.minsize = 0
        #maxs is a min heap of upper values
        self.maxs = []
        self.maxsize = 0
        
        heapify(self.mins)
        heapify(self.maxs)
        

    def addNum(self, num: int) -> None:
        heappush(self.mins, -num)
        self.minsize += 1
        if self.minsize > self.maxsize+1:
            x = heappop(self.mins)
            self.minsize -= 1
            heappush(self.maxs, -x)
            self.maxsize += 1
            
        if self.maxsize and -self.mins[0] > self.maxs[0]:
            x = heappop(self.mins)
            y = heappop(self.maxs)
            heappush(self.mins, -y)
            heappush(self.maxs, -x)

    def findMedian(self) -> float:
        if self.minsize == self.maxsize:
            return (-self.mins[0]+self.maxs[0])/2
        return -self.mins[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()