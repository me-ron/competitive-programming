class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        x=len(strs[0])
        strs="".join(strs)
        print(strs)
        count=set()
        for i in range(x,len(strs)):
            if ord(strs[i])<ord(strs[i-x]):
                count.add(i%x)
        
        return len(count)