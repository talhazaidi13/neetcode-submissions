class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] = 1 + count[num]
            
        freq=[]
        for i in range(len(nums)+1):
            freq.append([])

        # freq = [[] for i in range(len(nums) + 1)]


        for num, cnt in count.items():
            freq[cnt].append(num)
        # arr.sort()
        
        
        res=[]
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
              res.append(num)
              if len(res)==k:
                 return res