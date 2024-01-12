class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans=0
        i=0
        count=0
        for j in range(len(nums)):
            count+=nums[j]%2
            while count>k:
                count-=nums[i]%2
                i+=1
            if count==k:
                temp=i
                while nums[temp]%2==0:
                    ans+=1
                    temp+=1
            ans+=(count==k)
        return ans


        