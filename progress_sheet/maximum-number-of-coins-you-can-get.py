from itertools import combinations
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        un=len(piles)//3
        piles.sort()
        ans=0
        for i in range(un,len(piles)-1,2):
            ans+=piles[i]
        return ans
        
        