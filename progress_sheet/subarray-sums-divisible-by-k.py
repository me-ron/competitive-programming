class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans=0
        run={0:1}
        for i in range(len(nums)):
            if i!=0:
                nums[i]+=nums[i-1]
            if nums[i]%k in run:
                ans+=run[nums[i]%k]
            
            run[nums[i]%k]=run.get(nums[i]%k,0)
            run[nums[i]%k]+=1
        return ans
        