class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        c2 = defaultdict(int)
        i = 0
        for j in range(len(s2)):
            c2[s2[j]] += s2[j] in c1
            if j - i + 1 > len(s1):
                c2[s2[i]] -= s2[i] in c1
                if c2[s2[i]] == 0:
                    c2.pop(s2[i])
                i += 1
            if c1 == c2:
                return True
        return False
        