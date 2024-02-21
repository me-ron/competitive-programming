class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans, end = [], 0
        prev = 0
        last = {s[i]:i for i in range(len(s))}
        
        for i in range(len(s)):
            end = max(end, last[s[i]])
            if end == i:
                ans.append(i - prev + 1)
                prev = end + 1
        return ans
        
        