class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        rate = r
        while l<=r:
            mid = (l+r)//2
            hours = 0
            for p in piles:
                hours = hours + math.ceil(float(p) / mid)
            if hours <= h:
                res = min(rate, mid)
                r = mid-1
            else:
                l= mid+1
        return res