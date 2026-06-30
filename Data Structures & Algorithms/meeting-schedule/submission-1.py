"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        def divide(intervals):
            if len(intervals)<=1:
                return intervals
            mid= len(intervals)//2
            left = divide(intervals[:mid])
            right = divide(intervals[mid:])
            return merge(left, right)

        def merge(left, right):
            i, j=0,0
            array=[]
            while i<len(left) and j<len(right):
                if left[i].start <= right[j].start:
                    array.append(left[i])
                    i += 1
                else:
                    array.append(right[j])
                    j += 1
            array.extend(left[i:])
            array.extend(right[j:])
            return array

        res = divide(intervals)

        for i in range(1, len(res)):
            if res[i].start < res[i-1].end:
                return False
        return True

