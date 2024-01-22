class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        rem=sum(nums)%p
        if not rem:
            return 0
        ans=float("inf")
        run={0:-1}
        for i in range(len(nums)):
            if i!=0:
                nums[i]+=nums[i-1]
            if (nums[i]-rem)%p in run:
                ans = min(ans,i-run[(nums[i]-rem)%p])
            
            run[nums[i]%p]=i
        print(run)
        return ans if ans<len(nums) else -1
        
        