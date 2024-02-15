class Solution:
    def longestPalindrome(self, s: str) -> int:
        c=Counter(s)
        odd=0
        ans=0
        for i in c:
            if c[i]%2:
                odd+=1 
            ans+=c[i]
        odd -= 1 if odd else 0
        return ans-odd
