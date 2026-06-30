class Solution:
    def countBits(self, n: int) -> List[int]:
        array = []
        for i in range(n+1):
            res = 0
            while i:
                res = res + (i%2)
                i = i >> 1
            array.append(res)
        return array