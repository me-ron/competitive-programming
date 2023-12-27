class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        ans=0
        s=0
        m=0
        for i in flips:
            if s==m:
                ans+=1
            s+=1
            m=max(i,m)
        return ans