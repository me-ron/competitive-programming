class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans=float('inf')
        temp=0
        i=0
        for j in range(len(blocks)):
            temp+=blocks[j]=='W'
            if j-i+1>k:
                temp-=blocks[i]=='W'
                i+=1
            ans=min(temp,ans) if j-i+1==k else ans
        return ans
        