class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)//4
        l, ans, count = 0,float('inf'), Counter(list(s))

        have={ch:count[ch]-n for ch in count if count[ch]>n}
        required=len(have)

        for r in range(len(s)):
            if s[r] in have:
                have[s[r]] -= 1
                required-= have[s[r]] == 0
            while required==0 and l < len(s):
                if  s[l] in have:
                    have[s[l]] += 1
                    required+= have[s[l]] > 0
                ans = min(ans, r - l + 1)
                l += 1
               
        return ans if (ans != float('inf') and ans > 0) else 0