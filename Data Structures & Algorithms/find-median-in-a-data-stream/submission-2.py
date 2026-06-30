class MedianFinder:

    def __init__(self):
        self.array = []

    def addNum(self, num: int) -> None:
        self.array.append(num)
        self.array.sort()

    def findMedian(self) -> float:
        if len(self.array) % 2 ==0:
            mid1 = len(self.array)//2
            mid2 = mid1-1
            return (self.array[mid1] + self.array[mid2] )/2
        else:
            mid = len(self.array)//2
            return self.array[mid]
        
        