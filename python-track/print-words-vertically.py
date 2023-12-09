class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        n = len(max(s, key=len))
        ans = []
        for i in range(n):
            temp = ""
            for j in range(len(s)):
                if i < len(s[j]):
                    temp += s[j][i]
                else:
                    temp += ' '
            ans.append(temp.rstrip())
        return ans
        