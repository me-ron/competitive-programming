class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort(key= lambda x: x<0)
        ans=[]
        n=len(nums)//2
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i+n])
        return ans
        