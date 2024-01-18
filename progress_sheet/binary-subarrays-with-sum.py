class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        run={0:1}
        ans=0
        for i in range(len(nums)):
            if i!=0:
                nums[i]+=nums[i-1]

            if nums[i]-goal in run:
                ans+=run[nums[i]-goal]

            run[nums[i]]=run.get(nums[i],0)
            run[nums[i]]+=1
        return ans