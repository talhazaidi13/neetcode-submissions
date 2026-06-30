class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        i = 0   # minimum cost to reach two steps before
        j = 0   # minimum cost to reach one step before

        for step_cost in cost:
            current = step_cost + min(i, j)
            i = j
            j = current

        return min(i, j)