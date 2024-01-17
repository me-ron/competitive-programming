class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        x=max(trips,key=lambda t:t[2])
        ans=[0]*x[2]
        for k,a,b in trips:
            ans[a]+=k
            if b<x[2]:
                ans[b]-=k
        print(ans)
        for i in range(len(ans)):
            if i!=0:
                ans[i]+=ans[i-1]
            if ans[i]>capacity:
                return False
        return True