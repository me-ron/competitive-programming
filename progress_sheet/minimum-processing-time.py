class Solution:
    def minProcessingTime(self, p: List[int], t: List[int]) -> int:
        ans=0
        p.sort(reverse=True)
        t.sort()
        m=lambda x: x//4
        for i in range(len(t)):
            ans=max(p[m(i)]+t[i],ans)
        return ans

        