class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic=defaultdict(int)
        i=0
        j=0
        ans=0
        max_len=0
        for j in range(len(s)):
            dic[s[j]]+=1
            max_len=max(max_len,dic[s[j]])
            if j-i+1-max_len>k:
                dic[s[i]]-=1
                i+=1
            ans=max(j-i+1,ans)
        return ans
            
        
        