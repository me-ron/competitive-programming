class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t=Counter(t)
        i=0
        dis=len(s)+3
        x,y=0,0
        for j in range(len(s)):
            if s[j] in t:
                t[s[j]]-=1
            while all([t[ch]<=0 for ch in t]) and i<len(s):
                if dis>j-i+1:
                    dis=j-i+1
                    x,y=i,j
                if s[i] in t:
                    t[s[i]]+=1
                i+=1
        return s[x:y+1] if dis<=len(s) else ""
                    
        
        