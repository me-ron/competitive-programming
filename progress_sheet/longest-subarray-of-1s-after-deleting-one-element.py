class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count=0
        ans=0
        i=0
        j=0
        while j<len(nums):
            count += (nums[j] == 0 )
            while count>1:
                count-=(nums[i] == 0)
                i+=1
            j+=1
            ans=max(j-i,ans)
        return ans-1
                