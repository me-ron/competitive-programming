class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans=float("inf")
        for i in range (len(nums)-2):
            j=i+1
            k=len(nums)-1
            while j<k:
                x=nums[j]+nums[k]+nums[i]
                if abs(x-target) < abs(ans-target):
                    ans=x
                if x<target:
                    j+=1
                else:
                    k-=1

        return ans
        
        