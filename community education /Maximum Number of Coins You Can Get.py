from itertools import combinations
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        un=int(len(piles)/3)
        piles.sort()
        ans=0
        lst=piles[un:]
        for i in range(un):
            ans+=lst[2*i]
        return ans
        
        
