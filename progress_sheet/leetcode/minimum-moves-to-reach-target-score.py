class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans=0
        for i in range(maxDoubles):
            if target==1:
                return ans
            ans+=target%2
            ans+=1
            target//=2
        return ans+target-1
            
        