class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ans=0
        i,j=0,0
        while i<len(g) and j<len(s):
            while j<len(s) and g[i]>s[j]:
                j+=1
            if j<len(s):
                ans+=1
            i+=1
            j+=1
        return ans