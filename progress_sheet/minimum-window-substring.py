class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t = Counter(t)
        i = 0
        dis = len(s)+3
        x, y = 0, 0
        required = len(t)
        for j in range(len(s)):
            if s[j] in t:
                t[s[j]] -= 1
                required -= t[s[j]] == 0
            while required == 0:
                if dis > j - i + 1:
                    dis = j - i + 1
                    x, y = i, j
                if s[i] in t:
                    t[s[i]] += 1
                    required += t[s[i]] > 0
                i += 1
        return s[x:y+1] if dis <= len(s) else ""
                    
        
        