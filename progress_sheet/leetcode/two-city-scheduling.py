class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: x[1] - x[0])
        ans = 0 
        n = len(costs)//2
        for i in range(n):
            ans += costs[i][1] + costs[i+n][0]
        return ans

        