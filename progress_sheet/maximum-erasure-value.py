class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        i=0
        occured=set()
        ans=temp=0
        for j in range(len(nums)):
            temp+=nums[j]
            while nums[j] in occured:
                temp-=nums[i]
                occured.remove(nums[i])
                i+=1
            occured.add(nums[j])
            ans=max(temp,ans)
        return ans
        