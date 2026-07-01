class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # out = defaultdict(int)
        # res=0
        # for num in nums:
        #     if not out[num]:
        #         left = out[num-1]
        #         right = out[num+1]
        #         length = left + right + 1

        #         out[num] = length
        #         out[num-left] = length
        #         out[num+right] = length

        #         res = max(res, out[num])
        # return res

        if not nums:
            return 0
        nums.sort()
        streak = 1
        res = 1
        for i in range(1, len(nums)):
            difference = nums[i] - nums[i - 1]
            if difference == 1:
                streak += 1
                res = max(res, streak)
            elif difference == 0:
                continue
            else:
                streak=1
        return res
            