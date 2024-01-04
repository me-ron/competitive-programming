from collections import Counter
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans=0
        i,j=0,len(nums)-1
        while i<j:
            x=nums[i]+nums[j]
            if x==k:
                ans+=1
                i+=1
                j-=1
            elif x<k:
                i+=1
            else:
                j-=1
        return ans

                
        
        
        