class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        c1 = Counter(p)
        c2 = defaultdict(int)
        i = 0
        for j in range(len(s)):
            if s[j] in c1:
                c2[s[j]] += 1
            if j - i + 1 > len(p):
                c2[s[i]] -= s[i] in c1
                if c2[s[i]] == 0:
                    c2.pop(s[i])
                i += 1
            if c1 == c2:
                ans.append(i)
        return ans
        