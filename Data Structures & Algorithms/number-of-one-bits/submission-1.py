class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            if n & 1:
                res = res+1
            # res = res + (n%2)
            n = n>>1
        return res
