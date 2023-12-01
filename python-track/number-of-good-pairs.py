class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hash={}
        ans=0
        for i in nums:
            if i in hash:
                hash[i]+=1
            else:
                hash[i]=0
        for j in hash:
            if hash[j]>0:
                n=hash[j]
                ans+=sum([i for i in range(1,n+1)])
        return ans

                    
        