class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # x=1 ; out=[] ; zero_cnt =0
        # for i in range(len(nums)):
        #     if nums[i]:
        #         x=x*nums[i]
        #     else:
        #         zero_cnt = zero_cnt +1
        # if zero_cnt > 1:
        #      return [0] * len(nums)

        # for i in range(len(nums)):
        #     if zero_cnt:
        #         if nums[i]==0:
        #             x2=x
        #         else:
        #             x2=0
        #     else:
        #         x2=x/nums[i]

        #     out.append(int(x2))
        
        # return out

        out=[]
        for i in range(len(nums)):
            prod=1
            for j in range(len(nums)):
                if i == j:
                    continue
                prod = prod * nums[j]
            out.append(prod)
        return out

