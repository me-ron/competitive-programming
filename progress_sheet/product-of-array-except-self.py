class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=1
        c=0
        for i in range(len(nums)):
            ans*=nums[i] if nums[i]!=0 else 1
            c+=nums[i]==0
        if c>1:
            return [0]*len(nums)

        for i in range(len(nums)):
            nums[i]= ans if nums[i]==0 else ans*(not c)//nums[i]
        return nums

