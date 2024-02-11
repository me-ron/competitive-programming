class Solution:
    def bestClosingTime(self, customers: str) -> int:
        ans=[0]*len(customers)
        N=Y=0
        n=len(customers)
        for i in range(n):
            ans[n-i-1]+=Y
            N+=customers[i]=="N"
            Y+=customers[n-i-1]=="Y"   
            ans[i]+=N

        ans=[Y]+ans
        x=2*n
        j=0
        for i in range(len(ans)):
            if ans[i]<x:
                j=i
                x=ans[i]
        return j
        