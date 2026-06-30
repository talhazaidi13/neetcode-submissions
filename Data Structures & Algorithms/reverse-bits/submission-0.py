class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            shifted_n = n >> i
            bit = shifted_n & 1

            new_position = 31 - i
            shifted_bit = bit << new_position

            res = res + shifted_bit

        return res