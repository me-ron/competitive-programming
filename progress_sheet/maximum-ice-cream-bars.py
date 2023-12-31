class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans=0
        i=0
        while coins>0 and i<len(costs):
            coins-=costs[i]
            ans+=(coins>=0)
            i+=1
        return ans
        