class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        t=len(nums)//3
        s=set(nums)
        ans=[]
        for i in s:
            if nums.count(i)>t:
                ans.append(i)
        return ans
        