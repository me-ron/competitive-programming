class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        c=Counter(answers)
        ans=0
        for i in c:
            ans+=(c[i]//(i+1))*(i+1)
            ans+=i+1 if c[i]%(i+1) else 0
        return ans
        