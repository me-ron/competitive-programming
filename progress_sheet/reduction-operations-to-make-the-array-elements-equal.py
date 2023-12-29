class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        c=Counter(nums)
        s=sorted(c.keys())
        ans=0
        for i in range(len(s)):
            ans+=(i*c[s[i]])
        return ans
