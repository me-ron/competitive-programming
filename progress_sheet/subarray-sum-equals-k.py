class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans=0
        i=0
        run={0:1}
        for j in range(len(nums)):
            if j!=0:
                nums[j]+=nums[j-1]
            if nums[j]-k in run:
                ans+=run[nums[j]-k]
            run[nums[j]]=run.get(nums[j],0)
            run[nums[j]]+=1

        return ans
        