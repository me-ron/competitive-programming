class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        ans=0
        s=set()
        m=0
        for i in flips:
            if i in s:
                s.pop(i)
            if len(s)==m:
                ans+=1
            s.add(i)
            m=max(i,m)
        return ans