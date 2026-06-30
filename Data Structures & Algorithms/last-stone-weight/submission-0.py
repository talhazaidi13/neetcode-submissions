class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = []
        for i in stones:
            arr.append(-1*i)
        heapq.heapify(arr)

        while len(arr)>1:
            lar1 = -1 *  heapq.heappop(arr)
            lar2 = -1 *  heapq.heappop(arr)

            if abs(lar1 - lar2):
                if lar1 < lar2:
                    new = (lar2-lar1)
                    heapq.heappush(arr, -1*new)
                else:
                    new = (lar1-lar2)
                    heapq.heappush(arr, -1*new)

        if len(arr) == 1:
            return -heapq.heappop(arr)

        return 0