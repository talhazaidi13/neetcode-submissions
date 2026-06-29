class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num=[]
        for j in nums:
            if j in num:
                return True
            num.append(j)
        return False