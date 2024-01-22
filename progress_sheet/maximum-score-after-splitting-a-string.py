class Solution:
    def maxScore(self, s: str) -> int:
        ones=s.count('1')
        before=0
        zeros=0
        big=0
        for i in range(len(s)-1):
            zeros+=(s[i]=='0')
            before+=(s[i]=='1')
            temp=zeros+(ones-before)
            big=max(big,temp)
        return big
        