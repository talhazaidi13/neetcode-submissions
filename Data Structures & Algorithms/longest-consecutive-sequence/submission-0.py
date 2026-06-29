class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        out = defaultdict(int)
        res=0
        for num in nums:
            if not out[num]:
                left = out[num-1]
                right = out[num+1]
                length = left + right + 1

                out[num] = length
                out[num-left] = length
                out[num+right] = length

                res = max(res, out[num])
        return res