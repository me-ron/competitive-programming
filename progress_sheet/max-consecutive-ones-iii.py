class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count=0
        ans=0
        i=0
        j=0
        while j<len(nums):
            count += (nums[j] == 0 )
            while count>k:
                count-=(nums[i] == 0)
                i+=1
            j+=1
            ans=max(j-i,ans)
        return ans
        