class MedianFinder:

    def __init__(self):
        self.small = []   # max heap using negatives
        self.large = []   # min heap

    def addNum(self, num: int) -> None:
        # Put number in small heap first
        heapq.heappush(self.small, -num)

        # Move the largest value from small to large
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # Keep small equal in size or one element larger
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        # Odd number of elements
        if len(self.small) > len(self.large):
            return -self.small[0]

        # Even number of elements
        return (-self.small[0] + self.large[0]) / 2
        