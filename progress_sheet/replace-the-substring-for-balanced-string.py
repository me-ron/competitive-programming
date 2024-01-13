class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)//4
        l, ans, count = 0,float('inf'), Counter(list(s))
        have={ch:count[ch]-n for ch in count if count[ch]>n}
        
        for r in range(len(s)):
            if s[r] in have:
                have[s[r]] -= 1
            while all(value <= 0 for value in have.values()) and l < len(s):
                if  s[l] in have:
                    have[s[l]] += 1
                ans = min(ans, r - l + 1)
                l += 1
               
        return ans if (ans != float('inf') and ans > 0) else 0