class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t=Counter(t)
        i=0
        ans=s+"rew"
        for j in range(len(s)):
            if s[j] in t:
                t[s[j]]-=1
            while all([t[ch]<=0 for ch in t]) and i<len(s):
                ans=min(ans,s[i:j+1],key=len)
                if s[i] in t:
                    t[s[i]]+=1
                i+=1
        return ans if len(ans)<=len(s) else ""
                    
        
        