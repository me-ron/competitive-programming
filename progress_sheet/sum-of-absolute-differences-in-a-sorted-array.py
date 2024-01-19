class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        ans=[]
        n=len(nums)
        left=0
        right=sum(nums)
        for i in range(len(nums)):
            sum_= i*nums[i]-left + right-(nums[i]*(n-i))
            ans.append(sum_)
            left+=nums[i]
            right-=nums[i]
        return ans
        