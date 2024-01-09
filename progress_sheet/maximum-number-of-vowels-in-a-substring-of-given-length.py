class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vow={'a', 'e', 'i', 'o','u'}
        c,ans=0,0
        i=0
        print(len(s))
        for j in range(len(s)):
            c+=s[j] in vow
            if j-i+1>k:
                c-=s[i] in vow
                ans=max(ans,c)
                i+=1
            ans=max(ans,c)
        return ans
             
            
        