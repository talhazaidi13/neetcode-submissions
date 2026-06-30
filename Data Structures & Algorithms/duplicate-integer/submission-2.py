class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num={}
        for i in range(len(nums)):
            num[nums[i]] = num.get(nums[i],0) + 1
            if num[nums[i]] > 1:
                return True
        return False