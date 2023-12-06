class Solution:
    def largestGoodInteger(self, num: str) -> str:
        i=0
        j=2
        ans=set()
        while j<len(num):
            if len(set(num[i:j+1]))==1:
                ans.add(num[i:j+1])
            i+=1
            j+=1
        return max(ans,key=int) if ans else ""