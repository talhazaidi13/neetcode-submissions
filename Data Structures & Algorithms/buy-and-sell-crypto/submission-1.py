class Solution:
    def maxProfit(self, prices: List[int]) -> int:

    ##################################################
    #### BRUTE FORCE
        # diff = 0
        # diff_array = []
        # streak = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #          diff = max(diff, prices[j]-prices[i])
        # return diff
            
    ##################################################
    #### Dynamic programming
        # res = 0
        # min_buy=prices[0]
        # for i in prices:
        #     res = max(res, i - min_buy)
        #     min_buy = min(min_buy, i)
        # return res

    ##################################################
    #### Two pointers
        
        l=0
        r=1
        res = 0
        while r<len(prices):
            buy = prices[l]
            if prices[l] < prices[r]:
               res = max(res, prices[r]-prices[l])
            else:
                l=r
            r=r+1
        return res
