class Solution:
    def dividePlayers(self, skills: List[int]) -> int:
        skills.sort()
        ans=0
        d=skills[0]+skills[-1]
        i,j=0,len(skills)-1
        while i<j:
            x=skills[i]+skills[j]
            if x!=d:
                return -1
            ans+=skills[i]*skills[j]
            i+=1
            j-=1
        return ans


        