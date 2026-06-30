class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        array = [-i for i in nums] 
        heapq.heapify(array)
        res=[]
        # if len(array) == 1:
        #     res.append(-1*heapq.heappop(array))
        # if len(array)<=k:
        #     res.extend(nums)
        #     print('in less res ',res)
        #     print('in less nums ',nums)
        #     print('inless  len(array) ',len(array))

        while array:
            res.append(-heapq.heappop(array))
            # print('in res ',res)
            # print('in len(array) ',len(array))


        print(res)
        return res[k-1]